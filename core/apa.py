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

class apache(object):
  def asr(self):
    if os.path.exists(bpath+"apachectl"):
      os.system("apachectl")
      sleep(4)
      self.apa()
    elif os.path.exists("/usr/sbin/apachectl"):
      os.system("apachectl start")
      sleep(4)
      self.apa()
    elif os.path.exists("/usr/sbin/apache2"):
      os.system("apache2 start")
      sleep(4)
      self.apa()
    else:
      Mylogo()
      print("\n\n\007\033[01;31m  Error \033[01;33mApache \033[01;31mNot installed.\033[00m")
      ex()

  def apa(self):
    os.system("python2 modules/.srvr.aex")
    Mylogo()
    if os.path.exists(bpath+"apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("rm -rf /data/data/com.termux/files/usr/var/run/apache2/httpd.pid")
        os.system("apachectl stop")
        sleep(2)
        print("\n\007\033[01;33m  Apache web server\033[01;31m stopped !! \033[00m")
      else:
        self.apa()

    elif os.path.exists("/usr/sbin/apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("apachectl stop")
        sleep(2)
        print("\n\007\033[01;33m  Apache web server\033[01;31m stopped !! \033[00m")
      else:
        self.apa()

    elif os.path.exists("/usr/sbin/apache2"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("apache2 stop")
        sleep(2)
        print("\n\007\033[01;33m  Apache web server\033[01;31m stopped !! \033[00m")
      else:
        self.apa()