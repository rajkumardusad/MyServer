# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 23/5/2018
# Powered By :- Aex Software's

import sys
import os

if os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
  pac="pkg"
  home=os.getenv("HOME")+"/"
  bpath="/data/data/com.termux/files/usr/bin/"
  spath=os.getenv("HOME")+"/"
  system="termux"
elif os.path.exists("/usr/bin/apt"):
  if os.path.exists("/usr/lib/sudo"):
      home=os.getenv("HOME")+"/"
      pac="sudo apt-get"
      bpath="/usr/bin/"
      spath=os.getenv("HOME")+"/"
      system="ubuntu"
  else:
      home=os.getenv("HOME")+"/"
      pac="apt-get"
      bpath="/usr/bin/"
      spath=os.getenv("HOME")+"/"
      system="debian"
elif os.path.exists("/bin/apt"):
  if os.path.exists("/usr/lib/sudo"):
      home=os.getenv("HOME")+"/"
      pac="sudo apt-get"
      bpath="/usr/bin/"
      spath=os.getenv("HOME")+"/"
      system="ubuntu"
  else:
      home=os.getenv("HOME")+"/"
      pac="apt-get"
      bpath="/usr/bin/"
      spath=os.getenv("HOME")+"/"
      system="debian"
