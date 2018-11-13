# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from modules.system import *
from modules.ux import *
from modules.load import load
from modules.menu import menu
from modules.logo import notin

class oschek(object):
  def ch_os(self):
	if "linux" in sys.platform:
       # Running MyServer on linux ...
	   pass
	elif "darwin" in sys.platform:
	   print("Sorry, MyServer is not available for windows right now...")
	   exit()
	elif "win" in sys.platform:
	   print("Sorry, MyServer is not available for windows right now...")
	   exit()
	else:
	   print("MyServer is not available for \'%s\' right now !!!" %sys.platform)
	   exit()

class inschek(object):
  def ch_ins(self):
    if system=="termux":
      if os.path.exists(bpath+"myserver"):
        pass
      else:
        notin()
        opt=raw_input("\033[01;33m Do you want to install MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
        if opt=="Y" or opt=="y":
          os.system("sh install")
        elif opt=="N" or opt=="n":
          exit()
        else:
          print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
          sleep(1)
          self.ch_ins()
    elif system=="ubuntu":
      if os.path.exists(bpath+"myserver"):
        pass
      else:
        notin()
        opt=raw_input("\033[01;33m Do you want to install MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
        if opt=="Y" or opt=="y":
          os.system("sh install")
        elif opt=="N" or opt=="n":
          exit()
        else:
          print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
          sleep(1)
          self.ch_ins()
    elif system=="debian":
      if os.path.exists(bpath+"myserver"):
        pass
      else:
        notin()
        opt=raw_input("\033[01;33m Do you want to install MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
        if opt=="Y" or opt=="y":
          os.system("sh install")
        elif opt=="N" or opt=="n":
          exit()
        else:
          print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
          sleep(1)
          self.ch_ins()

def MyServer():
  try:
	load()
	oschek().ch_os()
	inschek().ch_ins()
	menu()

  except KeyboardInterrupt:
	exit()
MyServer()