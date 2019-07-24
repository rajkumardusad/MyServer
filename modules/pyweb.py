# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *
from modules.logo import *

class py_web(object):
  def chkpy(self):
    os.system("python modules/.srvr.aex")
    if os.path.exists(spath+".path.aex"):
      g=open(spath+".path.aex","r")
      gp=g.read()
      g.close()
      p=open(spath+".port.aex","r")
      port=p.read()
      p.close()
      h=open(spath+".host.aex","r")
      host=h.read()
      h.close()
      if gp=="":
        self.srvr()
      if port=="":
        port="8080"
      if os.path.exists(gp+"/index.html") or os.path.exists(gp+"index.html") or os.path.exists(gp+"/index.php") or os.path.exists(gp+"index.php"):
        pass
      else:
        if system=="ubuntu":
          os.system("sudo cp core/index.sh "+gp)
          os.system("cd "+gp+" && sudo sh index.sh")
          os.system("cd "+gp+" && sudo rm index.sh")
        else:
          os.system("cp core/index.sh "+gp)
          os.system("cd "+gp+" && sh index.sh")
          os.system("cd "+gp+" && rm index.sh")
      Mylogo()
      print("\n\033[01;33mStarting Server ......\033[00m\n")
      print("\033[01;33mYour Server URL is :- \033[01;36mhttp://"+host+":"+port+"/\033[00m\n")
      os.system("cd "+gp+" && python3 -m http.server "+port+" --bind "+host)
      print("\n\007\033[01;31munfortunately server stopped\n\033[00m")
      sys.exit()
    else:
      self.srvr()

  def srvr(self):
    if system=="termux":
      Mylogo()
      gp=input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /sdcard/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /sdcard/www\n")
        sleep(4)
        self.srvr()
    else:
      Mylogo()
      gp=input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /home/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /home/www\n")
        sleep(4)
        self.srvr()
    Mylogo()
    port=input("\n\n\033[01;33m  Enter your port (\033[01;36mex: 8080\033[01;33m) :- \033[01;36m")
    if port=="":
      port="8080"
    Mylogo()
    host=input("\n\n\033[01;33m  Enter your localhost ip (\033[01;36mex: localhost OR 127.0.0.1\033[01;33m) :- \033[01;36m")
    if host=="":
      host="localhost"
    Mylogo()
    sav=input("\n\n\033[01;33m  Do you wan to save this setting [\033[01;32mY/n\033[01;33m] >> \033[01;36m")
    if sav=="Y" or sav=="y":
      spat=open(spath+".path.aex","w")
      spat.write(gp)
      spat.close()
      sport=open(spath+".port.aex","w")
      sport.write(port)
      sport.close()
      shost=open(spath+".host.aex","w")
      shost.write(host)
      shost.close()
    os.system("python modules/.srvr.aex")
    Mylogo()
    print("\n\033[01;33mStarting Server ......\033[00m\n")
    if os.path.exists(gp+"/index.html") or os.path.exists(gp+"index.html") or os.path.exists(gp+"/index.php") or os.path.exists(gp+"index.php"):
      pass
    else:
      if system=="ubuntu":
        os.system("sudo cp core/index.sh "+gp)
        os.system("cd "+gp+" && sudo sh index.sh")
        os.system("cd "+gp+" && sudo rm index.sh")
      else:
        os.system("cp core/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
    print("\033[01;33mYour Server URL is :- \033[01;36mhttp://"+host+":"+port+"/\033[00m\n")
    os.system("cd "+gp+" && python3 -m http.server "+port+" --bind "+host)
    print("\n\007\033[01;31munfortunately server stopped\n\033[00m")
    sys.exit()

def pyweb():
  py_web().chkpy()
