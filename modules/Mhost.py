# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from ux import *
from logo import *
from local import *
from open import *

class ngrok(object):
  def insng(self):
    Mylogo()
    if os.path.exists(bpath+"ngrok"):
      self.chsng()
    else:
      print("\n\n\033[01;32mInstalling ngrok ....\n")
      os.system("sh ~/.MyServer/modules/LiNgrok.sh")
      self.chsng()

  def chsng(self):
    Mylogo()
    if os.path.exists(bpath+"ngrok"):
      self.token()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can not install ngrok in your "+system+".")
      print("\n\033[01;32m Please download ngrok and extract zip or tar file into \033[01;33m/usr/bin\033[01;32m directory.\033[00m")
      sleep(3)
      Mhost()

  def token(self):
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
    Mylogo()
    auth=raw_input("\n\n\033[01;33m You have ngrok authtoken [Y/n] :- \033[01;36m")
    if auth=="y" or auth=="Y":
      getauth=raw_input("\033[01;33m Enter your ngrok authtoken :- \033[01;36m")
      os.system("ngrok authtoken "+getauth)
      self.ngrk()
    else:
      self.ngrk()

  def ngrk(self):
    acp=raw_input("\033[01;33m You have paid ngrok account [Y/n] :- \033[01;36m")
    if acp=="Y" or acp=="y":
      self.paid()
    else:
      self.free()

  def free(self):
    getp=raw_input("\033[01;33m Enter your port (\033[01;32mex 8080\033[01;33m) :- \033[01;36m")
    port=getp
    os.system("ngrok http "+port)
    print("\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

  def paid(self):
    getsub=raw_input("\033[01;33m Enter your subdomain name (\033[01;32mex myweb\033[01;33m) :- \033[01;36m")
    getp=raw_input("\n\033[01;33m Enter your port (\033[01;32mex 8080\033[01;33m) :- \033[01;36m")
    port=getp
    os.system("ngrok http -subdomain="+getsub+" "+port)
    print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

class mh(object):
  def mn(self):
    while True:
      mhlogo()
      Tool = raw_input(''' \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m''')
      if Tool == "1":
        if system=="termux":
          open()
        else:
          local()
      elif Tool == "2":
        open()
      elif Tool == "3":
        ngrok().insng()
        break
      elif Tool == "4":
        local()
      elif Tool == "0":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
        sleep(0.7)

def Mhost():
  mh().mn()