# Globals
phoneList = []

version = "1.0.1"
global m
global e

#Libraries
import io
import base64
import os
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from tkinter import messagebox
    from tkinter.ttk import *
    from tkinter import *
    from PIL import Image, ImageTk
    from urllib.request import urlopen
    import os
    from os import path

from functools import partial
import requests
import time

# Read values for IP address of phone 

def readIP():
    if path.exists('ip.txt'):
        f = open("ip.txt", "r")
        i = f.read()
        f.close()
    else:
        print("Default Ip Loaded")
        f = open("ip.txt", "w")
        f.write("192.168.1.xxx")
        f.close()
        f = open("ip.txt", "r")
        i = f.read()
        f.close()
    return i


# Read values for Password of phone

def readPasscode():
    if path.exists('pass.txt'):
        f = open("pass.txt", "r")
        p = f.read()
        f.close()
    else:
        print("Default Ip Loaded")
        f = open("pass.txt", "w")
        f.write("kostas")
        f.close()
        f = open("pass.txt", "r")
        p = f.read()
        f.close()
    return p


# Start Program 

# Load Data
ip = readIP()
passw = readPasscode()

def callelmi():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2102002200&account=0&password="+passw)
    return
def callelmiFO():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2102002321&account=0&password="+passw)
    return
def callinfopos():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2105690275&account=0&password="+passw)
    return
def callics():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2105778260&account=0&password="+passw)
    return

def callelzab():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2109819810&account=0&password="+passw)
    return

def calloktabit():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2118888885&account=0&password="+passw)
    return

def callinfolex():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2106722230&account=0&password="+passw)
    return

def callkonica():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2102896666&account=0&password="+passw)
    return

def callsunsoft():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=2109317811&account=0&password="+passw)
    return

def callKOSTAS():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=105&account=0&password="+passw)
    return

def callGIANNIS():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=101&account=0&password="+passw)
    return

def callNIA():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=112&account=0&password="+passw)
    return

def callHLIAS():
    requests.get("http://"+ ip + "/cgi-bin/api-make_call?phonenumber=103&account=0&password="+passw)
    return

def menu(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_separator()

    filemenu.add_command(label="Κλείσιμο", command=closeApp)
    menubar.add_cascade(label="Επιλογές", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)



    editmenu.add_command(label="Αλλαγή IP", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Αλλαγή Κωδικού", command=donothing)

    menubar.add_cascade(label="Επεξεργασία", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Σχετικά με...", command=aboutWindowInfo)
    menubar.add_cascade(label="Βοήθεια", menu=helpmenu)
    return menubar


def closeApp():
    os._exit(0)


def aboutWindowInfo():
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    inf = "Σωφρονάς Κωνσταντίνος Σωτήριος\nsofronas.konstantinos@gmail.com\n6983733807\n\nVersion:"
    global version
    inf = inf + version
    messagebox.showinfo("Σχετικά με την εφαρμογή", inf)
    root.destroy()

def donothing():
    print("nothing")

root = tk.Tk()
root['bg'] = 'white'
root.title("G-PhoneCaller")
root.resizable(0,0)
root.geometry("260x500")
root.config(menu=menu(root))


# create a labeled frame for the keypad buttons
# relief='groove' and labelanchor='nw' are default


photoELMI = PhotoImage(file = r"C:\CALLER\elmi.png")
photoELMIimage = photoELMI.subsample(3, 3)
Button(root, text = 'ΕΛΜΗ', image = photoELMIimage,compound = LEFT,bg='white',height = 30, width = 165,command=callelmi).pack(side = TOP)

photoELMIFO = PhotoImage(file = r"C:\CALLER\elmi.png")
photoELMIimageFO = photoELMIFO.subsample(3, 3)
Button(root, text = 'ΦΟΡΟΛΟΓΙΚΟΙ', image = photoELMIimageFO,compound = LEFT,bg='white',height = 30, width = 165,command=callelmiFO).pack(side = TOP)

photoICS = PhotoImage(file= r"C:\CALLER\ics.png")
photoICSimage = photoICS.subsample(3, 3)
Button(root, text = 'ICS', image = photoICSimage,compound = LEFT,bg='white',height = 30, width = 165,command=callics).pack(side = TOP)

photoELZAB = PhotoImage(file= r"C:\CALLER\elzab.png")
photoELZABimage = photoELZAB.subsample(3,3)
Button(root, text = "ELZAB", image = photoELZABimage,compound = LEFT,bg='white',height = 30, width = 165,command=callelzab).pack(side = TOP)

photoINFOPOS = PhotoImage(file= r"C:\CALLER\infopos.png")
photoINFOPOSimage = photoINFOPOS.subsample(3,3)
Button(root, text = "INFOPOS", image = photoINFOPOSimage,compound = LEFT,bg='white',height = 30, width = 165,command=callinfopos).pack(side = TOP)

photoOKTABIT = PhotoImage(file= r"C:\CALLER\OKTABIT.png")
photoOKTABITimage = photoOKTABIT.subsample(3,3)
Button(root, text = "OKTABIT", image = photoOKTABITimage,compound = LEFT,bg='white',height = 30, width = 165,command=calloktabit).pack(side = TOP)

photoINFOLEX = PhotoImage(file= r"C:\CALLER\INFOLEX.png")
photoINFOLEXimage = photoINFOLEX.subsample(3,3)
Button(root, text = "INFOLEX", image = photoINFOLEXimage,compound = LEFT,bg='white',height = 30, width = 165, command=callinfolex).pack(side = TOP)

photoKONICA = PhotoImage(file= r"C:\CALLER\KONICA.png")
photoKONICAimage = photoKONICA.subsample(3,3)
Button(root, text = "KONICA", image = photoKONICAimage,compound = LEFT,bg='white',height = 30, width = 165,command=callkonica).pack(side = TOP)

photoSUNSOFT = PhotoImage(file= r"C:\CALLER\sunsoft.png")
photoSUNSOFTimage = photoSUNSOFT.subsample(3,3)
Button(root, text = "SUNSOFT", image = photoSUNSOFTimage, compound = LEFT, bg='white',height = 30, width = 165,command=callsunsoft).pack(side = TOP)

Button(root, text = "Interior - 1010",height = 2, width = 23,bg='white',command=callKOSTAS).pack(side = TOP)

root.mainloop()
