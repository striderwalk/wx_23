import glob
import sys
import time
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import figure
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
import numpy as np
from PlottingTools import figure, makeErrorBar
from PlottingTools import makeAxes
from PlottingTools import plot
import matplotlib.patches as mpatches
import unit_conversion
import data_filter

r0_patch = mpatches.Patch(color="blue", label="R0")
r1_patch = mpatches.Patch(color="darkviolet", label="R1")
r2_patch = mpatches.Patch(color="deeppink", label="R2")
r3_patch = mpatches.Patch(color="crimson", label="R3")
r4_patch = mpatches.Patch(color="coral", label="R4")
r5_patch = mpatches.Patch(color="gold", label="R5")
r6_patch = mpatches.Patch(color="lime", label="R6")
r7_patch = mpatches.Patch(color="forestgreen", label="R7")
r8_patch = mpatches.Patch(color="turquoise", label="R8")
r9_patch = mpatches.Patch(color="cornflowerblue", label="R9")

DEMO = True


def cleanData(array):
    newArray = []
    filterer = DataFilter()
    filterer.reset
    array = filterer.apply(array)
    filterer.set("invert", True, "r5im")
    array = filterer.apply(array)

    for i in array:
        offsetData = offset_y_data(i, SpecialPoint=np.min(i))
        newArray.append(offsetData)

    return newArray


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        self.xrms = []
        self.yrms = []
        self.error_above = []
        self.error_below = []

        self.arr = []
        # setup main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1325, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # setup the lcds ----------------------------------------------------------->

        # coulombs
        self.coulomb_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.coulomb_lcd.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.coulomb_lcd.setObjectName("coulomb_lcd")
        self.coulombs_label = QtWidgets.QLabel(self.centralwidget)
        self.coulombs_label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.coulombs_label.setFont(font)
        self.coulombs_label.setObjectName("coulombs_label")

        # volts
        self.volt_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.volt_lcd.setGeometry(QtCore.QRect(130, 50, 81, 31))
        self.volt_lcd.setObjectName("volt_lcd")

        self.joules_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.joules_lcd.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.joules_lcd.setObjectName("joules_lcd")
        self.joules_label = QtWidgets.QLabel(self.centralwidget)
        self.joules_label.setGeometry(QtCore.QRect(230, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.joules_label.setFont(font)
        self.joules_label.setObjectName("joules_label")

        self.protons_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.protons_lcd.setGeometry(QtCore.QRect(320, 50, 81, 31))
        self.protons_lcd.setObjectName("protons_lcd")
        self.protons_lablel = QtWidgets.QLabel(self.centralwidget)
        self.protons_lablel.setGeometry(QtCore.QRect(320, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.protons_lablel.setFont(font)
        self.protons_lablel.setObjectName("protons_lablel")

        self.volts_label = QtWidgets.QLabel(self.centralwidget)
        self.volts_label.setGeometry(QtCore.QRect(140, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.volts_label.setFont(font)
        self.volts_label.setObjectName("volts_label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 921, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.vbox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName("vbox")

        self.fig, self.spec = figure(2, 1)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar2QT(self.canvas)
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)

        # setup R0 buttons
        self.R0 = QtWidgets.QCheckBox(self.centralwidget)
        self.R0.setGeometry(QtCore.QRect(970, 90, 51, 20))
        self.R0.setObjectName("R0")

        self.groupBox_R0 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R0.setGeometry(QtCore.QRect(960, 110, 81, 131))
        self.groupBox_R0.setTitle("")
        self.groupBox_R0.setObjectName("groupBox_R0")
        self.verticalLayoutWidget_29 = QtWidgets.QWidget(self.groupBox_R0)
        self.verticalLayoutWidget_29.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_29.setObjectName("verticalLayoutWidget_29")
        self.verticalLayout_R0 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_29)
        self.verticalLayout_R0.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R0.setObjectName("verticalLayout_R0")
        self.R0_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_29)
        self.R0_BLM1.setObjectName("R0_BLM1")
        self.verticalLayout_R0.addWidget(self.R0_BLM1)
        self.R0_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_29)
        self.R0_BLM3.setObjectName("R0_BLM3")
        self.verticalLayout_R0.addWidget(self.R0_BLM3)
        self.R0_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_29)
        self.R0_BLM4.setObjectName("R0_BLM4")
        self.verticalLayout_R0.addWidget(self.R0_BLM4)

        self.R0_blm_buttons = [self.R0_BLM1, self.R0_BLM3, self.R0_BLM4]

        # setup R1 buttons
        self.R1 = QtWidgets.QCheckBox(self.centralwidget)
        self.R1.setGeometry(QtCore.QRect(1060, 90, 51, 20))
        self.R1.setObjectName("R1")

        self.groupBox_R1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R1.setGeometry(QtCore.QRect(1050, 110, 81, 131))
        self.groupBox_R1.setTitle("")
        self.groupBox_R1.setObjectName("groupBox_R1")
        self.verticalLayoutWidget_33 = QtWidgets.QWidget(self.groupBox_R1)
        self.verticalLayoutWidget_33.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_33.setObjectName("verticalLayoutWidget_33")
        self.verticalLayout_R1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_33)
        self.verticalLayout_R1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R1.setObjectName("verticalLayout_R1")
        self.R1_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_33)
        self.R1_BLM1.setObjectName("R1_BLM1")
        self.verticalLayout_R1.addWidget(self.R1_BLM1)
        self.R1_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_33)
        self.R1_BLM2.setObjectName("R1_BLM2")
        self.verticalLayout_R1.addWidget(self.R1_BLM2)
        self.R1_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_33)
        self.R1_BLM3.setObjectName("R1_BLM3")
        self.verticalLayout_R1.addWidget(self.R1_BLM3)
        self.R1_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_33)
        self.R1_BLM4.setObjectName("R1_BLM4")
        self.verticalLayout_R1.addWidget(self.R1_BLM4)

        self.R1_blm_buttons = [self.R1_BLM1, self.R1_BLM2, self.R1_BLM3, self.R1_BLM4]

        # setup R2 buttons
        self.R2 = QtWidgets.QCheckBox(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(1150, 90, 51, 20))
        self.R2.setObjectName("R2")

        self.groupBox_R2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R2.setGeometry(QtCore.QRect(1140, 110, 81, 131))
        self.groupBox_R2.setTitle("")
        self.groupBox_R2.setObjectName("groupBox_R2")
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(self.groupBox_R2)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_R2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_R2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R2.setObjectName("verticalLayout_R2")
        self.R2_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_18)
        self.R2_BLM1.setObjectName("R2_BLM1")
        self.verticalLayout_R2.addWidget(self.R2_BLM1)
        self.R2_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_18)
        self.R2_BLM2.setObjectName("R2_BLM2")
        self.verticalLayout_R2.addWidget(self.R2_BLM2)
        self.R2_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_18)
        self.R2_BLM3.setObjectName("R2_BLM3")
        self.verticalLayout_R2.addWidget(self.R2_BLM3)
        self.R2_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_18)
        self.R2_BLM4.setObjectName("R2_BLM4")
        self.verticalLayout_R2.addWidget(self.R2_BLM4)

        self.R2_blm_buttons = [self.R2_BLM1, self.R2_BLM2, self.R2_BLM3, self.R2_BLM4]

        # setup R3 buttons
        self.R3 = QtWidgets.QCheckBox(self.centralwidget)
        self.R3.setGeometry(QtCore.QRect(1240, 90, 51, 20))
        self.R3.setObjectName("R3")

        self.groupBox_R3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R3.setGeometry(QtCore.QRect(1230, 110, 81, 131))
        self.groupBox_R3.setTitle("")
        self.groupBox_R3.setObjectName("groupBox_R3")
        self.verticalLayoutWidget_21 = QtWidgets.QWidget(self.groupBox_R3)
        self.verticalLayoutWidget_21.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_21.setObjectName("verticalLayoutWidget_21")
        self.verticalLayout_R3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_R3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R3.setObjectName("verticalLayout_R3")
        self.R3_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_21)
        self.R3_BLM1.setObjectName("R3_BLM1")
        self.verticalLayout_R3.addWidget(self.R3_BLM1)
        self.R3_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_21)
        self.R3_BLM2.setObjectName("R3_BLM2")
        self.verticalLayout_R3.addWidget(self.R3_BLM2)
        self.R3_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_21)
        self.R3_BLM3.setObjectName("R3_BLM3")
        self.verticalLayout_R3.addWidget(self.R3_BLM3)
        self.R3_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_21)
        self.R3_BLM4.setObjectName("R3_BLM4")
        self.verticalLayout_R3.addWidget(self.R3_BLM4)

        self.R3_blm_buttons = [self.R3_BLM1, self.R3_BLM2, self.R3_BLM3, self.R3_BLM4]

        # setup R4 buttons
        self.R4 = QtWidgets.QCheckBox(self.centralwidget)
        self.R4.setGeometry(QtCore.QRect(970, 250, 51, 20))
        self.R4.setObjectName("R4")

        self.groupBox_R4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R4.setGeometry(QtCore.QRect(960, 270, 81, 131))
        self.groupBox_R4.setTitle("")
        self.groupBox_R4.setObjectName("groupBox_R4")
        self.verticalLayoutWidget_34 = QtWidgets.QWidget(self.groupBox_R4)
        self.verticalLayoutWidget_34.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_34.setObjectName("verticalLayoutWidget_34")
        self.verticalLayout_R4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_34)
        self.verticalLayout_R4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R4.setObjectName("verticalLayout_R4")
        self.R4_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_34)
        self.R4_BLM1.setObjectName("R4_BLM1")
        self.verticalLayout_R4.addWidget(self.R4_BLM1)
        self.R4_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_34)
        self.R4_BLM2.setObjectName("R4_BLM2")
        self.verticalLayout_R4.addWidget(self.R4_BLM2)
        self.R4_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_34)
        self.R4_BLM3.setObjectName("R4_BLM3")
        self.verticalLayout_R4.addWidget(self.R4_BLM3)
        self.R4_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_34)
        self.R4_BLM4.setObjectName("R4_BLM4")
        self.verticalLayout_R4.addWidget(self.R4_BLM4)

        self.R4_blm_buttons = [self.R4_BLM1, self.R4_BLM2, self.R4_BLM3, self.R4_BLM4]

        # setup R5 buttons
        self.R5 = QtWidgets.QCheckBox(self.centralwidget)
        self.R5.setGeometry(QtCore.QRect(1060, 250, 51, 20))
        self.R5.setObjectName("R5")

        self.groupBox_R5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R5.setGeometry(QtCore.QRect(1050, 270, 81, 131))
        self.groupBox_R5.setTitle("")
        self.groupBox_R5.setObjectName("groupBox_R5")
        self.verticalLayoutWidget_37 = QtWidgets.QWidget(self.groupBox_R5)
        self.verticalLayoutWidget_37.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_37.setObjectName("verticalLayoutWidget_37")
        self.verticalLayout_R5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_37)
        self.verticalLayout_R5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R5.setObjectName("verticalLayout_R5")
        self.R5_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_37)
        self.R5_BLM1.setObjectName("R5_BLM1")
        self.verticalLayout_R5.addWidget(self.R5_BLM1)
        self.R5_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_37)
        self.R5_BLM2.setObjectName("R5_BLM2")
        self.verticalLayout_R5.addWidget(self.R5_BLM2)
        self.R5_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_37)
        self.R5_BLM3.setObjectName("R5_BLM3")
        self.verticalLayout_R5.addWidget(self.R5_BLM3)
        self.R5_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_37)
        self.R5_BLM4.setObjectName("R5_BLM4")
        self.verticalLayout_R5.addWidget(self.R5_BLM4)

        self.R5_blm_buttons = [self.R5_BLM1, self.R5_BLM2, self.R5_BLM3, self.R5_BLM4]

        # setup R6 buttons
        self.R6 = QtWidgets.QCheckBox(self.centralwidget)
        self.R6.setGeometry(QtCore.QRect(1150, 250, 51, 20))
        self.R6.setObjectName("R6")

        self.groupBox_R6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R6.setGeometry(QtCore.QRect(1140, 270, 81, 131))
        self.groupBox_R6.setTitle("")
        self.groupBox_R6.setObjectName("groupBox_R6")
        self.verticalLayoutWidget_30 = QtWidgets.QWidget(self.groupBox_R6)
        self.verticalLayoutWidget_30.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_30.setObjectName("verticalLayoutWidget_30")
        self.verticalLayout_R6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_30)
        self.verticalLayout_R6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R6.setObjectName("verticalLayout_R6")
        self.R6_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_30)
        self.R6_BLM1.setObjectName("R6_BLM1")
        self.verticalLayout_R6.addWidget(self.R6_BLM1)
        self.R6_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_30)
        self.R6_BLM2.setObjectName("R6_BLM2")
        self.verticalLayout_R6.addWidget(self.R6_BLM2)
        self.R6_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_30)
        self.R6_BLM3.setObjectName("R6_BLM3")
        self.verticalLayout_R6.addWidget(self.R6_BLM3)
        self.R6_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_30)
        self.R6_BLM4.setObjectName("R6_BLM4")
        self.verticalLayout_R6.addWidget(self.R6_BLM4)

        self.R6_blm_buttons = [self.R6_BLM1, self.R6_BLM2, self.R6_BLM3, self.R6_BLM4]

        # setup R7 buttons
        self.R7 = QtWidgets.QCheckBox(self.centralwidget)
        self.R7.setGeometry(QtCore.QRect(1240, 250, 51, 20))
        self.R7.setObjectName("R7")

        self.groupBox_R7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R7.setGeometry(QtCore.QRect(1230, 270, 81, 131))
        self.groupBox_R7.setTitle("")
        self.groupBox_R7.setObjectName("groupBox_R7")
        self.verticalLayoutWidget_39 = QtWidgets.QWidget(self.groupBox_R7)
        self.verticalLayoutWidget_39.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_39.setObjectName("verticalLayoutWidget_39")
        self.verticalLayout_R7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_39)
        self.verticalLayout_R7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R7.setObjectName("verticalLayout_R7")
        self.R7_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_39)
        self.R7_BLM1.setObjectName("R7_BLM1")
        self.verticalLayout_R7.addWidget(self.R7_BLM1)
        self.R7_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_39)
        self.R7_BLM2.setObjectName("R7_BLM2")
        self.verticalLayout_R7.addWidget(self.R7_BLM2)
        self.R7_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_39)
        self.R7_BLM3.setObjectName("R7_BLM3")
        self.verticalLayout_R7.addWidget(self.R7_BLM3)
        self.R7_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_39)
        self.R7_BLM4.setObjectName("R7_BLM4")
        self.verticalLayout_R7.addWidget(self.R7_BLM4)

        self.R7_blm_buttons = [self.R7_BLM1, self.R7_BLM2, self.R7_BLM3, self.R7_BLM4]

        # setup R8 buttons
        self.R8.setObjectName("R8")
        self.R8 = QtWidgets.QCheckBox(self.centralwidget)
        self.R8.setGeometry(QtCore.QRect(1240, 250, 61, 20))
        self.R8.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')

        self.groupBox_R8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R8.setGeometry(QtCore.QRect(1230, 270, 81, 131))
        self.groupBox_R8.setTitle("")
        self.groupBox_R8.setObjectName("groupBox_R8")
        self.verticalLayoutWidget_43 = QtWidgets.QWidget(self.groupBox_R8)
        self.verticalLayoutWidget_43.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_43.setObjectName("verticalLayoutWidget_43")
        self.verticalLayout_R8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_43)
        self.verticalLayout_R8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R8.setObjectName("verticalLayout_R8")
        self.R8_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_43)
        self.R8_BLM1.setObjectName("R8_BLM1")
        self.verticalLayout_R8.addWidget(self.R8_BLM1)
        self.R8_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_43)
        self.R8_BLM2.setObjectName("R8_BLM2")
        self.verticalLayout_R8.addWidget(self.R8_BLM2)
        self.R8_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_43)
        self.R8_BLM3.setObjectName("R8_BLM3")
        self.verticalLayout_R8.addWidget(self.R8_BLM3)
        self.R8_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_43)
        self.R8_BLM4.setObjectName("R8_BLM4")
        self.verticalLayout_R8.addWidget(self.R8_BLM4)

        self.R8_blm_buttons = [self.R8_BLM1, self.R8_BLM2, self.R8_BLM3, self.R8_BLM4]

        # setup R9 buttons
        self.R9 = QtWidgets.QCheckBox(self.centralwidget)
        self.R9.setGeometry(QtCore.QRect(1330, 250, 61, 20))
        self.R9.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R9.setObjectName("R9")

        self.groupBox_R9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R9.setGeometry(QtCore.QRect(1320, 270, 81, 131))
        self.groupBox_R9.setTitle("")
        self.groupBox_R9.setObjectName("groupBox_R9")
        self.verticalLayoutWidget_45 = QtWidgets.QWidget(self.groupBox_R9)
        self.verticalLayoutWidget_45.setGeometry(QtCore.QRect(10, 10, 61, 111))
        self.verticalLayoutWidget_45.setObjectName("verticalLayoutWidget_45")
        self.verticalLayout_R9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_45)
        self.verticalLayout_R9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_R9.setObjectName("verticalLayout_R9")
        self.R9_BLM1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_45)
        self.R9_BLM1.setObjectName("R9_BLM1")
        self.verticalLayout_R9.addWidget(self.R9_BLM1)
        self.R9_BLM2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_45)
        self.R9_BLM2.setObjectName("R9_BLM2")
        self.verticalLayout_R9.addWidget(self.R9_BLM2)
        self.R9_BLM3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_45)
        self.R9_BLM3.setObjectName("R9_BLM3")
        self.verticalLayout_R9.addWidget(self.R9_BLM3)
        self.R9_BLM4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_45)
        self.R9_BLM4.setObjectName("R9_BLM4")

        self.R9_blm_buttons = [self.R9_BLM1, self.R9_BLM2, self.R9_BLM3, self.R9_BLM4]

        self.clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all.setGeometry(QtCore.QRect(1170, 540, 93, 28))
        self.clear_all.setObjectName("clear_all")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(960, 670, 171, 101))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.blm_sum_min_time = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.blm_sum_min_time.setGeometry(QtCore.QRect(50, 20, 71, 31))
        self.blm_sum_min_time.setMinimum(-0.5)
        self.blm_sum_min_time.setValue(0)
        self.blm_sum_min_time.setMaximum(10.5)
        self.blm_sum_min_time.setObjectName("blm_sum_min_time")
        self.blm_sum_max_time = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.blm_sum_max_time.setGeometry(QtCore.QRect(50, 60, 71, 31))
        self.blm_sum_max_time.setMinimum(-0.5)
        self.blm_sum_max_time.setValue(10)
        self.blm_sum_max_time.setMaximum(10.5)
        self.blm_sum_max_time.setObjectName("blm_sum_max_time")
        self.blm_unit_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.blm_unit_groupBox.setGeometry(QtCore.QRect(410, 30, 120, 51))
        self.blm_unit_groupBox.setObjectName("blm_unit_groupBox")
        self.blm_unit_drop_down = QtWidgets.QComboBox(self.blm_unit_groupBox)
        self.blm_unit_drop_down.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.blm_unit_drop_down.setObjectName("blm_unit_drop_down")
        self.blm_unit_drop_down.addItem("")
        self.blm_unit_drop_down.addItem("")
        self.blm_unit_drop_down.addItem("")
        self.blm_unit_drop_down.addItem("")

        self.R5IM_unit_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.R5IM_unit_groupBox.setGeometry(QtCore.QRect(540, 30, 120, 51))
        self.R5IM_unit_groupBox.setObjectName("R5IM_unit_groupBox")
        self.R5IM_unit_drop_down = QtWidgets.QComboBox(self.R5IM_unit_groupBox)
        self.R5IM_unit_drop_down.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.R5IM_unit_drop_down.setObjectName("R5IM_unit_drop_down")
        self.R5IM_unit_drop_down.addItem("")
        self.R5IM_unit_drop_down.addItem("")
        self.R5IM_unit_drop_down.addItem("")

        self.mode_selection = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_selection.setGeometry(QtCore.QRect(1150, 580, 121, 121))
        self.mode_selection.setObjectName("mode_selection")

        self.mode_verticalLayout = QtWidgets.QVBoxLayout(self.mode_selection)
        self.mode_verticalLayout.setGeometry(QtCore.QRect(10, 30, 71, 80))
        # self.mode_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mode_verticalLayout.setObjectName("mode_verticalLayout")

        self.mean_button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.mean_button.setObjectName("mean_button")
        self.mean_button.click()
        self.sum_button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sum_button.setObjectName("sum_button")

        self.mode_verticalLayout.addWidget(self.mean_button)
        self.mode_verticalLayout.addWidget(self.sum_button)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1160, 430, 131, 101))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.SUM = QtWidgets.QCheckBox(self.groupBox_3)
        self.SUM.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.SUM.setObjectName("SUM")
        self.SUM_MINUS_R1_R2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.SUM_MINUS_R1_R2.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.SUM_MINUS_R1_R2.setObjectName("SUM_MINUS_R1_R2")
        self.R5IM = QtWidgets.QCheckBox(self.groupBox_3)
        self.R5IM.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.R5IM.setObjectName("checkBox")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(960, 570, 171, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.N_time = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.N_time.setGeometry(QtCore.QRect(10, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N_time.setFont(font)
        self.N_time.setMaximum(500.0)
        self.N_time.setObjectName("N_time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1325, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.y_axis_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.y_axis_groupBox.setGeometry(QtCore.QRect(1150, 700, 130, 150))
        self.y_axis_groupBox.setObjectName("y_axis_groupBox")
        self.y_axis_min = QtWidgets.QDoubleSpinBox(self.y_axis_groupBox)
        self.y_axis_min.setGeometry(QtCore.QRect(50, 60, 71, 31))
        self.y_axis_min.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.y_axis_min.setMaximum(-20)
        self.y_axis_min.setMaximum(20)
        self.y_axis_min.setValue(-20)

        self.y_axis_min.setObjectName("y_axis_min")
        self.y_axis_max = QtWidgets.QDoubleSpinBox(self.y_axis_groupBox)
        self.y_axis_max.setGeometry(QtCore.QRect(50, 20, 71, 31))
        self.y_axis_max.setStyleSheet("background-color: rgb(232, 232, 232)")

        self.y_axis_max.setMaximum(-20)
        self.y_axis_max.setMaximum(20)
        self.y_axis_max.setValue(15)
        self.y_axis_max.setObjectName("y_axis_max")

        self.auto_scale_y = QtWidgets.QPushButton(self.y_axis_groupBox)
        self.auto_scale_y.setGeometry(QtCore.QRect(10, 90, 41, 41))

        self.y_axis_min_label = QtWidgets.QLabel(self.y_axis_groupBox)
        self.y_axis_min_label.setGeometry(QtCore.QRect(10, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.y_axis_min_label.setFont(font)
        self.y_axis_min_label.setObjectName("y_axis_min_label")
        self.y_axis_max_label = QtWidgets.QLabel(self.y_axis_groupBox)
        self.y_axis_max_label.setGeometry(QtCore.QRect(10, 30, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.y_axis_max_label.setFont(font)
        self.y_axis_max_label.setObjectName("y_axis_max_label")

        self.btnLbls = [
            "r0_blm1",
            "r0_blm3",
            "r0_blm4",
            "r1_blm1",
            "r1_blm2",
            "r1_blm3",
            "r1_blm4",
            "r2_blm1",
            "r2_blm2",
            "r2_blm3",
            "r2_blm4",
            "r3_blm1",
            "r3_blm2",
            "r3_blm3",
            "r3_blm4",
            "r4_blm1",
            "r4_blm2",
            "r4_blm3",
            "r4_blm4",
            "r5_blm1",
            "r5_blm2",
            "r5_blm3",
            "r5_blm4",
            "r6_blm1",
            "r6_blm2",
            "r6_blm3",
            "r6_blm4",
            "r7_blm1",
            "r7_blm2",
            "r7_blm3",
            "r7_blm4",
            "r8_blm1",
            "r8_blm2",
            "r8_blm3",
            "r8_blm4",
            "r9_blm1",
            "r9_blm2",
            "r9_blm3",
            "r9_blm4",
        ]

        self.btnsChecked = [False for x in range(39)]

        self.blm_buttons = [
            *self.R0_blm_buttons,
            *self.R1_blm_buttons,
            *self.R2_blm_buttons,
            *self.R3_blm_buttons,
            *self.R4_blm_buttons,
            *self.R5_blm_buttons,
            *self.R6_blm_buttons,
            *self.R7_blm_buttons,
            *self.R8_blm_buttons,
            *self.R9_blm_buttons,
        ]

        self.all_blm_buttons = [
            *self.R0_blm_buttons,
            *self.R1_blm_buttons,
            *self.R2_blm_buttons,
            *self.R3_blm_buttons,
            *self.R4_blm_buttons,
            *self.R5_blm_buttons,
            *self.R6_blm_buttons,
            *self.R7_blm_buttons,
            *self.R8_blm_buttons,
            *self.R9_blm_buttons,
            self.R0,
            self.R1,
            self.R2,
            self.R3,
            self.R4,
            self.R5,
            self.R6,
            self.R7,
            self.R8,
            self.R9,
        ]

        for button in self.blm_buttons:
            button.stateChanged.connect(self.btnChecked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect all the buttons
        self.R0.stateChanged.connect(self.set_R0)
        self.R1.stateChanged.connect(self.set_R1)
        self.R2.stateChanged.connect(self.set_R2)
        self.R3.stateChanged.connect(self.set_R3)
        self.R4.stateChanged.connect(self.set_R4)
        self.R5.stateChanged.connect(self.set_R5)
        self.R6.stateChanged.connect(self.set_R6)
        self.R7.stateChanged.connect(self.set_R7)
        self.R8.stateChanged.connect(self.set_R8)
        self.R9.stateChanged.connect(self.set_R9)
        self.clear_all.clicked.connect(self.clear_all_buttons)

        # setup demo mode
        if DEMO:
            self.dumy_data_count = 0
            timer = QtCore.QTimer(MainWindow)
            timer.timeout.connect(self.get_demo_data)
            timer.start()
        else:
            print("WARNING: demo mode is the only ")

    def retranslateUi(self, MainWindow):
        """
        Setup the names
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.coulombs_label.setText(_translate("MainWindow", "Coulombs lost"))
        self.protons_lablel.setText(_translate("MainWindow", "Protons lost"))
        self.joules_label.setText(_translate("MainWindow", "Joules lost"))
        self.volts_label.setText(_translate("MainWindow", "Volts lost"))
        self.R0.setText(_translate("MainWindow", "R0"))
        self.R2.setText(_translate("MainWindow", "R2"))
        self.R1.setText(_translate("MainWindow", "R1"))
        self.R9.setText(_translate("MainWindow", "R9"))
        self.R8.setText(_translate("MainWindow", "R8"))
        self.R6.setText(_translate("MainWindow", "R6"))
        self.R7.setText(_translate("MainWindow", "R7"))
        self.R3.setText(_translate("MainWindow", "R3"))
        self.R5.setText(_translate("MainWindow", "R5"))
        self.R4.setText(_translate("MainWindow", "R4"))
        self.R2_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R2_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R2_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R2_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R0_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R0_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R0_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R1_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R1_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R1_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R1_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R3_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R3_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R3_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R3_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R6_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R6_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R6_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R6_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R4_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R4_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R4_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R4_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R5_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R5_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R5_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R5_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R7_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R7_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R7_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R7_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R8_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R8_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R8_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R8_BLM4.setText(_translate("MainWindow", "blm4"))
        self.R9_BLM1.setText(_translate("MainWindow", "blm1"))
        self.R9_BLM2.setText(_translate("MainWindow", "blm2"))
        self.R9_BLM3.setText(_translate("MainWindow", "blm3"))
        self.R9_BLM4.setText(_translate("MainWindow", "blm4"))
        self.clear_all.setText(_translate("MainWindow", "CLEAR ALL"))
        self.groupBox.setTitle(_translate("MainWindow", "BLM SUM- time (ms)"))
        self.label_3.setText(_translate("MainWindow", "MIN"))
        self.label_4.setText(_translate("MainWindow", "MAX"))
        self.mode_selection.setTitle(_translate("MainWindow", "Select method"))

        self.mean_button.setText(_translate("MainWindow", "Mean"))
        self.sum_button.setText(_translate("MainWindow", "Sum"))
        self.blm_unit_groupBox.setTitle(_translate("MainWindow", "Select units BLMs"))
        self.blm_unit_drop_down.setItemText(0, _translate("MainWindow", "Millivolts"))
        self.blm_unit_drop_down.setItemText(1, _translate("MainWindow", "Protons"))
        self.blm_unit_drop_down.setItemText(2, _translate("MainWindow", "Coloumbs"))
        self.blm_unit_drop_down.setItemText(3, _translate("MainWindow", "Joules"))

        self.R5IM_unit_groupBox.setTitle(_translate("MainWindow", "Select units R5IM"))
        self.R5IM_unit_drop_down.setItemText(0, _translate("MainWindow", "Millivolts"))
        self.R5IM_unit_drop_down.setItemText(1, _translate("MainWindow", "Protons"))
        self.R5IM_unit_drop_down.setItemText(2, _translate("MainWindow", "Coloumbs"))

        self.SUM.setText(_translate("MainWindow", "SUM"))
        self.SUM_MINUS_R1_R2.setText(_translate("MainWindow", "SUM -R1 -R2"))
        self.R5IM.setText(_translate("MainWindow", "R5IM"))
        self.groupBox_5.setTitle(_translate("MainWindow", "RMS- display time (sec)"))

        self.y_axis_min_label.setText(_translate("MainWindow", "MIN"))
        self.y_axis_max_label.setText(_translate("MainWindow", "MAX"))
        self.auto_scale_y.setText(_translate("MainWindow", "Auto scale"))
        self.y_axis_groupBox.setTitle(_translate("MainWindow", "RMS- y axis"))

    def rms(self, data_point):
        self.arr.append(data_point)
        if len(self.arr) < 5:
            return

        self.arr.pop(0)
        return np.std(self.arr, axis=0)

    def sumBLMs(self, array):
        filterer = data_filter.DataFilter()
        filterer.set(
            "select", False, ["r0blm1", "r5im"]
        )  # removes r0blm1 and r5im from the array
        filteredArray = filterer.apply(array)
        result = np.sum(filteredArray, 0)
        return result

    def sumBLMs_exclude12(self, array):
        filterer = data_filter.DataFilter()
        filterer.set(
            "select", False, ["r0blm1", "r5im"]
        )  # removes r0blm1 and r5im from the array
        filterer.set(
            "select",
            False,
            [
                "r1blm1",
                "r1blm2",
                "r1blm3",
                "r1blm4",
                "r2blm1",
                "r2blm2",
                "r2blm3",
                "r2blm4",
            ],
        )  # removes r1 and r2 from the array
        filteredArray = filterer.apply(array)
        result = np.sum(filteredArray, 0)
        return result

    def get_demo_data(self):
        # print(time.time())
        file_name = glob.glob("./cycle/*.csv")[self.dumy_data_count]
        # print(file_name)
        input_data = pd.read_csv(file_name)
        input_data = input_data.drop(columns=input_data.columns[0]).to_numpy()

        self.update(np.linspace(-0.05, 10.5, 2200), input_data)
        self.dumy_data_count += 1
        self.dumy_data_count %= 18

    def convert_units(self, y):
        if self.blm_unit_drop_down.currentText() == "Coloumbs":
            blm_data = np.array(map(unit_conversion.blm_to_coloumbs, y[:39]))
            blm_data = np.insert(blm_data, 0, 0)

        elif self.blm_unit_drop_down.currentText() == "Joules":
            blm_data = np.array(map(unit_conversion.blm_to_joules, y[:39]))
            blm_data = np.insert(blm_data, 0, 0)
        elif self.blm_unit_drop_down.currentText() == "Millivolts":
            blm_data = y[:-1]
        elif self.blm_unit_drop_down.currentText() == "Protons":
            blm_data = np.array(map(unit_conversion.blm_to_proton, y[:39]))
            blm_data = np.insert(blm_data, 0, 0)
        else:
            raise ValueError(
                f"blm_unit_drop_down has unknow value {self.blm_unit_drop_down.currentText()}"
            )

        if self.R5IM_unit_drop_down.currentText() == "Millivolts":
            r5im = y[-1]
        elif self.R5IM_unit_drop_down.currentText() == "Protons":
            r5im = unit_conversion.R5IM_to_protons(y[-1])
        elif self.R5IM_unit_drop_down.currentText() == "Coulombs":
            r5im = unit_conversion.R5IM_to_coloumbs(y[-1])
        else:
            raise ValueError("R5IM_unit_drop_down has unknow value")

        y = np.insert(blm_data, 39, r5im, axis=0)
        return y

    def mode(self, data):
        return np.mean(data.ravel())

    def sum(self, data):
        return np.sum(data.ravel())

    def update(self, x, y):
        y = cleanData(y)
        min_time = self.blm_sum_min_time.value() * 0.9
        max_time = self.blm_sum_max_time.value() * 1.10
        min_index = round(self.blm_sum_min_time.value() * 200) + 100
        max_index = round(self.blm_sum_max_time.value() * 200) + 100

        y = self.convert_units(y)
        x = x[min_index:max_index]
        y = y[:, min_index:max_index]

        self.fig.clear()
        self.plotBlmGraph(x, y, min_time=min_time, max_time=max_time)

        # find the data that has been selected to calaclate and plot rms
        selected_data = []
        for i in range(len(self.btnsChecked)):
            if self.btnsChecked[i]:
                selected_data.append(y[i])

        if self.SUM.isChecked():
            selected_data.append(self.sumBLMs(y))

        if self.SUM_MINUS_R1_R2.isChecked():
            selected_data.append(self.sumBLMs_exclude12(y))

        if self.R5IM.isChecked():
            selected_data.append(y[-1])

        # disply_rms vaule
        selected_data = np.array(selected_data)
        if len(selected_data) == 0:
            return
        if self.mean_button.isChecked():
            y_point = self.mode(selected_data)
        elif self.sum_button.isChecked():
            y_point = self.sum(selected_data)
        else:
            raise ValueError("mean or sum must be selected")

        rms = self.rms(y_point)
        if rms:
            self.plotRMSgraph(y_point, rms)

    def plotBlmGraph(
        self, x, y, xlbl="", ylbl="", lbl="line", min_time=None, max_time=None
    ):
        self.blmAx, self.r5imax = makeAxes(self.fig, self.spec, 0, True, "mV")
        # plot the selected Blm graphs
        for i in range(len(self.btnsChecked)):
            if self.btnsChecked[i]:
                self.blmAx = plot(
                    x,
                    y[i],
                    self.blmAx,
                    lbl=self.btnLbls[i],
                    xmin=min_time,
                    xmax=max_time,
                    ymin=-0.02,
                    ymax=0.3,
                )
        # plot the blm sum if selected
        if self.SUM.isChecked():
            plot(
                x,
                self.sumBLMs(y),
                self.blmAx,
                lbl="BLM SUM",
                xmin=min_time,
                xmax=max_time,
                ymin=-0.02,
                ymax=0.3,
            )

        # plot the blm sum -(R1+R2) if selected
        if self.SUM_MINUS_R1_R2.isChecked():
            plot(
                x,
                self.sumBLMs_exclude12(y),
                self.blmAx,
                lbl="BLM SUM minis (R1+R2)",
                xmin=min_time,
                xmax=max_time,
                ymin=-0.02,
                ymax=0.3,
            )

        # plot R5IM if selected
        if self.R5IM.isChecked():
            plot(
                x,
                -y[-1],
                self.r5imax,
                lbl="R5IM",
                xmin=min_time,
                xmax=max_time,
                ymin=-0.02,
                ymax=3.5,
                legend="upper left",
            )

    def plotRMSgraph(self, y, rms):
        self.error_above.append(y + rms)
        self.error_below.append(y - rms)

        self.xrms.append(len(self.xrms) + 1)
        self.yrms.append(y)

        if len(self.xrms) > 50:
            self.xrms.pop()
            self.yrms.pop(0)
            self.error_above.pop(0)
            self.error_below.pop(0)

        self.sumAx = makeAxes(self.fig, self.spec, index=1)
        y_min = self.y_axis_min.value()
        y_max = self.y_axis_max.value()

        self.sumAx = plot(
            self.xrms,
            self.yrms,
            self.sumAx,
            True,
            "Time(s)",
            xmin=0,
            xmax=50,
            ymin=y_min,
            ymax=y_max,
        )
        self.sumAx = plot(
            self.xrms,
            self.error_below,
            self.sumAx,
            False,
            "Time(s)",
            xmin=0,
            xmax=50,
            ymin=y_min,
            ymax=y_max,
        )
        self.sumAx = plot(
            self.xrms,
            self.error_above,
            self.sumAx,
            False,
            "Time(s)",
            xmin=0,
            xmax=50,
            ymin=y_min,
            ymax=y_max,
        )
        self.sumAx.fill_between(
            self.xrms,
            self.error_above,
            self.error_below,
            alpha=0.5,
            edgecolor="#CC4F1B",
            facecolor="#FF9848",
        )
        self.canvas.draw()

    def btnChecked(self):
        for i in range(len(self.blm_buttons)):
            if self.blm_buttons[i].isChecked():
                self.btnsChecked[i] = True
            else:
                self.btnsChecked[i] = False

    def clear_all_buttons(self):
        self.fig.clear()
        self.canvas.draw()

        for i in self.all_blm_buttons:
            i.setChecked(False)
        self.SUM.setChecked(False)
        self.SUM_MINUS_R1_R2.setChecked(False)
        self.R5IM.setChecked(False)

    def set_R0(self):
        """
        When the R0 buttons is pressed update its BLMs
        """
        state = self.R0.isChecked()
        for i in self.R0_blm_buttons:
            i.setChecked(state)

    def set_R1(self):
        """
        When the R1 buttons is pressed update its BLMs
        """
        state = self.R1.isChecked()
        for i in self.R1_blm_buttons:
            i.setChecked(state)

    def set_R2(self):
        """
        When the R2 buttons is pressed update its BLMs
        """
        state = self.R2.isChecked()
        for i in self.R2_blm_buttons:
            i.setChecked(state)

    def set_R3(self):
        """
        When the R3 buttons is pressed update its BLMs
        """
        state = self.R3.isChecked()
        for i in self.R3_blm_buttons:
            i.setChecked(state)

    def set_R4(self):
        """
        When the R4 buttons is pressed update its BLMs
        """
        state = self.R4.isChecked()
        for i in self.R4_blm_buttons:
            i.setChecked(state)

    def set_R5(self):
        """
        When the R5 buttons is pressed update its BLMs
        """
        state = self.R5.isChecked()
        for i in self.R5_blm_buttons:
            i.setChecked(state)

    def set_R6(self):
        """
        When the R6 buttons is pressed update its BLMs
        """
        state = self.R6.isChecked()
        for i in self.R6_blm_buttons:
            i.setChecked(state)

    def set_R7(self):
        """
        When the R7 buttons is pressed update its BLMs
        """
        state = self.R7.isChecked()
        for i in self.R7_blm_buttons:
            i.setChecked(state)

    def set_R8(self):
        """
        When the R8 buttons is pressed update its BLMs
        """
        state = self.R8.isChecked()
        for i in self.R8_blm_buttons:
            i.setChecked(state)

    def set_R9(self):
        """
        When the R9 buttons is pressed update its BLMs
        """
        state = self.R9.isChecked()
        for i in self.R9_blm_buttons:
            i.setChecked(state)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
