#!/usr/bin/env python
import os
import sys
import time

def install ():
    print ("1.Install Mariadb")
    pil = input ("Pilih Nomor : ")
    if pil == "1":
       os.system ("pkg install php")
       os.system ("pkg install mariadb")
       os.system ("mariadb --version")
    
install ()