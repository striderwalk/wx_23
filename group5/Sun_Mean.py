import glob
import pandas as pd

# import random
# import paho.mqtt.client as mqtt
import string
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
import os

os.chdir("C:\\Users\\zhl58523\\Documents")
files = glob.glob("BLM_R5IM_Data/cycle" + "/*.csv")
selected_file = files[0]
input_data = pd.read_csv(selected_file)
array = input_data.drop(columns=input_data.columns[0]).to_numpy()


class statsClass:
    def __init__(self, array):
        self.array = array

    def sumOfNumbers(self, signal):
        return sum(array[signal])

    def meanOfNumbers(self, signal):
        return statistics.mean(array[signal])

    def time(
        self, times, startTime, endTime, dataPoints
    ):  # finds the relative position of a time in the 2200 data points
        return list(
            map(
                lambda t: (
                    round(((t - startTime) / (endTime - startTime)) * dataPoints)
                ),
                times,
            )
        )  # Lambda is a keyword that allows you to define a function in one line and use immediately.
        # map excecutes a specified function in a list without an explicit loop.

    def pairs(
        self, listOfTimes
    ):  # pairs time boundaries together eg. -0.5 to 3.0, 3.0 to 4.5
        return list(
            zip(listOfTimes, listOfTimes[1:])
        )  # zip returns an iterator of tuples, with two items paired together in each

    def sumWithTimes(
        self, signal, pairsList
    ):  # sum of data points between specified boundaries
        return (sum(array[signal][start:end]) for start, end in pairsList)

    def meanWithTimes(
        self, signal, pairsList
    ):  # mean of data points between specified boundaries
        return [statistics.mean(array[signal][start:end]) for start, end in pairsList]

    def cumulativeWithTimes(self, time, prevTotal, counter, data, x, y, i):
        i += 1
        if (y + 1) <= len(time):
            # if (index[x]-startTime)/(*dataPerSec <= i <= (index[y]-startTime)*dataPerSec:
            if time[x] <= i <= time[y]:
                counter += 1
                total = prevTotal + data

                if time[y] == i:
                    # allIndexTotals.append(indexTotal)
                    x = y
                    y += 1
                    # counter = 0

                    return [total, total / counter, 0, x, y, i]
                # print("cumulative total", total, "\ncumulative mean", total/counter)
                return [total, total / counter, counter, x, y, i]
        return [0, 0, 0, 0, i]
        # print("hello")

    def cumulateNTimes(self, nList, currentData):
        nList.append(currentData)
        nList.pop(0)
        return nList


stats = statsClass(array)
timebound1 = 1  # milliseconds included within stat.time
timebound2 = 2  # milliseconds included within stat.time

min_interval = -0.5
max_interval = 10.5

datapoints = 2200


# mean of signals within two timebounds - timebounds are in milliseconds
def mean(timebound1, timebound2):
    meanBoundaries = stats.meanWithTimes(
        2,
        (
            stats.pairs(
                stats.time(
                    [timebound1, timebound2], min_interval, max_interval, datapoints
                )
            )
        ),
    )
    print(meanBoundaries)


# sum of signals in two timebounds
def sum():
    sumBoundaries = stats.sumWithTimes(
        2,
        (
            stats.pairs(
                stats.time(
                    [timebound1, timebound2], min_interval, max_interval, datapoints
                )
            )
        ),
    )
    print(sumBoundaries)


sum()
