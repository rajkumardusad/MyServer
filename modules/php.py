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

class phpserver(object):
  def chphp(self):
    if os.path.exists(bpath+"php"):
      self.chkp()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;33mPHP\033[01;31m in your "+system+".")
      sleep(3)

  def chkp(self):
    if os.path.exists(spath+".path.aex"):
      g=open(spath+".path.aex","r")
      getpat=g.read()
      g.close()
      p=open(spath+".port.aex","r")
      getp=p.read()
      p.close()
      h=open(spath+".host.aex","r")
      host=h.read()
      h.close()
      if getpat=="":
        self.phps()     
      if getp=="":
        getp="8080"
      if host=="":
        host="localhost"
      os.system("python2 ~/.MyServer/modules/.srvr.aex")
      Mylogo()
      print("\n\033[01;33mStarting Server ......\033[00m\n")
      if os.path.exists(getpat+"/index.html"):
        pass
      elif os.path.exists(getpat+"index.html"):
        pass
      elif os.path.exists(getpat+"/index.php"):
        pass
      elif os.path.exists(getpat+"index.php"):
        pass
      else:
        if system=="termux":
          os.system("cp "+home+".MyServer/modules/index.sh "+getpat)
          os.system("cd "+getpat+" && sh index.sh")
          os.system("cd "+getpat+" && rm index.sh")
        else:
          os.system("sudo cp "+home+".MyServer/modules/index.sh "+getpat)
          os.system("cd "+getpat+" && sudo sh index.sh")
          os.system("cd "+getpat+" && sudo rm index.sh")
      os.system("php -S "+host+":"+getp+" -t "+getpat)
      print("\033[01;31m unfortunately server stopped\n\033[00m")
      ex()
    else:
      self.phps()

  def phps(self):
    if system=="termux":
      Mylogo()
      getpat=raw_input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /sdcard/www\033[01;33m) :- \033[01;36m")
      if getpat=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /sdcard/www\n")
        sleep(4)
        self.phps()
    else:
      Mylogo()
      getpat=raw_input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /home/www\033[01;33m) :- \033[01;36m")
      if getpat=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /home/www\n")
        sleep(4)
        self.phps()
    Mylogo()
    getp=raw_input("\n\n\033[01;33m  Enter your port (\033[01;36mex: 8080\033[01;33m) :- \033[01;36m")
    if getp=="":
      getp="8080"
    Mylogo()
    host=raw_input("\n\n\033[01;33m  Enter your localhost ip (\033[01;36mex: localhost OR 127.0.0.1\033[01;33m) :- \033[01;36m")
    if host=="":
      host="localhost"
    Mylogo()
    hostn=host
    pat=getpat
    port=getp
    sav=raw_input("\n\n\033[01;33m  Do you wan to save this setting [\033[01;32mY/n\033[01;33m] >> \033[01;36m")
    if sav=="Y" or sav=="y":
      spat=open(spath+".path.aex","w")
      spat.write(pat)
      spat.close()
      sport=open(spath+".port.aex","w")
      sport.write(port)
      sport.close()
      shost=open(spath+".host.aex","w")
      shost.write(hostn)
      shost.close()
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
    Mylogo()
    print("\n\033[01;33mStarting Server ......\033[00m\n")
    if os.path.exists(pat+"/index.html"):
      pass
    elif os.path.exists(pat+"index.html"):
      pass
    elif os.path.exists(pat+"/index.php"):
      pass
    elif os.path.exists(pat+"index.php"):
      pass
    else:
      if system=="termux":
        os.system("cp "+home+".MyServer/modules/index.sh "+pat)
        os.system("cd "+pat+" && sh index.sh")
        os.system("cd "+pat+" && rm index.sh")
      else:
        os.system("sudo cp "+home+".MyServer/modules/index.sh "+pat)
        os.system("cd "+pat+" && sudo sh index.sh")
        os.system("cd "+pat+" && sudo rm index.sh")
    os.system("php -S "+hostn+":"+port+" -t "+pat)
    print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

def inphp():
  if system=="termux":
    os.system(pac+" update")
    os.system(pac+" install php -y")
  else:
    os.system(pac+" update")
    os.system(pac+" install php -y")
    os.system(pac+" install php5 -y")

def php():
  if os.path.exists(bpath+"php"):
    phpserver().chphp()
  else:
    Mylogo()
    print("\n\033[01;33minstalling PHP ......\033[00m\n")
    sleep(1)
    inphp()
    phpserver().chphp()
