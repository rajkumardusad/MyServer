# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *
from pyweb import *
from php import *
from apache import *
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
  apache()
elif sys.argv[1]=="-py":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  pyweb()
elif sys.argv[1]=="-ng":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  nginx()
elif sys.argv[1]=="-d":
  s=open(spath+".serv.lock","w")
  s.write(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  s.close()
  if os.path.exists(bpath+"php"):
    php()
  else:
    pyweb()