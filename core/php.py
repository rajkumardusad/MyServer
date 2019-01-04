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
      self.phps()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;33mPHP\033[01;31m in your "+system+".\033[00m")
      sleep(3)

  def phps(self):
    hostn=sys.argv[2]
    port=sys.argv[3]
    pat=sys.argv[4]
    os.system("python2 modules/.srvr.aex")
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
        os.system("cp modules/index.sh "+pat)
        os.system("cd "+pat+" && sh index.sh")
        os.system("cd "+pat+" && rm index.sh")
      elif system=="ubuntu":
        os.system("sudo cp modules/index.sh "+pat)
        os.system("cd "+pat+" && sudo sh index.sh")
        os.system("cd "+pat+" && sudo rm index.sh")
      else:
        os.system("cp modules/index.sh "+pat)
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