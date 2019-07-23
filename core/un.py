# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *

class Un(object):
  def Uni(self):
    while True:
      Mylogo()
      ask = input("\n\n\033[1;33m Do you want to uninstall MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if ask == "n" or ask == "N":
        break
      elif ask == "Y" or ask == "y":
        if system=="ubuntu":
          os.system("cd "+spath+" && sudo rm -rf MyServer")
          os.system("sudo rm -rf "+bpath+"myserver")
          os.system("cd "+spath+" && sudo rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
        else:
          os.system("rm -rf "+bpath+"myserver")
          os.system("cd "+spath+" && rm -rf MyServer")
          os.system("cd "+spath+" && rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
        exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ask+"\'")
        sleep(1)

Un().Uni()