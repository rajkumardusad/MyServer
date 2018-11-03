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

class pyweb(object):
  def srvr(self):
    port=sys.argv[3]
    gp=sys.argv[4]
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
      elif system=="ubuntu":
        os.system("sudo cp "+home+".MyServer/modules/index.sh "+gp)
        os.system("cd "+gp+" && sudo sh index.sh")
        os.system("cd "+gp+" && sudo rm index.sh")
      else:
        os.system("cp "+home+".MyServer/modules/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
    print("\033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \n http://127.0.0.1:"+port+"/\033[00m\n")
    os.system("cd "+gp+" && python2 -m SimpleHTTPServer "+port)
    print("\n\007\033[01;31munfortunately server stopped\n\033[00m")
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
      print("\n\n\007\033[01;31m  Error \033[01;33mApache \033[01;31mNot installed.\033[00m")
      ex()

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
      else:
        self.apa()

    elif os.path.exists("/usr/sbin/apachectl"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[00m ");
      if stop=="0":
        os.system("apachectl stop")
        sleep(4)
      else:
        self.apa()

    elif os.path.exists("/usr/sbin/apache2"):
      print("\n\n \007\033[01;33m Apache web server\033[01;32m is running .....")
      stop=raw_input(" \033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[00m ");
      if stop=="0":
        os.system("apache2 stop")
        sleep(4)
      else:
        self.apa()

class phpserver(object):
  def chphp(self):
    if os.path.exists(bpath+"php"):
      self.phps()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;33mPHP\033[01;31m in your "+system+".\033[00m")
      sleep(3)

  def phps(self):
    hostn=sys.argv[2]
    port=sys.argv[3]
    pat=sys.argv[4]
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
      elif system=="ubuntu":
        os.system("sudo cp "+home+".MyServer/modules/index.sh "+pat)
        os.system("cd "+pat+" && sudo sh index.sh")
        os.system("cd "+pat+" && sudo rm index.sh")
      else:
        os.system("cp "+home+".MyServer/modules/index.sh "+pat)
        os.system("cd "+pat+" && sh index.sh")
        os.system("cd "+pat+" && rm index.sh")
    os.system("php -S "+hostn+":"+port+" -t "+pat)
    print("\n\007\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

def inphp():
  if system=="termux":
    os.system(pac+" update")
    os.system(pac+" install php -y")
  else:
    os.system(pac+" update")
    os.system(pac+" install php -y")
    os.system(pac+" install php5 -y")
    os.system(pac+" install php5-mysql -y")

def php():
  if os.path.exists(bpath+"php"):
    phpserver().chphp()
  else:
    Mylogo()
    print("\n\033[01;33mSetting Up ......\033[00m\n")
    sleep(1)
    inphp()
    phpserver().chphp()

if sys.argv[1]=="-php":
  php()
elif sys.argv[1]=="-apa":
  if os.path.exists(bpath+"apachectl"):
    apache().asr()
  elif os.path.exists("/usr/sbin/apache2"):
    apache().asr()
  else:
    Mylogo()
    print("\n\033[01;33minstalling Apache2 web server .........\033[00m\n")
    os.system(pac+" update")
    os.system(pac+" install apache2 -y")
    apache().asr()
elif sys.argv[1]=="-py":
  pyweb().srvr()
elif sys.argv[1]=="-d":
  if os.path.exists(bpath+"php"):
    php()
  else:
    pyweb().srvr()
