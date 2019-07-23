# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *

class apache_server(object):
  def asr(self):
    if os.path.exists(bpath+"apachectl"):
      os.system("apachectl")
      sleep(0.1)
      self.apa()
    elif os.path.exists("/usr/sbin/apachectl"):
      os.system("apachectl start")
      sleep(0.1)
      self.apa()
    elif os.path.exists("/usr/sbin/apache2"):
      os.system("apache2 start")
      sleep(0.1)
      self.apa()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;33mApache Server\033[01;31m in your "+system+".\033[00m")
      sleep(3)

  def apa(self):
    os.system("python modules/.srvr.aex")
    Mylogo()
    if os.path.exists(bpath+"apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[00m ");
      if stop=="0":
        os.system("apachectl stop")
        sleep(2)
        print("\n\007\033[01;33mApache web server\033[01;31m stopped !! \033[00m")
        sys.exit()
      else:
        self.apa()
    elif os.path.exists("/usr/sbin/apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[00m ");
      if stop=="0":
        os.system("apachectl stop")
        sleep(2)
        print("\n\007\033[01;33mApache web server\033[01;31m stopped !! \033[00m")
        sys.exit()
      else:
        self.apa()
    elif os.path.exists("/usr/sbin/apache2"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[00m ");
      if stop=="0":
        os.system("apache2 stop")
        sleep(2)
        print("\n\007\033[01;33mApache web server\033[01;31m stopped !! \033[00m")
        sys.exit()
      else:
        self.apa()

def apache():
  if os.path.exists(bpath+"apachectl") or os.path.exists("/usr/sbin/apache2") or os.path.exists("/usr/sbin/apachectl"):
    apache_server().asr()
  else:
    Mylogo()
    print("\n\n\033[01;31m   [\033[01;33m+\033[01;31m] \033[01;36mApache Server \033[01;31mis not installed in your "+system+".")
    opt=input("\n\033[01;33m Do you want to install Apache Server [\033[01;32mY/n\033[01;33m] >>\033[00m ")
    if opt=="y" or opt=="Y":
      Mylogo()
      print("\n\033[01;33minstalling Apache Server ......\033[00m\n")
      sleep(1)
      os.system(pac+" update")
      os.system(pac+" install apache2 -y")
      apache_server().asr()