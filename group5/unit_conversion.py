import glob
import math

# import time
# import string
import pandas as pd
import numpy as np
import scipy
import scipy.interpolate as interp
import scipy.integrate as integrate

# import random
# import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec

from scipy.constants import c, m_p, e
import data_filter


def synchrotron_momentum(max_E, time):
    mpeV = m_p * c**2 / e  # Proton mass in eV
    R0 = 26  # Mean machine radius
    n_dip = 10  # Number of dipoles
    dip_l = 4.4  # Dipole length

    dip_angle = 2 * np.pi / n_dip  # Dipole bending angle
    rho = dip_l / dip_angle  # Dipole radius of curvature
    omega = 2 * np.pi * 50

    Ek = np.array([70, max_E]) * 1e6  # Injection and extraction kinetic energies
    E = Ek + mpeV  # Injection and extraction kinetic energies
    p = np.sqrt(E**2 - mpeV**2)  # Injection and extraction momenta

    B = p / c / rho  # Ideal magnetic field at injection and extraction energies

    Bdip = (
        lambda t: (B[1] + B[0] - (B[1] - B[0]) * np.cos(omega * t)) / 2
    )  # Idealised B-field variation with AC
    pdip = lambda t: Bdip(t) * rho * c  # Momentum from B-field in MeV

    return pdip(time * 1e-3)


def synchrotron_kinetic_energy(max_E, time):
    mpeV = m_p * c**2 / e  # Proton mass in eV
    # Relativistic Kinetic Energy = Relativistic Energy - mass
    return (
        np.sqrt(synchrotron_momentum(max_E, time) ** 2 + mpeV**2) - mpeV
    )  # Return array in eV
    # return (np.sqrt(synchrotron_momentum(max_E, time)**2 + mpeV**2) - mpeV)/1E6 # Return array in MeV


def divided_diff(x, y):
    """
    function to calculate the divided
    differences table
    """
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


def newton_poly(coef, x_data, x):
    """
    evaluate the newton polynomial
    at x
    """
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


def get_calibration_curve(data_points):
    BLM_Cal_x_time = np.array([0.0, 3.0, 5.0, 7.0, 9.0])
    # mVs/proton
    # BLM_Cal_y = np.array([2.22E-16, 2.59E-16, 4.31E-15, 1.60E-14, 3.50E-14])
    # vS/proton
    BLM_Cal_y = np.array([2.22e-16, 2.59e-16, 4.31e-15, 1.60e-14, 3.50e-14])

    a_s = divided_diff(BLM_Cal_x_time, BLM_Cal_y)[0, :]
    time_array = np.linspace(0.0, 10.0, data_points)

    # Original 1F method
    return newton_poly(a_s, BLM_Cal_x_time, time_array)


def calibration_curve_beta(t_min=-0.5, t_max=10.5, data_points=2200, max_E=800):
    BLM_Cal_x_time = np.array([0.0, 3.0, 5.0, 7.0, 9.0])
    # mVs/proton
    # BLM_Cal_y = np.array([2.22E-16, 2.59E-16, 4.31E-15, 1.60E-14, 3.50E-14])
    # vS/proton
    BLM_Cal_y = np.array([2.22e-16, 2.59e-16, 4.31e-15, 1.60e-14, 3.50e-14])

    time_array = np.linspace(t_min, t_max, data_points)

    # Default if in storage ring mode (fixed 70 MeV)
    if max_E == 70:
        return np.ones(len(time_array)) * BLM_Cal_y[0]

    # calculate data points to pass to calibration curve (only returns between 0 - 10 ms)
    t_range = t_max - t_min
    # t_excess = t_range - 10.
    t_scale = data_points / t_range  # points per millisecond
    # print(t_scale)
    cal_data_points = int(t_scale * 10)
    pre_data_points = int(t_scale * -t_min)
    post_data_points = int(t_scale * (t_max - 10))

    assert (cal_data_points + pre_data_points + post_data_points) == data_points

    a_s = divided_diff(BLM_Cal_x_time, BLM_Cal_y)[0, :]

    # Original 1F method
    calibration_curve = get_calibration_curve(
        cal_data_points
    )  # newton_poly(a_s, BLM_Cal_x_time, time_array)

    # Conditional: if time before first calibration data point, fix value
    if np.any(time_array < BLM_Cal_x_time[0]):
        # calibration_curve[np.where(time_array < 0)] = BLM_Cal_y[0]
        calibration_curve = np.concatenate(
            [np.ones(pre_data_points) * BLM_Cal_y[0], calibration_curve]
        )

    # Find Maximum - dependent on energy
    cal_max = 4.63e-14  # default to interpolated 800 MeV value

    # Conditional: if time before first calibration data point, fix value
    if np.any(time_array > 10.0):
        # calibration_curve[np.where(time_array < 0)] = BLM_Cal_y[0]
        calibration_curve = np.concatenate(
            [calibration_curve, np.ones(post_data_points) * cal_max]
        )

    # Conditional: between first two points use linear interpolation

    # calibration_curve[np.where(time_array < 0)] = BLM_Cal_y[0]

    return calibration_curve


def find_diff_between_adj(array):
    diff_integral = np.diff(array)
    diff_integral = np.insert(diff_integral, 0, array[0])

    return diff_integral


def get_integral(x, value):
    # print(x.shape, value.shape)
    integral = scipy.integrate.cumulative_trapezoid(value, x=x)
    return find_diff_between_adj(integral)


def blm_to_protons(blm_signal):
    # data_points = 2200
    # x_data = np.linspace(-0.5, 10.5, data_points)
    integrated_BLM_data = get_integral(np.linspace(-0.5, 10.5, 2200), blm_signal)
    return integrated_BLM_data / (
        calibration_curve_beta(t_min=-0.5, t_max=10.5, data_points=2200)[:-1]
    )


def blm_to_coloumbs(blm_signal):
    return blm_to_protons(blm_signal) * e


def blm_to_joules(blm_signal):
    """
    This function does not work ask Harron
    """
    proton_data = blm_to_protons(blm_signal)
    time_array = np.linspace(-0.5, 10.5, 2200)
    E = synchrotron_kinetic_energy(800.0, time_array) * 1e-6
    return (proton_data * (E[:-1] + 938.27208816) * 1.602e-19) * 1e6


def R5IM_to_protons(R5IM_data):
    return R5IM_data * 4e12


def R5IM_to_coloumbs(R5IM_data):
    return R5IM_to_protons(R5IM_data) * e
