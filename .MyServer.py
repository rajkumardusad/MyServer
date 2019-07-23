# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 4/July/2019
# Powered By :- Aex Software's

import sys, os
from time import sleep
from core.system import *
from modules.logo import *
from modules.menu import *

class inst:
  def chk_sys(self):
    if "linux" in sys.platform or "linux2" in sys.platform:
      self.chk_inst()
    elif "darwin" in sys.platform:
      print("Sorry, MyServer is not available for mac right now !!")
      sys.exit()
    elif "win" in sys.platform:
      print("Sorry, MyServer is not available for windows right now !!")
      sys.exit()
    else:
      print("MyServer is not available for \'%s\' right now !!!" %sys.platform)
      sys.exit()

  def chk_inst(self):
    if os.path.exists(bpath+"myserver") and os.path.exists(spath+"MyServer"):
      menu()
    else:
      self.inst()

  def inst(self):
    if system=="ubuntu":
      noti()
      opt=raw_input("\033[01;33m Do you want to install MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if opt=="Y" or opt=="y":
        os.system("sh install")
      elif opt=="N" or opt=="n":
        sys.exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
        sleep(1)
        self.inst()
    else:
      noti()
      opt=raw_input("\033[01;33m Do you want to install MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if opt=="Y" or opt=="y":
        os.system("sh install")
      elif opt=="N" or opt=="n":
        sys.exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
        sleep(1)
        self.inst()

def MyServer():
  try:
    inst().chk_sys()
  except KeyboardInterrupt:
    exit()
MyServer()