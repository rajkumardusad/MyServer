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

if sys.argv[1]=="-s":
  s=open(spath+".serv.lock","r")
  sr=s.read()
  s.close()
  os.system("python2 ~/.MyServer/core/server.py "+sr)
elif sys.argv[1]=="-h":
  s=open(spath+".h.lock","r")
  sr=s.read()
  s.close()
  os.system("python2 ~/.MyServer/core/host.py "+sr)
