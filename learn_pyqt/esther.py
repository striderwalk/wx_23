import sys
import numpy as np
import multiprocessing
import paho.mqtt.client as mqtt
from PyQt5 import QtGui
from PyQt5.QtGui import * 
import PyQt5.QtWidgets as qt
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import json
import matplotlib.patches as mpatches
from PyQt5 import QtCore, QtGui, QtWidgets
import math 

class gui(qt.QWidget):
    def __init__(self, data_queue):
        super().__init__()
        self.data_queue = data_queue
        self.MyUi()

        def on_connect(client, userdata, flags, rc):
            # Subscribes to the user input inside the input_mqtt_topic
            topic_list = self.input_mqtt_topic.currentText()
            print("Connected to topic: "+str(topic_list))
            client.subscribe(topic_list)

            # if button_connect is clicked 
            # self.button_connect.clicked.disconnect()
            # self.button_connect.clicked.connect(self.disconnect)
            # self.button_connect.setText("Disconnect")

            # self.input_mqttport.setEnabled(False)
            # self.input_mqttserver.setEnabled(False)
            # self.input_mqtt_topic.setEnabled(False)


        def on_message(client, userdata, msg):
            msg_byte = msg.payload
            msg_array = np.frombuffer(msg_byte, dtype=float, count=-1, offset=0)
            msg_full = np.reshape(msg_array, (40, 2200))
            # when we receive a message (on_message), we run the update_plot function, 
            # which plots the data as soon as it receives a message.
            self.update_plot(np.array(msg_full))
            

        def on_disconnect(client, userdata, rc):
            if rc != 0:
                print("Unexpected disconnection")
            else:
                print("Disconnected")

            self.button_connect.clicked.disconnect()
            # self.button_connect.clicked.connect(self.connect)
            # self.button_connect.setText("Connect")

            # self.input_mqttport.setEnabled(True)
            # self.input_mqttserver.setEnabled(True)
            self.input_mqtt_topic.setEnabled(True)


        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_disconnect = on_disconnect
        self.button_connect.clicked.connect(self.connect)

    def MyUi(self):
        '''
        Method to create the main GUI elements including the matplotlib graph
        and input settings.
        '''
        # The main layout is a QHbox
        hbox = qt.QHBoxLayout()
        #hbox.addStretch(1)
        self.setFixedWidth(1350)
        self.setFixedHeight(750)

        # Make an initially blank matplotlib canvas and axis
        chart_vbox = qt.QVBoxLayout()
        self.fig = Figure(figsize = [9, 3])
        self.static_canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.static_canvas, self)

        # Buttons
        self.widget = qt.QWidget()
        buttons = qt.QVBoxLayout()
        # self.input_mqttserver = qt.QLineEdit()
        # self.input_mqttserver.setPlaceholderText("Start Time")

        # self.input_mqttport = qt.QLineEdit()
        # self.input_mqttport.setPlaceholderText("End Time")

        self.input_mqtt_topic = qt.QComboBox()
        self.input_mqtt_topic.addItems(["ac_phys/workxp/live_signals", "ac_phys/workxp/standard", "ac_phys/workxp/test_signals"])
        self.button_connect = qt.QPushButton("Connect")

        # self.button_save = qt.QPushButton("Save Chart Data")
        # self.button_clear = qt.QPushButton("Clear Chart")

        # buttons.addWidget(self.input_mqttserver)
        # buttons.addWidget(self.input_mqttport)
        buttons.addWidget(self.input_mqtt_topic)
        buttons.addWidget(self.button_connect)
        # buttons.addWidget(self.button_save)
        # buttons.addWidget(self.button_clear)


        self.scrollArea = qt.QScrollArea()
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 431, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(50)
        self.checkBox_50 = qt.QCheckBox("R0", self.scrollAreaWidgetContents)
        self.checkBox_50.setGeometry(QtCore.QRect(50, 20, 43, 20))
        self.checkBox_50.setObjectName("checkBox_50")
        self.checkBox_50.setFont(font)
        self.checkBox_54 = QtWidgets.QCheckBox("R1", self.scrollAreaWidgetContents)
        self.checkBox_54.setGeometry(QtCore.QRect(150, 20, 43, 20))
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_54.setFont(font)
        self.checkBox_55 = QtWidgets.QCheckBox("R9", self.scrollAreaWidgetContents)
        self.checkBox_55.setGeometry(QtCore.QRect(150, 340, 43, 20))
        self.checkBox_55.setObjectName("checkBox_55")
        self.checkBox_55.setFont(font)
        self.checkBox_56 = QtWidgets.QCheckBox("R8", self.scrollAreaWidgetContents)
        self.checkBox_56.setGeometry(QtCore.QRect(50, 340, 43, 20))
        self.checkBox_56.setObjectName("checkBox_56")
        self.checkBox_56.setFont(font)
        self.checkBox_57 = QtWidgets.QCheckBox("R2", self.scrollAreaWidgetContents)
        self.checkBox_57.setGeometry(QtCore.QRect(250, 20, 43, 20))
        self.checkBox_57.setObjectName("checkBox_57")
        self.checkBox_57.setFont(font)
        self.checkBox_58 = QtWidgets.QCheckBox("R3", self.scrollAreaWidgetContents)
        self.checkBox_58.setGeometry(QtCore.QRect(350, 20, 43, 20))
        self.checkBox_58.setObjectName("checkBox_58")
        self.checkBox_58.setFont(font)
        self.checkBox_59 = QtWidgets.QCheckBox("R5", self.scrollAreaWidgetContents)
        self.checkBox_59.setGeometry(QtCore.QRect(150, 170, 43, 20))
        self.checkBox_59.setObjectName("checkBox_59")
        self.checkBox_59.setFont(font)
        self.checkBox_60 = QtWidgets.QCheckBox("R4", self.scrollAreaWidgetContents)
        self.checkBox_60.setGeometry(QtCore.QRect(50, 170, 43, 20))
        self.checkBox_60.setObjectName("checkBox_60")
        self.checkBox_60.setFont(font)
        self.checkBox_61 = QtWidgets.QCheckBox("R7", self.scrollAreaWidgetContents)
        self.checkBox_61.setGeometry(QtCore.QRect(350, 170, 43, 20))
        self.checkBox_61.setObjectName("checkBox_61")
        self.checkBox_61.setFont(font)
        self.checkBox_62 = QtWidgets.QCheckBox("R6", self.scrollAreaWidgetContents)
        self.checkBox_62.setGeometry(QtCore.QRect(250, 170, 43, 20))
        self.checkBox_62.setObjectName("checkBox_62")
        self.checkBox_62.setFont(font)
        self.checkBox_63 = QtWidgets.QCheckBox("R5IM", self.scrollAreaWidgetContents)
        self.checkBox_63.setGeometry(QtCore.QRect(250, 440, 81, 20))
        self.checkBox_63.setObjectName("checkBox_63")
        self.checkBox_63.setFont(font)
        self.checkBox_64 = QtWidgets.QCheckBox("SUM", self.scrollAreaWidgetContents)
        self.checkBox_64.setGeometry(QtCore.QRect(250, 400, 111, 20))
        self.checkBox_64.setFont(font)
        self.checkBox_64.setObjectName("checkBox_64")
        self.checkBox_65 = QtWidgets.QCheckBox("SUM - R1  - R2", self.scrollAreaWidgetContents)
        self.checkBox_65.setGeometry(QtCore.QRect(250, 360, 131, 20))
        self.checkBox_65.setObjectName("checkBox_65")
        self.checkBox_65.setFont(font)
        self.groupBox_11 = QtWidgets.QGroupBox("R1", self.scrollAreaWidgetContents)
        self.groupBox_11.setGeometry(QtCore.QRect(120, 40, 91, 111))
        self.groupBox_11.setObjectName("groupBox_11")
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setWeight(50)
        self.checkBox_66 = QtWidgets.QCheckBox("r1blm1", self.groupBox_11)
        self.checkBox_66.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_66.setFont(font)
        self.checkBox_66.setObjectName("checkBox_66")
        self.checkBox_67 = QtWidgets.QCheckBox("r1blm2", self.groupBox_11)
        self.checkBox_67.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_67.setObjectName("checkBox_67")
        self.checkBox_67.setFont(font)
        self.checkBox_68 = QtWidgets.QCheckBox("r1blm3", self.groupBox_11)
        self.checkBox_68.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_68.setObjectName("checkBox_68")
        self.checkBox_68.setFont(font)
        self.checkBox_69 = QtWidgets.QCheckBox("r1blm4", self.groupBox_11)
        self.checkBox_69.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_69.setObjectName("checkBox_69")
        self.checkBox_69.setFont(font)
        self.groupBox_12 = QtWidgets.QGroupBox("R2", self.scrollAreaWidgetContents)
        self.groupBox_12.setGeometry(QtCore.QRect(220, 40, 91, 111))
        self.groupBox_12.setObjectName("groupBox_12")
        self.checkBox_70 = QtWidgets.QCheckBox("r2blm2", self.groupBox_12)
        self.checkBox_70.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_70.setObjectName("checkBox_70")
        self.checkBox_70.setFont(font)
        self.checkBox_71 = QtWidgets.QCheckBox("r2blm1", self.groupBox_12)
        self.checkBox_71.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_71.setFont(font)
        self.checkBox_71.setObjectName("checkBox_71")
        self.checkBox_72 = QtWidgets.QCheckBox("r2blm3", self.groupBox_12)
        self.checkBox_72.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_72.setObjectName("checkBox_72")
        self.checkBox_72.setFont(font)
        self.checkBox_73 = QtWidgets.QCheckBox("r2blm4", self.groupBox_12)
        self.checkBox_73.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_73.setObjectName("checkBox_73")
        self.checkBox_73.setFont(font)

        self.groupBox_13 = QtWidgets.QGroupBox("R3", self.scrollAreaWidgetContents)
        self.groupBox_13.setGeometry(QtCore.QRect(320, 40, 91, 111))
        self.groupBox_13.setObjectName("groupBox_13")
        self.checkBox_74 = QtWidgets.QCheckBox("r3blm4", self.groupBox_13)
        self.checkBox_74.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_74.setObjectName("checkBox_74")
        self.checkBox_74.setFont(font)
        self.checkBox_75 = QtWidgets.QCheckBox("r3blm2", self.groupBox_13)
        self.checkBox_75.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_75.setObjectName("checkBox_75")
        self.checkBox_75.setFont(font)
        self.checkBox_76 = QtWidgets.QCheckBox("r3blm3", self.groupBox_13)
        self.checkBox_76.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_76.setObjectName("checkBox_76")
        self.checkBox_76.setFont(font)
        self.checkBox_77 = QtWidgets.QCheckBox("r3blm1", self.groupBox_13)
        self.checkBox_77.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_77.setFont(font)
        self.checkBox_77.setObjectName("checkBox_77")

        self.groupBox_14 = QtWidgets.QGroupBox("R4", self.scrollAreaWidgetContents)
        self.groupBox_14.setGeometry(QtCore.QRect(20, 210, 91, 111))
        self.groupBox_14.setObjectName("groupBox_14")
        self.checkBox_78 = QtWidgets.QCheckBox("r4blm4", self.groupBox_14)
        self.checkBox_78.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_78.setFont(font)
        self.checkBox_78.setObjectName("checkBox_78")
        self.checkBox_79 = QtWidgets.QCheckBox("r4blm1", self.groupBox_14)
        self.checkBox_79.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_79.setFont(font)
        self.checkBox_79.setObjectName("checkBox_79")
        self.checkBox_80 = QtWidgets.QCheckBox("r4blm2", self.groupBox_14)
        self.checkBox_80.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_80.setFont(font)
        self.checkBox_80.setObjectName("checkBox_80")
        self.checkBox_81 = QtWidgets.QCheckBox("r4blm3", self.groupBox_14)
        self.checkBox_81.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_81.setFont(font)
        self.checkBox_81.setObjectName("checkBox_81")

        self.groupBox_15 = QtWidgets.QGroupBox("R5", self.scrollAreaWidgetContents)
        self.groupBox_15.setGeometry(QtCore.QRect(120, 210, 91, 111))
        self.groupBox_15.setObjectName("groupBox_15")
        self.checkBox_82 = QtWidgets.QCheckBox("r5blm4", self.groupBox_15)
        self.checkBox_82.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_82.setObjectName("checkBox_82")
        self.checkBox_82.setFont(font)
        self.checkBox_83 = QtWidgets.QCheckBox("r5blm2", self.groupBox_15)
        self.checkBox_83.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_83.setObjectName("checkBox_83")
        self.checkBox_83.setFont(font)
        self.checkBox_84 = QtWidgets.QCheckBox("r5blm1", self.groupBox_15)
        self.checkBox_84.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_84.setFont(font)
        self.checkBox_84.setObjectName("checkBox_84")
        self.checkBox_85 = QtWidgets.QCheckBox("r5blm3", self.groupBox_15)
        self.checkBox_85.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_85.setObjectName("checkBox_85")
        self.checkBox_85.setFont(font)

        self.groupBox_16 = QtWidgets.QGroupBox("R6", self.scrollAreaWidgetContents)
        self.groupBox_16.setGeometry(QtCore.QRect(220, 210, 91, 111))
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.checkBox_86 = QtWidgets.QCheckBox("r6blm4", self.groupBox_16)
        self.checkBox_86.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_86.setFont(font)
        self.checkBox_86.setObjectName("checkBox_86")
        self.checkBox_87 = QtWidgets.QCheckBox("r6blm2", self.groupBox_16)
        self.checkBox_87.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_87.setFont(font)
        self.checkBox_87.setObjectName("checkBox_87")
        self.checkBox_88 = QtWidgets.QCheckBox("r6blm1", self.groupBox_16)
        self.checkBox_88.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_88.setFont(font)
        self.checkBox_88.setObjectName("checkBox_88")
        self.checkBox_89 = QtWidgets.QCheckBox("r6blm3", self.groupBox_16)
        self.checkBox_89.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_89.setFont(font)
        self.checkBox_89.setObjectName("checkBox_89")

        self.groupBox_17 = QtWidgets.QGroupBox("R7", self.scrollAreaWidgetContents)
        self.groupBox_17.setGeometry(QtCore.QRect(320, 210, 91, 111))
        self.groupBox_17.setFont(font)
        self.groupBox_17.setObjectName("groupBox_17")
        self.checkBox_90 = QtWidgets.QCheckBox("r7blm4", self.groupBox_17)
        self.checkBox_90.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_90.setFont(font)
        self.checkBox_90.setObjectName("checkBox_90")
        self.checkBox_91 = QtWidgets.QCheckBox("r7blm1", self.groupBox_17)
        self.checkBox_91.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_91.setFont(font)
        self.checkBox_91.setObjectName("checkBox_91")
        self.checkBox_92 = QtWidgets.QCheckBox("r7blm2", self.groupBox_17)
        self.checkBox_92.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_92.setFont(font)
        self.checkBox_92.setObjectName("checkBox_92")
        self.checkBox_93 = QtWidgets.QCheckBox("r7blm3", self.groupBox_17)
        self.checkBox_93.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_93.setFont(font)
        self.checkBox_93.setObjectName("checkBox_93")

        self.groupBox_18 = QtWidgets.QGroupBox("R8", self.scrollAreaWidgetContents)
        self.groupBox_18.setGeometry(QtCore.QRect(20, 370, 91, 111))
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.checkBox_94 = QtWidgets.QCheckBox("r8blm4", self.groupBox_18)
        self.checkBox_94.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_94.setFont(font)
        self.checkBox_94.setObjectName("checkBox_94")
        self.checkBox_95 = QtWidgets.QCheckBox("r8blm3", self.groupBox_18)
        self.checkBox_95.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_95.setFont(font)
        self.checkBox_95.setObjectName("checkBox_95")
        self.checkBox_96 = QtWidgets.QCheckBox("r8blm2", self.groupBox_18)
        self.checkBox_96.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_96.setFont(font)
        self.checkBox_96.setObjectName("checkBox_96")
        self.checkBox_97 = QtWidgets.QCheckBox("r8blm1", self.groupBox_18)
        self.checkBox_97.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_97.setFont(font)
        self.checkBox_97.setObjectName("checkBox_97")

        self.groupBox_19 = QtWidgets.QGroupBox("R9", self.scrollAreaWidgetContents)
        self.groupBox_19.setGeometry(QtCore.QRect(120, 370, 91, 111))
        self.groupBox_19.setFont(font)
        self.groupBox_19.setObjectName("groupBox_19")
        self.checkBox_98 = QtWidgets.QCheckBox("r9blm4", self.groupBox_19)
        self.checkBox_98.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_98.setFont(font)
        self.checkBox_98.setObjectName("checkBox_98")
        self.checkBox_99 = QtWidgets.QCheckBox("r9blm3", self.groupBox_19)
        self.checkBox_99.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.checkBox_99.setFont(font)
        self.checkBox_99.setObjectName("checkBox_99")
        self.checkBox_100 = QtWidgets.QCheckBox("r9blm1", self.groupBox_19)
        self.checkBox_100.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_100.setFont(font)
        self.checkBox_100.setObjectName("checkBox_100")
        self.checkBox_101 = QtWidgets.QCheckBox("r9blm2", self.groupBox_19)
        self.checkBox_101.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.checkBox_101.setFont(font)
        self.checkBox_101.setObjectName("checkBox_101")

        self.groupBox_20 = QtWidgets.QGroupBox("R0", self.scrollAreaWidgetContents)
        self.groupBox_20.setGeometry(QtCore.QRect(20, 40, 91, 111))
        self.groupBox_20.setObjectName("groupBox_20")
        self.checkBox_102 = QtWidgets.QCheckBox("r0blm4", self.groupBox_20)
        self.checkBox_102.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.checkBox_102.setObjectName("checkBox_102")
        self.checkBox_102.setFont(font)
        self.checkBox_103 = QtWidgets.QCheckBox("r0blm1", self.groupBox_20)
        self.checkBox_103.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.checkBox_103.setFont(font)
        self.checkBox_103.setObjectName("checkBox_103")
        self.checkBox_104 = QtWidgets.QCheckBox("r0blm3", self.groupBox_20)
        self.checkBox_104.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.checkBox_104.setObjectName("checkBox_104")
        self.checkBox_104.setFont(font)
        self.button_clear_all = qt.QPushButton("Clear Selected", self.scrollAreaWidgetContents)
        self.button_clear_all.setGeometry(QtCore.QRect(250, 480, 120, 30))
        # self.LCDNumber = QtWidgets.QLCDNumber(99, self.scrollAreaWidgetContents)
        # self.LCDNumber.setGeometry(QtCore.QRect(20, 500, 100, 25))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        # Add the widgets to chart layout
        chart_vbox.addWidget(self.static_canvas)
        chart_vbox.addWidget(self.toolbar)

        # Add the layouts to the main layout
        hbox.addLayout(chart_vbox)
        hbox.addLayout(buttons)
        buttons.addWidget(self.scrollArea)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 600, 350)
        self.setWindowTitle("MQTT Plotter")
        self.show()

    def plot_blm(self, data, i):
        self.ax.plot(np.linspace(-0.3, 10.57, num=2200, endpoint=True), data[i])

    def connect(self):
        '''
        Connections to the broker
        '''
        self.client.connect("130.246.57.45", 8883, 60)
        self.client.loop_start()


    def disconnect(self):
        self.client.loop_stop()
        self.client.unsubscribe(self.input_mqtt_topic.text())
        self.client.disconnect()

    def clear_all(self):
        self.checkBox_50.setChecked(False)
        self.checkBox_54.setChecked(False)
        self.checkBox_55.setChecked(False)
        self.checkBox_56.setChecked(False)
        self.checkBox_57.setChecked(False)
        self.checkBox_58.setChecked(False)
        self.checkBox_59.setChecked(False)
        self.checkBox_60.setChecked(False)
        self.checkBox_61.setChecked(False)
        self.checkBox_62.setChecked(False)
        self.checkBox_63.setChecked(False)
        self.checkBox_64.setChecked(False)
        self.checkBox_65.setChecked(False)
        self.checkBox_66.setChecked(False)
        self.checkBox_67.setChecked(False)
        self.checkBox_68.setChecked(False)
        self.checkBox_69.setChecked(False)
        self.checkBox_70.setChecked(False)
        self.checkBox_71.setChecked(False)
        self.checkBox_72.setChecked(False)
        self.checkBox_73.setChecked(False)
        self.checkBox_74.setChecked(False)
        self.checkBox_75.setChecked(False)
        self.checkBox_76.setChecked(False)
        self.checkBox_77.setChecked(False)
        self.checkBox_78.setChecked(False)
        self.checkBox_79.setChecked(False)
        self.checkBox_80.setChecked(False)
        self.checkBox_81.setChecked(False)
        self.checkBox_82.setChecked(False)
        self.checkBox_83.setChecked(False)
        self.checkBox_84.setChecked(False)
        self.checkBox_85.setChecked(False)
        self.checkBox_86.setChecked(False)
        self.checkBox_87.setChecked(False)
        self.checkBox_88.setChecked(False)
        self.checkBox_89.setChecked(False)
        self.checkBox_90.setChecked(False)
        self.checkBox_91.setChecked(False)
        self.checkBox_92.setChecked(False)
        self.checkBox_93.setChecked(False)
        self.checkBox_94.setChecked(False)
        self.checkBox_95.setChecked(False)
        self.checkBox_96.setChecked(False)
        self.checkBox_97.setChecked(False)
        self.checkBox_98.setChecked(False)
        self.checkBox_99.setChecked(False)
        self.checkBox_100.setChecked(False)
        self.checkBox_101.setChecked(False)
        self.checkBox_102.setChecked(False)
        self.checkBox_103.setChecked(False)
        self.checkBox_104.setChecked(False)

    def update_plot(self, data):
        self.fig.clear()
        self.fig.subplots_adjust(top=0.925, bottom=0.13, left=0.085, right=0.95)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Live Plot of BLM Waveforms updated per second', fontsize=16)
        self.ax.set_xlabel('Time (s)', fontsize = 14)
        self.ax.set_ylabel('Voltage (V)', fontsize = 14)
        self.ax.grid(color = "dimgray")
        # self.ax.set_facecolor("black")
        # self.ax.set_xlim([-0.4, 10.7])
        self.ax.set_ylim([-0.15, 0.6])
        #np.save('data_backup', self.data)
        #self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), data[i])
        check_on = [0] * 40
        if self.checkBox_103.isChecked() == True:
            self.ax.set_ylim([-5.2, 0.4])
        if self.checkBox_63.isChecked() == True:
            self.ax.set_ylim([-0.2, 4.0])

        #r0
        if self.checkBox_50.isChecked() == True:
            self.checkBox_103.setChecked(True)
            self.checkBox_104.setChecked(True)
            self.checkBox_102.setChecked(True)
        #r1
        if self.checkBox_54.isChecked() == True:
            self.checkBox_66.setChecked(True)
            self.checkBox_67.setChecked(True)
            self.checkBox_68.setChecked(True)
            self.checkBox_69.setChecked(True)
        #r2
        if self.checkBox_57.isChecked() == True:
            self.checkBox_70.setChecked(True)
            self.checkBox_71.setChecked(True)
            self.checkBox_72.setChecked(True)
            self.checkBox_73.setChecked(True)
        #r3
        if self.checkBox_58.isChecked() == True:
            self.checkBox_74.setChecked(True)
            self.checkBox_75.setChecked(True)
            self.checkBox_76.setChecked(True)
            self.checkBox_77.setChecked(True)
        #r4
        if self.checkBox_60.isChecked() == True:
            self.checkBox_78.setChecked(True)
            self.checkBox_79.setChecked(True)
            self.checkBox_80.setChecked(True)
            self.checkBox_81.setChecked(True)
        #r5
        if self.checkBox_59.isChecked() == True:
            self.checkBox_82.setChecked(True)
            self.checkBox_83.setChecked(True)
            self.checkBox_84.setChecked(True)
            self.checkBox_85.setChecked(True)
        #r6
        if self.checkBox_62.isChecked() == True:
            self.checkBox_86.setChecked(True)
            self.checkBox_87.setChecked(True)
            self.checkBox_88.setChecked(True)
            self.checkBox_89.setChecked(True)
        #r7
        if self.checkBox_61.isChecked() == True:
            self.checkBox_90.setChecked(True)
            self.checkBox_91.setChecked(True)
            self.checkBox_92.setChecked(True)
            self.checkBox_93.setChecked(True)
        #r8
        if self.checkBox_56.isChecked() == True:
            self.checkBox_94.setChecked(True)
            self.checkBox_95.setChecked(True)
            self.checkBox_96.setChecked(True)
            self.checkBox_97.setChecked(True)
        #r9
        if self.checkBox_55.isChecked() == True:
            self.checkBox_98.setChecked(True)
            self.checkBox_99.setChecked(True)
            self.checkBox_100.setChecked(True)
            self.checkBox_101.setChecked(True)
        if self.checkBox_103.isChecked() == True:
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[0])), c = 'blue', ls='-')
        if self.checkBox_104.isChecked() == True:
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[1])), c = 'blue', ls='-.')
        if self.checkBox_102.isChecked() == True:
            check_on[2] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[2])), c = 'blue', ls=':')
        if self.checkBox_66.isChecked() == True:
            check_on[3] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[3])), c = 'darkviolet', ls='-')
        if self.checkBox_67.isChecked() == True:
            check_on[4] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[4])), c = 'darkviolet', ls='--')
        if self.checkBox_68.isChecked() == True:
            check_on[5] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[5])), c = 'darkviolet', ls='-.')
        if self.checkBox_69.isChecked() == True:
            check_on[6] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[6])), c = 'darkviolet', ls=':')
        if self.checkBox_71.isChecked() == True:
            check_on[7] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[7])), c = 'deeppink', ls='-')
        if self.checkBox_70.isChecked() == True:
            check_on[8] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[8])), c = 'deeppink', ls='--')
        if self.checkBox_72.isChecked() == True:
            check_on[9] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[9])), c = 'deeppink', ls='-.')
        if self.checkBox_73.isChecked() == True:
            check_on[10] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[10])), c = 'deeppink', ls=':')
        if self.checkBox_77.isChecked() == True:
            check_on[11] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[11])), c = 'crimson', ls='-')
        if self.checkBox_75.isChecked() == True:
            check_on[12] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[12])), c = 'crimson', ls='--')
        if self.checkBox_76.isChecked() == True:
            check_on[13] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[13])), c = 'crimson', ls='-.')
        if self.checkBox_74.isChecked() == True:
            check_on[14] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[14])), c = 'crimson', ls=':')
        if self.checkBox_79.isChecked() == True:
            check_on[15] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[15])), c = 'coral', ls='-')
        if self.checkBox_80.isChecked() == True:
            check_on[16] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[16])), c = 'coral', ls='--')
        if self.checkBox_81.isChecked() == True:
            check_on[17] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[17])), c = 'coral', ls='-.')
        if self.checkBox_78.isChecked() == True:
            check_on[18] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[18])), c = 'coral', ls=':')
        if self.checkBox_84.isChecked() == True:
            check_on[19] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[19])), c = 'gold', ls='-')
        if self.checkBox_83.isChecked() == True:
            check_on[20] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[20])), c = 'gold', ls='--')
        if self.checkBox_85.isChecked() == True:
            check_on[21] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[21])), c = 'gold', ls='-.')
        if self.checkBox_82.isChecked() == True:
            check_on[22] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[22])), c = 'gold', ls=':')
        if self.checkBox_88.isChecked() == True:
            check_on[23] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[23])), c = 'lime', ls='-')
        if self.checkBox_87.isChecked() == True:
            check_on[24] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[24])), c = 'lime', ls='--')
        if self.checkBox_89.isChecked() == True:
            check_on[25] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[25])), c = 'lime', ls='-.')
        if self.checkBox_86.isChecked() == True:
            check_on[26] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[26])), c = 'lime', ls=':')
        if self.checkBox_91.isChecked() == True:
            check_on[27] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[27])), c = 'forestgreen', ls='-')
        if self.checkBox_92.isChecked() == True:
            check_on[28] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[28])), c = 'forestgreen', ls='--')
        if self.checkBox_93.isChecked() == True:
            check_on[29] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[29])), c = 'forestgreen', ls='-.')
        if self.checkBox_90.isChecked() == True:
            check_on[30] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[30])), c = 'forestgreen', ls=':')
        if self.checkBox_97.isChecked() == True:
            check_on[31] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[31])), c = 'turquoise', ls='-')
        if self.checkBox_96.isChecked() == True:
            check_on[32] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[32])), c = 'turquoise', ls='--')
        if self.checkBox_95.isChecked() == True:
            check_on[33] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[33])), c = 'turquoise', ls='-.')
        if self.checkBox_94.isChecked() == True:
            check_on[34] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[34])), c = 'turquoise', ls=':')
        if self.checkBox_100.isChecked() == True:
            check_on[35] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[35])), c = 'cornflowerblue', ls='-')
        if self.checkBox_101.isChecked() == True:
            check_on[36] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[36])), c = 'cornflowerblue', ls='--')
        if self.checkBox_99.isChecked() == True:
            check_on[37] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[37])), c = 'cornflowerblue', ls='-.')
        if self.checkBox_98.isChecked() == True:
            check_on[38] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[38])), c = 'cornflowerblue', ls=':')
        if self.checkBox_63.isChecked() == True:
            check_on[39] = 1
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), ((data[39])), c = 'navy')
        if self.checkBox_64.isChecked() == True:
            tot_sum = np.sum((data), axis = 0)
            blm_sum = tot_sum - (data[0]) - (data[39])
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), blm_sum, c = 'black')
        if self.checkBox_65.isChecked() == True:
            tot_sum = (np.sum((data), axis = 0))
            blm_sum2 = tot_sum - ((data[39])) - (data[0]) - (data[1]) - (data[2]) - (data[3]) - (data[4]) - (data[5]) - (data[6])
            self.ax.plot(np.linspace(-0.5, 10.5, num=2200, endpoint=True), blm_sum2, c = 'gray')
        if (1 in check_on):
            pass
        else:
            self.button_clear_all.clicked.connect(self.clear_all)

        r0_patch = mpatches.Patch(color='blue', label='R0')
        r1_patch = mpatches.Patch(color='darkviolet', label='R1')
        r2_patch = mpatches.Patch(color='deeppink', label='R2')
        r3_patch = mpatches.Patch(color='crimson', label='R3')
        r4_patch = mpatches.Patch(color='coral', label='R4')
        r5_patch = mpatches.Patch(color='gold', label='R5')
        r6_patch = mpatches.Patch(color='lime', label='R6')
        r7_patch = mpatches.Patch(color='forestgreen', label='R7')
        r8_patch = mpatches.Patch(color='turquoise', label='R8')
        r9_patch = mpatches.Patch(color='cornflowerblue', label='R9')
        im_patch = mpatches.Patch(color='navy', label='R5IM')
        sum_patch = mpatches.Patch(color='black', label='SUM')
        sum2_patch = mpatches.Patch(color='gray', label='SUM-R1-R2')
        self.ax.legend(handles=[r0_patch, r1_patch, r2_patch, r3_patch, r4_patch, r5_patch, r6_patch, r7_patch, r8_patch, r9_patch, im_patch, sum_patch, sum2_patch], loc='best', fontsize = "x-small")
        
        self.static_canvas.draw()

if __name__ == '__main__':
    data_queue = multiprocessing.Queue()

    app = qt.QApplication(sys.argv)
    window = gui(data_queue)
    window.show()
    app.exec()