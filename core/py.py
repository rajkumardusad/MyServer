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
    print("\n\007\033[01;31munfortunately server stopped\n\033[00m")
    ex()