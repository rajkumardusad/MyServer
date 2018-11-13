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
    ex()

  def locals(self):
    while True:
      dn = sys.argv[1]
      port = sys.argv[3]
      h=open(spath+".h.lock","w")
      h.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3])
      h.close()
      os.system("python2 modules/.srvr.aex")
      Mylogo()
      print("\n\033[01;33mStarting Up Server ......\033[00m\n")
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
        self.localin()
        break

  def localin(self):
    Mylogo()
    print("\n\033[01;32mSetting Up Server .......\033[00m\n")
    if system=="termux":
      self.notinl()
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
        self.locals()
      elif os.path.exists("/usr/bin/lt"):
        self.locals()
      elif os.path.exists("/usr/local/bin/lt"):
        self.locals()
      elif os.path.exists("/usr/sbin/lt"):
        self.locals()
      else:
        self.notinl()

    elif system=="ubuntu":
      os.system(pac+" update")
      os.system(pac+" upgrade -y")
      os.system(pac+" install nodejs -y")
      os.system(pac+" install npm -y")
      os.system("sudo npm install -g localtunnel")
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


class openssh(object):
  def notino(self):
    Mylogo()
    print("\n\n\033[1;31m  Error \033[01;33m\'OpenSSH-server\' \033[01;31mis not installed in "+system+".\033[00m")
    ex()

  def opens(self):
    while True:
      if os.path.exists(bpath+"ssh"):
        dn = sys.argv[1]
        portl = sys.argv[2]
        port = sys.argv[3]
        h=open(spath+".h.lock","w")
        h.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3])
        h.close()
        os.system("python2 modules/.srvr.aex")
        Mylogo()
        print("\n\033[01;33mStarting Server ......\033[00m\n")
        os.system("ssh -R "+port+":localhost:"+portl+" "+dn+"@localhost.run")
        print("\n\007\033[01;31m unfortunately server stopped.\n\033[00m")
        ex()
      else:
        self.ssh()
        if os.path.exists(bpath+"ssh"):
          self.opens()
        else:
          self.notino()
          break

  def ssh(self):
    Mylogo()
    print("\n\033[01;32mSetting Up server......\033[00m\n")
    if system=="termux":
      os.system(pac+" update")
      os.system(pac+" install openssh -y")
    else:
      os.system(pac+" update")
      os.system(pac+" install openssh-server -y")

if system=="termux":
  openssh().opens()
else:
  if os.path.exists(bpath+"ssh"):
    openssh().opens()
  elif os.path.exists("/data/data/com.termux/files/usr/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/local/bin/lt"):
	lt().locals()
  elif os.path.exists("/usr/sbin/lt"):
	lt().locals()
  else:
    openssh().opens()