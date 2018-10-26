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

class pyweb(object):
  def chkpy(self):
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
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
          os.system("cp "+home+".MyServer/modules/index.sh "+gp)
          os.system("cd "+gp+" && sh index.sh")
          os.system("cd "+gp+" && rm index.sh")
        else:
          os.system("sudo cp "+home+".MyServer/modules/index.sh "+gp)
          os.system("cd "+gp+" && sudo sh index.sh")
          os.system("cd "+gp+" && sudo rm index.sh")
      Mylogo()
      print("\n\033[01;33mStarting Server ......\033[00m\n")
      print("\n \033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \n http://127.0.0.1:"+port+"/\033[00m\n")
      os.system("cd "+gp+" && python2 -m SimpleHTTPServer "+port)
      print("\033[01;31m unfortunately server stopped\n\033[00m")
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
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
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
        os.system("cp "+home+".MyServer/modules/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
      else:
        os.system("sudo cp "+home+".MyServer/modules/index.sh "+gp)
        os.system("cd "+gp+" && sudo sh index.sh")
        os.system("cd "+gp+" && sudo rm index.sh")
    print("\n \033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \n http://127.0.0.1:"+port+"/\033[00m\n")
    os.system("cd "+gp+" && python2 -m SimpleHTTPServer "+port)
    print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

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
      print("\n\n\007\033[01;31m  Error \033[01;33mApache \033[01;31mNot installed.")
      sleep(4)
      MServer()

  def apa(self):
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
    Mylogo()
    if os.path.exists(bpath+"apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("rm -rf /data/data/com.termux/files/usr/var/run/apache2/httpd.pid")
        os.system("apachectl stop")
        sleep(4)
        MServer()
      else:
        self.apa()
    elif os.path.exists("/usr/sbin/apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("apachectl stop")
        sleep(4)
        MServer()
      else:
        self.apa()
    elif os.path.exists("/usr/sbin/apache2"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("apache2 stop")
        sleep(4)
        MServer()
      else:
        self.apa()

class Manual(object):
  def MS(self):
    while True:
      mslogo()
      Tool = raw_input(''' \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m''')
      if Tool == "1":
        php()
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
      elif Tool == "0" or Tool=="back":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
      sleep(0.7)

def MServer():
  Manual().MS()