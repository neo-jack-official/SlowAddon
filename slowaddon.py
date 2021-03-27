#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack


import random
import sys, os, time
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
   

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import *

def ini():       
    slow = "slowhttptest"
    c = "-c"
    i = "-i"
    r = "-r"
    u = "-u"
    t = "-t"
    k = "-k"
    n = "-n"
    l = "-l"
    print("INFORMACION: \n" + " " + http + host + ":" + met + ".\n Conexiones: " + num_conex + ". Intervalo: " + intervalo1 + " seg." + " N° Clientes por seg. " + conexSeg + "\n Repetir Peticiones: " + PRepetir + ". Intervalo: " + PRInter + "seg. Duracion: " + dura + "seg.\n Proxy a usar: " + tor)
    print("")
    print("Comando: " + tor + " " + slow + " " + c + " " + num_conex + " " + i + " " + intervalo1 + " " + r + " " + conexSeg + " " + u + " " + http + host + " " + t + " " + met + " " + k + " " + PRepetir + " " + n + " " + PRInter + " " + l + " " + dura) 
    print("")
    print("Ejecutando...")
    system(tor + " " + slow + " " + c + " " + num_conex + " " + i + " " + intervalo1 + " " + r + " " + conexSeg + " " + u + " " + http + host + " " + t + " " + met + " " + k + " " + PRepetir + " " + n + " " + PRInter + " " + l + " " + dura ) 


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()  
        self.setGeometry(500, 30, 399, 402)      
        self.initUI() 

    def iniciando(self):        
        global http
        global host
        global met
        global num_conex
        global intervalo1
        global conexSeg
        global PRepetir 
        global PRInter  
        global dura
        global tor

        http = str(http_e.currentText())       
        host = str(target_e.text())        
        met = str(get_post_e.currentText()) 
        num_conex = str(n_conx_e.text()) 
        intervalo1 = str(inter_c_e.text()) 
        conexSeg = str(conex_seg_e.text()) 
        PRepetir = str(peticiones_e.text()) 
        PRInter = str(peticiones_i_e.text()) 
        dura = str(duracion_e.text()) 
        tor = str(tor_e.currentText())     

        if met == "Random":
            data = ["GET", "POST"]
            met = random.choice(data)

        if tor == "No":
            tor = ""
        elif tor == "Torify":
            tor = "torify"
        else:
            tor = "proxychains"

        ini()       

    def initUI(self):        
        global http_e
        global target_e
        global get_post_e
        global n_conx_e
        global inter_c_e
        global conex_seg_e
        global peticiones_e
        global peticiones_i_e
        global duracion_e
        global tor_e

        self.setFixedSize(399, 402)               
        self.setWindowTitle("SlowHttpTest ADDON") 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plugin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
        self.setWindowIcon(icon) 
        self.line_1 = QtWidgets.QFrame(self)
        self.line_1.setGeometry(QtCore.QRect(10, 30, 381, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(10, 230, 381, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(10, 310, 381, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        titulo = QtWidgets.QLabel(self)
        titulo.setGeometry(QtCore.QRect(80, 10, 201, 20)) 
        titulo.setText("Addon for SlowHttpTest") 
        titulo.setStyleSheet("font: 75 italic 13pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 233, 79);")
        titulo.setObjectName("titulo")
        self.text_target = QtWidgets.QLabel(self)
        self.text_target.setGeometry(QtCore.QRect(140, 50, 67, 17))
        self.text_target.setText("Target:") 
        self.text_target.setObjectName("text_target")
        self.rango = QtWidgets.QLabel(self)
        self.rango.setGeometry(QtCore.QRect(80, 120, 71, 17))
        self.rango.setText("(50 a Inf.)") 
        self.rango.setObjectName("rango")     
        self.num_conex = QtWidgets.QLabel(self)
        self.num_conex.setGeometry(QtCore.QRect(10, 100, 201, 17))
        self.num_conex.setText("Num. Conexiones:") 
        self.num_conex.setObjectName("num_conex")
        self.lintervalo = QtWidgets.QLabel(self)
        self.lintervalo.setGeometry(QtCore.QRect(160, 100, 71, 17))
        self.lintervalo.setText("Intervalo:") 
        self.lintervalo.setObjectName("lintervalo")
        self.segundos = QtWidgets.QLabel(self)
        self.segundos.setGeometry(QtCore.QRect(200, 120, 51, 17))
        self.segundos.setText("Seg.") 
        self.segundos.setObjectName("segundos")
        self.conex_seg = QtWidgets.QLabel(self)
        self.conex_seg.setGeometry(QtCore.QRect(240, 100, 141, 17)) 
        self.conex_seg.setText("Conexiones por Seg.:") 
        self.conex_seg.setObjectName("conex_seg")
        self.repetir = QtWidgets.QLabel(self)
        self.repetir.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.repetir.setText("Repetir Peticion:") 
        self.repetir.setObjectName("repetir")
        self.repetir_i = QtWidgets.QLabel(self)
        self.repetir_i.setGeometry(QtCore.QRect(140, 170, 151, 17))
        self.repetir_i.setText("Intervalo de Peticion:") 
        self.repetir_i.setObjectName("repetir_i")
        self.seg2 = QtWidgets.QLabel(self)
        self.seg2.setGeometry(QtCore.QRect(180, 190, 67, 17))
        self.seg2.setText("Seg.") 
        self.seg2.setObjectName("seg2")
        self.duracion_text = QtWidgets.QLabel(self)
        self.duracion_text.setGeometry(QtCore.QRect(300, 170, 67, 17))
        self.duracion_text.setText("Duracion:") 
        self.duracion_text.setObjectName("duracion_text")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(360, 190, 67, 17))
        self.label_14.setText("Seg.") 
        self.label_14.setObjectName("label_14")
        self.tor = QtWidgets.QLabel(self)
        self.tor.setGeometry(QtCore.QRect(10, 250, 121, 17))
        self.tor.setText("Tor Network by:") 
        self.tor.setObjectName("tor")
        self.soket = QtWidgets.QLabel(self)
        self.soket.setGeometry(QtCore.QRect(10, 280, 111, 17))
        self.soket.setText("Proxy Socket5 :")
        self.soket.setObjectName("soket")
        self.autor = QtWidgets.QLabel(self)
        self.autor.setGeometry(QtCore.QRect(240, 370, 141, 20))
        self.autor.setText("Addon by Neo-Jack 2021") 
        self.autor.setStyleSheet("font: 9pt \"Ubuntu\";")
        self.autor.setObjectName("autor")
        http_e = QtWidgets.QComboBox(self)
        http_e.setGeometry(QtCore.QRect(10, 70, 86, 25))
        http_e.setObjectName("http_e")
        http_e.addItem("http://")
        http_e.addItem("https://")
        target_e = QtWidgets.QLineEdit(self)
        target_e.setGeometry(QtCore.QRect(100, 70, 171, 25))
        target_e.setText("www.ejemplo.com")
        target_e.setObjectName("target_e")
        get_post_e = QtWidgets.QComboBox(self)
        get_post_e.setGeometry(QtCore.QRect(280, 70, 86, 25))
        get_post_e.setObjectName("get_post_e")
        get_post_e.addItem("GET")
        get_post_e.addItem("POST")
        n_conx_e = QtWidgets.QLineEdit(self)
        n_conx_e.setGeometry(QtCore.QRect(10, 120, 61, 25))
        n_conx_e.setText("65000")
        n_conx_e.setObjectName("n_conx_e") 
        inter_c_e = QtWidgets.QLineEdit(self)
        inter_c_e.setGeometry(QtCore.QRect(160, 120, 31, 25))
        inter_c_e.setText("2") 
        inter_c_e.setObjectName("inter_c_e")
        conex_seg_e = QtWidgets.QLineEdit(self)
        conex_seg_e.setGeometry(QtCore.QRect(240, 120, 31, 25))
        conex_seg_e.setText("50") 
        conex_seg_e.setObjectName("conex_seg_e") 
        peticiones_e = QtWidgets.QLineEdit(self)
        peticiones_e.setGeometry(QtCore.QRect(10, 190, 31, 25))
        peticiones_e.setText("1")
        peticiones_e.setObjectName("peticiones_e")
        peticiones_i_e = QtWidgets.QLineEdit(self)
        peticiones_i_e.setGeometry(QtCore.QRect(140, 190, 31, 25))
        peticiones_i_e.setText("2") 
        peticiones_i_e.setObjectName("peticiones_i_e")
        duracion_e = QtWidgets.QLineEdit(self)
        duracion_e.setGeometry(QtCore.QRect(300, 190, 51, 25))
        duracion_e.setText("1800")
        duracion_e.setObjectName("duracion_e")    
        tor_e = QtWidgets.QComboBox(self)
        tor_e.setGeometry(QtCore.QRect(120, 280, 141, 25))
        tor_e.setObjectName("tor_e")
        tor_e.addItem("No")
        tor_e.addItem("Torify")
        tor_e.addItem("Proxychanins")
        self.iniciar = QtWidgets.QPushButton(self)
        self.iniciar.setGeometry(QtCore.QRect(150, 340, 89, 25))
        self.iniciar.setText("Iniciar") 
        self.iniciar.setObjectName("iniciar")
        self.iniciar.clicked.connect(self.iniciando) 
        

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
