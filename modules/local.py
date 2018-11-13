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

class lt(object):
  def notinl(self):
    Mylogo()
    print("\n\n\033[1;31m  Error \033[01;33m\'localtunnel\' \033[01;31mis not installed in "+system+".\033[00m")
    sleep(2)

  def locals(self):
    while True:
      os.system("python2 modules/.srvr.aex")
      Mylogo()
      dn = raw_input('''\n\n\033[1;33m  Enter your subdomain name (\033[01;32mex Myweb\033[01;33m) :- \033[1;36m''')

      port = raw_input('''\033[1;33m  Enter your port (\033[01;32mex 8080\033[01;33m) :- \033[1;36m''')

      os.system("python2 modules/.srvr.aex")

      Mylogo()
      print("\n\033[01;33mStarting Server ......\033[00m\n")
      if os.path.exists(bpath+"lt"):
        os.system("lt --port "+port+" --subdomain "+dn)
        print("\n\033[01;31m unfortunately server stopped\n\033[00m")
        ex()
      elif os.path.exists("/usr/local/bin/lt"):
        os.system("lt --port "+port+" --subdomain "+dn)
        print("\033[01;31m unfortunately server stopped\n\033[00m")
        ex()
      elif os.path.exists("/usr/sbin/lt"):
        os.system("lt --port "+port+" --subdomain "+dn)
        print("\n\033[01;31m unfortunately server stopped\n\033[00m")
        ex()
      else:
        ins().localin()
        if os.path.exists("/data/data/com.termux/files/usr/bin/lt"):
          self.locals()
        elif os.path.exists("/usr/bin/lt"):
          self.locals()
        elif os.path.exists("/usr/local/bin/lt"):
          self.locals()
        elif os.path.exists("/usr/sbin/lt"):
          self.locals()
        else:
          self.notinl()
          break

class ins(object):
  def localin(self):
    Mylogo()
    print("\n\033[01;32mInstalling Localtunnel.......\033[00m\n")
    if system=="termux":
      lt().notinl()
    elif system=="debian":
      os.system(pac+" install sudo -y")
      os.system(pac+" update")
      os.system(pac+" upgrade -y")
      os.system(pac+" install curl python-software-properties -y")
      os.system("curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -")
      os.system(pac+" install nodejs -y")
      os.system(pac+" install npm -y")
      os.system("npm install -g localtunnel")
      if os.path.exists("/data/data/com.termux/files/usr/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/local/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/sbin/lt"):
        lt().locals()
      else:
        lt().notinl()

    elif system=="ubuntu":
      os.system(pac+" update")
      os.system(pac+" upgrade -y")
      os.system(pac+" install nodejs -y")
      os.system(pac+" install npm -y")
      os.system("sudo npm install -g localtunnel")
      if os.path.exists("/data/data/com.termux/files/usr/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/local/bin/lt"):
        lt().locals()
      elif os.path.exists("/usr/sbin/lt"):
        lt().locals()
      else:
        lt().notinl()

def chklt():
  if os.path.exists("/data/data/com.termux/files/usr/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/local/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/sbin/lt"):
	lt().locals()
  else:
    ins().localin()

def local():
	chklt()