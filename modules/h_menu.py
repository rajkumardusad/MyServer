# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *
from modules.default_h import *
from modules.logo import *
from modules.local import *
from modules.open import *

class ngrok(object):
  def insng(self):
    Mylogo()
    if os.path.exists(bpath+"ngrok"):
      self.chsng()
    else:
      print("\n\n\033[01;32mInstalling ngrok ....\n")
      os.system("sh core/LiNgrok.sh")
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
      h_menu()

  def token(self):
    os.system("python modules/.srvr.aex")
    Mylogo()
    auth=input("\n\n\033[01;33m You have ngrok authtoken [Y/n] :- \033[01;36m")
    if auth=="y" or auth=="Y":
      getauth=input("\033[01;33m Enter your ngrok authtoken :- \033[01;36m")
      os.system("ngrok authtoken "+getauth)
      self.ngrk()
    else:
      self.ngrk()

  def ngrk(self):
    acp=input("\033[01;33m You have paid ngrok account [Y/n] :- \033[01;36m")
    if acp=="Y" or acp=="y":
      self.paid()
    else:
      self.free()

  def free(self):
    getp=input("\033[01;33m Enter your port (\033[01;32mex 8080\033[01;33m) :- \033[01;36m")
    port=getp
    os.system("ngrok http "+port)
    print("\033[01;31m unfortunately server stopped\n\033[00m")
    sys.exit()

  def paid(self):
    getsub=input("\033[01;33m Enter your subdomain name (\033[01;32mex myweb\033[01;33m) :- \033[01;36m")
    getp=input("\n\033[01;33m Enter your port (\033[01;32mex 8080\033[01;33m) :- \033[01;36m")
    port=getp
    os.system("ngrok http -subdomain="+getsub+" "+port)
    print("\n\033[01;31munfortunately server stopped\n\033[00m")
    sys.exit()

class mh(object):
  def mn(self):
    while True:
      mhlogo()
      Tool = input(" \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      if Tool == "1":
        default_h()
      elif Tool == "2":
        open()
      elif Tool == "3":
        ngrok().insng()
        break
      elif Tool == "4":
        local()
      elif Tool == "0" or Tool=="back":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
        sleep(0.7)

def h_menu():
  mh().mn()