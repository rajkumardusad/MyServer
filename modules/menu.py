# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from modules.load import *
from core.system import *
from modules.logo import *
from modules.setting import *
from modules.update import *
from modules.default_s import *
from modules.s_menu import *
from modules.h_menu import *
from modules.mysql import *

class main(object):
  def about(self):
    while True:
      ab()
      back = input(" \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      if back == "" or back == "back" or back == "Back" or back == "0":
        self.menu()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+back+"\'")
        sleep(1)

  def uninstall(self):
    while True:
      Mylogo()
      ask = input("\n\033[1;33m Do you want to uninstall MyServer [\033[01;32mY/n\033[01;33m] >> \033[1;36m")
      if ask == "n" or ask == "N":
        break
      elif ask == "Y" or ask == "y":
        if os.path.exists(bpath+"myserver") or os.path.exists(spath+"MyServer"):
          if system=="ubuntu":
            os.system("sudo rm -rf "+spath+"MyServer && rm -rf "+bpath+"myserver")
            os.system("cd "+spath+" && sudo rm -rf .path.aex .port.aex .host.aex .serv.lock .h.lock")
          else:
            os.system("rm -rf "+spath+"MyServer && rm -rf "+bpath+"myserver")
            os.system("cd "+spath+" && rm -rf .path.aex .port.aex .host.aex .serv.lock .h.lock")
        exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ask+"\'")
        sleep(1)

  def menu(self):
    while True:
      logo()
      Tool = input(" \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      if Tool == "1":
        default_s()
      elif Tool == "2":
        default_h()
      elif Tool == "3":
        Mys()
      elif Tool == "4":
        s_menu()
      elif Tool == "5":
        h_menu()
      elif Tool == "6":
        update()
      elif Tool == "7":
        setting()
      elif Tool == "8":
        self.about()
      elif Tool == "Uninstall MyServer" or Tool == "uninstall myserver" or Tool == "rm -T":
        self.uninstall()
      elif Tool == "exit":
        exit()
      elif Tool == "x":
        Toolo = input("\n\033[1;32m Do you want to Exit ? [\033[01;33mY/n\033[01;32m] >>  \033[01;36m")
        if Toolo == "N" or Toolo == "n":
          pass
        elif Toolo == "Y" or Toolo == "y":
          exit()
        else:
          print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Toolo+"\'")
          sleep(1)
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
        sleep(1)

def menu():
  load()
  main().menu()