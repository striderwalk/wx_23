import glob
import pandas as pd
import random
import paho.mqtt.client as mqtt
import string
import time

files = glob.glob("pandas_26_05_2023" + '/*.csv')

def generate_dummy_data():
    random_file = random.randint(0, (len(files)-1))
    file = files[random_file]
    next = pd.read_csv(file)
    dataframe = next.drop(columns = next.columns[0]).to_numpy()
    return dataframe

def generate_shortuuid() -> str:
    """Public function for generating short UUID messages"""
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    shortuiid = "".join(random.choices(alphabet, k=12))
    return shortuiid

# def publish_dummy_data(frequency):
#     publish_client = mqtt.Client(client_id="accphys-workxp"+ generate_shortuuid())
#     publish_client.connect("mqtt.isis.rl.ac.uk", 1883, 60)
#     publish_client.loop_start()
#     while True:
#         publish_client.publish("acc_phys_workxp_data", generate_dummy_data().tobytes(order='C'))
#         period = 1/frequency
#         time.sleep(period)

def publish_dummy_data(frequency):
    publish_client = mqtt.Client(client_id="accphys-workxp"+ generate_shortuuid())
    publish_client.connect("130.246.57.45", 8883, 60)
    publish_client.loop_start()
    while True:
        publish_client.publish("ac_phys/workxp/live_signals", generate_dummy_data().tobytes(order='C'))
        period = 1/frequency
        time.sleep(period)

publish_dummy_data(1)