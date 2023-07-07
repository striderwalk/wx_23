import glob
import pandas as pd
#import random
#import paho.mqtt.client as mqtt
import string
import time
import matplotlib.pyplot as plt
import numpy as np
def dataframe():
    files = glob.glob('../BLM_R5IM_Data/cycle' + '/*.csv')
    selected_file = files[0]
    global x_data
    x_data = np.linspace(-0.5, 10.5, 2200)
    #use x_data as x-coordinate when performing calculations
    input_data = pd.read_csv(selected_file)
    dataframe = input_data.drop(columns = input_data.columns[0]).to_numpy()
    #eg. datagrame[39] calls BL value of BLM39 
    return dataframe

    