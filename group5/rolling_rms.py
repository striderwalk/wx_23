import numpy as np
import matplotlib as plt
import os
import glob
import pandas as pd

os.chdir("C:\\Users\\zhl58523\\Documents")
files = glob.glob("BLM_R5IM_Data/cycle" + "/*.csv")
selected_file = files[0]
input_data = pd.read_csv(selected_file)
dataframe = input_data.drop(columns=input_data.columns[0]).to_numpy()
x = 1
arr = []
n = len(arr)
# for i in range(0, 2200):#no for loop - integrates into mqtt on message function
#     if len(arr) > 5:
#         arr.pop([0])

#     if len(arr) < 5:
#             arr.append() #append data from file

#     if len(arr) == 5:

#         for i in (dataframe[1:38]):
#             for g in (i):
#                 arr.append(g)
#                 rms = np.std(arr)

#             print(n)
#             plt.scatter(x,rmsValue(arr,n))

arr = []


def rms(y):
    global arr

    arr.append(y)
    if len(arr) < 5:
        return
    # compute it here
    n = len(arr)
    # print(n)
    compute = np.std(arr, axis=0)
    arr.pop(0)
    # return it here
    print(compute)
    # return compute


for i in range(1000):
    rms(i)
