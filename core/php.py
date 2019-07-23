# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *

class phpserver(object):
  def chphp(self):
    if os.path.exists(bpath+"php"):
      self.chkp()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;33mPHP\033[01;31m in your "+system+".\033[00m")
      sleep(3)

  def chkp(self):
    getpat=sys.argv[4]
    getp=sys.argv[3]
    host=sys.argv[2]
    os.system("python modules/.srvr.aex")
    Mylogo()
    print("\n\033[01;33mStarting Server ......\033[00m\n")
    if os.path.exists(getpat+"/index.html") or os.path.exists(getpat+"index.html") or os.path.exists(getpat+"/index.php") or os.path.exists(getpat+"index.php"):
      pass
    else:
      if system=="ubuntu":
        os.system("sudo cp core/index.sh "+getpat)
        os.system("cd "+getpat+" && sudo sh index.sh")
        os.system("cd "+getpat+" && sudo rm index.sh")
      else:
        os.system("cp core/index.sh "+getpat)
        os.system("cd "+getpat+" && sh index.sh")
        os.system("cd "+getpat+" && rm index.sh")
    os.system("php -S "+host+":"+getp+" -t "+getpat)
    print("\n\007\033[01;31m unfortunately server stopped\n\033[00m")
    sys.exit()

def inphp():
  if system=="termux":
    os.system(pac+" update")
    os.system(pac+" install php -y")
    os.system(pac+" install php-mysqli -y")
  else:
    os.system(pac+" update")
    os.system(pac+" install php -y")
    os.system(pac+" install php5 -y")
    os.system(pac+" install php5-mysql -y")
    os.system(pac+" install php5-mysqli -y")

def php():
  if os.path.exists(bpath+"php"):
    phpserver().chkp()
  else:
    Mylogo()
    print("\n\n\033[01;31m   [\033[01;33m+\033[01;31m] \033[01;36mPHP \033[01;31mis not installed in your "+system+".")
    opt=input("\n\033[01;33m Do you want to install PHP [\033[01;32mY/n\033[01;33m] >>\033[00m")
    if opt=="y" or opt=="Y":
      Mylogo()
      print("\n\033[01;33minstalling PHP ......\033[00m\n")
      sleep(1)
      inphp()
      phpserver().chphp()