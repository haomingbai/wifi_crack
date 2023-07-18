# coding=utf8
import imp
import os
try:
    imp.find_module('pywifi')
    found1 = True
except ImportError:
    found1 = False
while found1==False :
    os.system(f'pip install pywifi')
    try:
        imp.find_module('pywifi')
        found1 = True
    except ImportError:
        found1 = False
wifi = pywifi.PyWiFi()

