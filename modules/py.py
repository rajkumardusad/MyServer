# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 4/1/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from ux import *
from logo import *

class pyweb(object):
  def chkpy(self):
    os.system("python2 modules/.srvr.aex")
    if os.path.exists(spath+".path.aex"):
      g=open(spath+".path.aex","r")
      gp=g.read()
      g.close()
      p=open(spath+".port.aex","r")
      port=p.read()
      p.close()
      if gp=="":
        self.srvr()
      if port=="":
        port="8080"
      if os.path.exists(gp+"/index.html"):
        pass
      elif os.path.exists(gp+"index.html"):
        pass
      elif os.path.exists(gp+"/index.py"):
        pass
      elif os.path.exists(gp+"index.py"):
        pass
      else:
        if system=="termux":
          os.system("cp modules/index.sh "+gp)
          os.system("cd "+gp+" && sh index.sh")
          os.system("cd "+gp+" && rm index.sh")
        elif system=="ubuntu":
          os.system("sudo cp modules/index.sh "+gp)
          os.system("cd "+gp+" && sudo sh index.sh")
          os.system("cd "+gp+" && sudo rm index.sh")
        else:
          os.system("cp modules/index.sh "+gp)
          os.system("cd "+gp+" && sh index.sh")
          os.system("cd "+gp+" && rm index.sh")
      Mylogo()
      print("\n\033[01;33mStarting Server ......\033[00m\n")
      print("\033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \n http://127.0.0.1:"+port+"/\033[00m\n")
      os.system("cd "+gp+" && python2 -m SimpleHTTPServer "+port)
      print("\007\033[01;31munfortunately server stopped\n\033[00m")
      ex()
    else:
      self.srvr()

  def srvr(self):
    if system=="termux":
      Mylogo()
      gp=raw_input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /sdcard/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /sdcard/www\n")
        sleep(4)
        self.srvr()
    else:
      Mylogo()
      gp=raw_input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /home/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error Document Root path is invalid please enter path for an \033[01;33mexample\033[01;32m /home/www\n")
        sleep(4)
        self.srvr()
    Mylogo()
    port=raw_input("\n\n\033[01;33m  Enter your port (\033[01;36mex: 8080\033[01;33m) :- \033[01;36m")
    if port=="":
      port="8080"
    Mylogo()
    sav=raw_input("\n\n\033[01;33m  Do you wan to save this setting [\033[01;32mY/n\033[01;33m] >> \033[01;36m")
    if sav=="Y" or sav=="y":
      spat=open(spath+".path.aex","w")
      spat.write(gp)
      spat.close()
      sport=open(spath+".port.aex","w")
      sport.write(port)
      sport.close()
      shost=open(spath+".host.aex","w")
      shost.write("localhost")
      shost.close()
    os.system("python2 modules/.srvr.aex")
    Mylogo()
    print("\n\033[01;33mStarting Server ......\033[00m\n")
    if os.path.exists(gp+"/index.html"):
      pass
    elif os.path.exists(gp+"index.html"):
      pass
    elif os.path.exists(gp+"/index.py"):
      pass
    elif os.path.exists(gp+"index.py"):
      pass
    else:
      if system=="termux":
        os.system("cp modules/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
      elif system=="ubuntu":
        os.system("sudo cp modules/index.sh "+gp)
        os.system("cd "+gp+" && sudo sh index.sh")
        os.system("cd "+gp+" && sudo rm index.sh")
      else:
        os.system("cp modules/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
    print("\033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \n http://127.0.0.1:"+port+"/\033[00m\n")
    os.system("cd "+gp+" && python2 -m SimpleHTTPServer "+port)
    print("\007\033[01;31munfortunately server stopped\n\033[00m")
    ex()