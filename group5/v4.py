# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1325, 839)
        MainWindow.setStyleSheet("background-color: rgb(184, 226, 244)\n" "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coulom_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.coulom_lcd.setGeometry(QtCore.QRect(40, 40, 81, 31))
        self.coulom_lcd.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.coulom_lcd.setObjectName("coulom_lcd")
        self.volt_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.volt_lcd.setGeometry(QtCore.QRect(140, 40, 81, 31))
        self.volt_lcd.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.volt_lcd.setObjectName("volt_lcd")
        self.joules_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.joules_lcd.setGeometry(QtCore.QRect(240, 40, 71, 31))
        self.joules_lcd.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.joules_lcd.setObjectName("joules_lcd")
        self.protons_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.protons_lcd.setGeometry(QtCore.QRect(330, 40, 81, 31))
        self.protons_lcd.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.protons_lcd.setObjectName("protons_lcd")
        self.coulombs_label = QtWidgets.QLabel(self.centralwidget)
        self.coulombs_label.setGeometry(QtCore.QRect(30, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.coulombs_label.setFont(font)
        self.coulombs_label.setObjectName("coulombs_label")
        self.protons_lablel = QtWidgets.QLabel(self.centralwidget)
        self.protons_lablel.setGeometry(QtCore.QRect(330, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.protons_lablel.setFont(font)
        self.protons_lablel.setObjectName("protons_lablel")
        self.joules_label = QtWidgets.QLabel(self.centralwidget)
        self.joules_label.setGeometry(QtCore.QRect(240, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.joules_label.setFont(font)
        self.joules_label.setObjectName("joules_label")
        self.volts_label = QtWidgets.QLabel(self.centralwidget)
        self.volts_label.setGeometry(QtCore.QRect(150, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.volts_label.setFont(font)
        self.volts_label.setObjectName("volts_label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 90, 921, 681))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setAcceptDrops(False)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);\n" "")
        self.graphicsView.setObjectName("graphicsView")
        self.R0 = QtWidgets.QCheckBox(self.centralwidget)
        self.R0.setGeometry(QtCore.QRect(970, 90, 51, 20))
        self.R0.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R0.setObjectName("R0")
        self.R2 = QtWidgets.QCheckBox(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(1150, 90, 51, 20))
        self.R2.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R2.setObjectName("R2")
        self.R1 = QtWidgets.QCheckBox(self.centralwidget)
        self.R1.setGeometry(QtCore.QRect(1060, 90, 51, 20))
        self.R1.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R1.setObjectName("R1")
        self.R9 = QtWidgets.QCheckBox(self.centralwidget)
        self.R9.setGeometry(QtCore.QRect(1060, 410, 61, 20))
        self.R9.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R9.setObjectName("R9")
        self.R8 = QtWidgets.QCheckBox(self.centralwidget)
        self.R8.setGeometry(QtCore.QRect(970, 410, 61, 20))
        self.R8.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R8.setObjectName("R8")
        self.R6 = QtWidgets.QCheckBox(self.centralwidget)
        self.R6.setGeometry(QtCore.QRect(1140, 250, 51, 20))
        self.R6.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R6.setObjectName("R6")
        self.R7 = QtWidgets.QCheckBox(self.centralwidget)
        self.R7.setGeometry(QtCore.QRect(1230, 250, 51, 20))
        self.R7.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R7.setObjectName("R7")
        self.R3 = QtWidgets.QCheckBox(self.centralwidget)
        self.R3.setGeometry(QtCore.QRect(1240, 90, 51, 20))
        self.R3.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R3.setObjectName("R3")
        self.R5 = QtWidgets.QCheckBox(self.centralwidget)
        self.R5.setGeometry(QtCore.QRect(1050, 250, 51, 20))
        self.R5.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R5.setObjectName("R5")
        self.R4 = QtWidgets.QCheckBox(self.centralwidget)
        self.R4.setGeometry(QtCore.QRect(970, 250, 51, 20))
        self.R4.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.R4.setTristate(False)
        self.R4.setObjectName("R4")
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
        self.groupBox_R8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R8.setGeometry(QtCore.QRect(960, 430, 81, 131))
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
        self.groupBox_R9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_R9.setGeometry(QtCore.QRect(1050, 430, 81, 131))
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
        self.verticalLayout_R9.addWidget(self.R9_BLM4)
        self.clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all.setGeometry(QtCore.QRect(1170, 520, 93, 28))
        self.clear_all.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.clear_all.setObjectName("clear_all")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(970, 570, 171, 101))
        self.groupBox.setStyleSheet("background-color: rgb(184, 226, 244);")
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
        self.blm_sum_min_time.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.blm_sum_min_time.setMaximum(500.0)
        self.blm_sum_min_time.setObjectName("blm_sum_min_time")
        self.blm_sum_max_time = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.blm_sum_max_time.setGeometry(QtCore.QRect(50, 60, 71, 31))
        self.blm_sum_max_time.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.blm_sum_max_time.setMaximum(500.0)
        self.blm_sum_max_time.setObjectName("blm_sum_max_time")
        self.BLM_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BLM_groupBox.setGeometry(QtCore.QRect(420, 20, 120, 51))
        self.BLM_groupBox.setObjectName("BLM_groupBox")
        self.BLM_unit_drop_box = QtWidgets.QComboBox(self.BLM_groupBox)
        self.BLM_unit_drop_box.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.BLM_unit_drop_box.setAcceptDrops(False)
        self.BLM_unit_drop_box.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.BLM_unit_drop_box.setObjectName("BLM_unit_drop_box")
        self.BLM_unit_drop_box.addItem("")
        self.BLM_unit_drop_box.addItem("")
        self.BLM_unit_drop_box.addItem("")
        self.BLM_unit_drop_box.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1160, 420, 131, 101))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.SUM = QtWidgets.QCheckBox(self.groupBox_3)
        self.SUM.setGeometry(QtCore.QRect(0, 10, 91, 20))
        self.SUM.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.SUM.setObjectName("SUM")
        self.SUM_MINUS_R1_R2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.SUM_MINUS_R1_R2.setGeometry(QtCore.QRect(0, 40, 131, 20))
        self.SUM_MINUS_R1_R2.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.SUM_MINUS_R1_R2.setObjectName("SUM_MINUS_R1_R2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(0, 70, 91, 20))
        self.checkBox.setStyleSheet('font: 75 11pt "MS Shell Dlg 2";')
        self.checkBox.setObjectName("checkBox")
        self.mode_selection = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_selection.setGeometry(QtCore.QRect(1150, 570, 121, 101))
        self.mode_selection.setObjectName("mode_selection")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.mode_selection)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 81, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mode_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mode_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mode_verticalLayout.setObjectName("mode_verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.mode_verticalLayout.addWidget(self.radioButton_2)
        self.sum_button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sum_button.setObjectName("sum_button")
        self.mode_verticalLayout.addWidget(self.sum_button)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(990, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.R5IM_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.R5IM_groupBox.setGeometry(QtCore.QRect(560, 20, 120, 51))
        self.R5IM_groupBox.setObjectName("R5IM_groupBox")
        self.R5IM_unit_dropBox = QtWidgets.QComboBox(self.R5IM_groupBox)
        self.R5IM_unit_dropBox.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.R5IM_unit_dropBox.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.R5IM_unit_dropBox.setObjectName("R5IM_unit_dropBox")
        self.R5IM_unit_dropBox.addItem("")
        self.R5IM_unit_dropBox.addItem("")
        self.R5IM_unit_dropBox.addItem("")
        self.R5IM_unit_dropBox.addItem("")
        self.N_time = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.N_time.setGeometry(QtCore.QRect(710, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N_time.setFont(font)
        self.N_time.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.N_time.setMaximum(500.0)
        self.N_time.setObjectName("N_time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 20, 121, 16))
        self.label.setObjectName("label")
        self.Warningbox = QtWidgets.QComboBox(self.centralwidget)
        self.Warningbox.setGeometry(QtCore.QRect(980, 680, 331, 31))
        self.Warningbox.setStyleSheet(
            'font: 100 10pt "MS Shell Dlg 2";\n' "background-color: rgb(85, 255, 127)"
        )
        self.Warningbox.setMaxVisibleItems(50)
        self.Warningbox.setPlaceholderText("")
        self.Warningbox.setObjectName("Warningbox")
        self.Warningbox.addItem("")
        self.Text_warning_field = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_warning_field.setGeometry(QtCore.QRect(980, 720, 321, 71))
        self.Text_warning_field.setObjectName("Text_warning_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1325, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
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
        self.BLM_groupBox.setTitle(_translate("MainWindow", "Select units BLM"))
        self.BLM_unit_drop_box.setItemText(0, _translate("MainWindow", "Coloumbs"))
        self.BLM_unit_drop_box.setItemText(1, _translate("MainWindow", "Joules"))
        self.BLM_unit_drop_box.setItemText(2, _translate("MainWindow", "Volts"))
        self.BLM_unit_drop_box.setItemText(3, _translate("MainWindow", "Protons"))
        self.SUM.setText(_translate("MainWindow", "SUM"))
        self.SUM_MINUS_R1_R2.setText(_translate("MainWindow", "SUM -R1 -R2"))
        self.checkBox.setText(_translate("MainWindow", "R5IM"))
        self.mode_selection.setTitle(_translate("MainWindow", "Select method"))
        self.radioButton_2.setText(_translate("MainWindow", "Mean"))
        self.sum_button.setText(_translate("MainWindow", "Sum"))
        self.label_2.setText(_translate("MainWindow", "Signal selection to plot"))
        self.R5IM_groupBox.setTitle(_translate("MainWindow", "Select units R5IM"))
        self.R5IM_unit_dropBox.setItemText(0, _translate("MainWindow", "Coloumbs"))
        self.R5IM_unit_dropBox.setItemText(1, _translate("MainWindow", "Joules"))
        self.R5IM_unit_dropBox.setItemText(2, _translate("MainWindow", "Volts"))
        self.R5IM_unit_dropBox.setItemText(3, _translate("MainWindow", "Protons"))
        self.label.setText(_translate("MainWindow", "RMS Dislplay time"))
        self.Warningbox.setCurrentText(_translate("MainWindow", "Warnings"))
        self.Warningbox.setItemText(0, _translate("MainWindow", "Warnings"))
        self.Text_warning_field.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Text box for selecting warning - dispays amount of data lost, between which two points, and the timestamp</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())