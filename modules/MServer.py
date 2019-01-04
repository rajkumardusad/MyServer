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
from php import *
from py import *
from ng import *
from apa import *

class Manual(object):
  def MS(self):
    while True:
      mslogo()
      Tool = raw_input(''' \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m''')
      if Tool == "1":
        if os.path.exists(bpath+"php"):
          php()
        else:
          pyweb().chkpy()
          break
      elif Tool == "2":
        php()
      elif Tool == "3":
        pyweb().chkpy()
        break
      elif Tool == "4":
        if os.path.exists(bpath+"apachectl"):
          apache().asr()
          break
        elif os.path.exists("/usr/sbin/apache2"):
          apache().asr()
          break
        else:
          Mylogo()
          print("\n\033[01;33minstalling Apache2 web server .........\033[00m\n")
          os.system(pac+" update")
          os.system(pac+" install apache2 -y")
          apache().asr()
          break
      elif Tool == "5":
        if os.path.exists(bpath+"nginx"):
          nginx().ng()
          break
        elif os.path.exists("/usr/sbin/nginx"):
          nginx().ng()
          break
        else:
          Mylogo()
          print("\n\033[01;33minstalling Nginx web server .........\033[00m\n")
          os.system(pac+" update")
          os.system(pac+" install nginx -y")
          nginx().ng()
          break
      elif Tool == "0" or Tool=="back":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
      sleep(0.7)

def MServer():
  Manual().MS()
