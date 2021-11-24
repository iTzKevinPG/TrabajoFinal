#!/usr/bin/env python
import wx
import wx.grid
from datetime import datetime
import requests
import tkinter as tk
from tkinter import * 
from tkinter import ttk


class Ventana():

    mainWindow = tk.Tk()
    pageVariable = StringVar()
    style = ttk.Style(mainWindow)
    treeViewTable = ttk.Treeview(mainWindow, columns="#0, #1, #2")
    dataTabla = []

    def __init__(self, titulo):
        self.mainWindow.geometry("900x500")
        self.mainWindow.title(titulo)
        self.mainWindow.resizable(False, False)
        self.mainWindow.config(background = "#484848")
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#D1D1D1", fieldbackground="#D1D1D1", foreground="#D1D1D1", font=("Cambria", 10), anchor=CENTER)

    def getUsers(self):

        for item in self.treeViewTable.get_children():
            self.treeViewTable.delete(item)

        self.loadData(self.dataTabla)

    pass

    def loadData(self, data):

        for user in data:

            userExtraData = []
            idUsuario = user['name']
            userExtraData.append(f"{user['email']}")
            userExtraData.append(f"{user['gender']}")
            userExtraData.append(f"{user['status']}")
            self.treeViewTable.insert("",END, text=idUsuario, values=userExtraData, tags=('gr',))

    pass

    def titulo(self, titleText):
        self.title = Label(text=titleText, font=("Cambria", 13), bg="#FFC500", fg="black", width="450", height="2")
        self.title.pack()

    def labels(self, textLabel, positionX, positionY):
        self.pageText = Label(text=textLabel, font=("Cambria", 10), bg="#B5B5B5")
        self.pageText.place(x=positionX, y=positionY)

    def labels_entrada(self, positionX, positionY):
        self.numberPage = Entry(textvariable=self.pageVariable, font=("Cambria", 10), width="70", bg="#D1D1D1")
        self.numberPage.place(x=positionX, y=positionY)

    def botones(self, textName, positionX, positionY):
        self.buttonLoad = Button(self.mainWindow, text=textName, command=self.getUsers,font=("Cambria", 11), width="20", height="2", bg="#FFC500")
        self.buttonLoad.place(x=positionX, y=positionY)

    def cargar_tabla(self, data, positionX, positionY):
        self.treeViewTable.tag_configure('gr', background='#D1D1D1')
        self.treeViewTable.place(x=positionX, y=positionY)
        self.treeViewTable.heading("#0", text="Nombre", anchor=CENTER)
        self.treeViewTable.heading("#1", text="Email", anchor=CENTER)
        self.treeViewTable.heading("#2", text="Genero", anchor=CENTER)
        self.treeViewTable.heading("#3", text="Estado", anchor=CENTER)
        self.dataTabla = data

    def iniciar(self):
        self.mainWindow.mainloop()



