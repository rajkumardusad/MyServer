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
from py import *
from php import *
from apa import *
from ng import *

if sys.argv[1]=="-php":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  php()
elif sys.argv[1]=="-apa":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1])
  s.close()
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
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  pyweb().srvr()
elif sys.argv[1]=="-ng":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  if os.path.exists(bpath+"nginx"):
    nginx().ng()
  elif os.path.exists("/usr/sbin/nginx"):
    nginx().ng()
  else:
    Mylogo()
    print("\n\033[01;33minstalling Nginx web server .........\033[00m\n")
    os.system(pac+" update")
    os.system(pac+" install nginx -y")
    nginx().ng()
elif sys.argv[1]=="-d":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  if os.path.exists(bpath+"php"):
    php()
  else:
    pyweb().srvr()
