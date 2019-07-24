# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *

class py_web(object):
  def chkpy(self):
    os.system("python modules/.srvr.aex")
    gp=sys.argv[4]
    port=sys.argv[3]
    host=sys.argv[2]
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

def pyweb():
  py_web().chkpy()
