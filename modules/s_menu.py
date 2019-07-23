# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *
from modules.logo import *
from modules.php import *
from modules.pyweb import *
from modules.default_s import *
from modules.apache import *
from modules.nginx import *

class Manual(object):
  def MS(self):
    while True:
      mslogo()
      Tool = input(" \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      if Tool == "1":
        default_s()
      elif Tool == "2":
        php()
      elif Tool == "3":
        pyweb()
      elif Tool == "4":
        apache()
      elif Tool == "5":
        nginx()
      elif Tool == "0" or Tool=="back":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
      sleep(0.7)

def s_menu():
  Manual().MS()