# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *

class upd(object):
  def chk_upd(self):
    while True:
      Mylogo()
      askv = input("\n\033[1;33m Do you want to Update MyServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if askv == "n" or askv == "N":
        break
      elif askv == "Y" or askv == "y":
        Mylogo()
        print("\n\033[01;32mUpdating MyServer .........\033[01;36m")
        if os.path.exists(bpath+"git"):
          print("\033[01;32mDone ....\033[01;36m")
        else:
          os.system(pac+" update")
          os.system(pac+" install git -y")
        if system=="ubuntu":
          os.system("cd "+home+" && sudo git clone https://github.com/Rajkumrdusad/MyServer.git")
        else:
          os.system("cd "+home+" && git clone https://github.com/Rajkumrdusad/MyServer.git")
        if os.path.exists(home+"MyServer"):
          os.system("cd "+home+"MyServer && sh install")
          os.system("clear")
          os.system("myserver start")
          sys.exit()
        else:
          Mylogo()
          print("\n\n\033[01;37m    [+] \033[01;31mSorry We can't update MyServer !!\033[00m")
          print("\033[01;37m    [+] \033[01;31mYou are \033[01;33moffline \033[01;31m!!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mCheck your \033[01;33mnetwork \033[01;31mconnection !!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mTry again after sometime.\033[00m\n\n")
          sleep(4)
          break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+askv+"\'")
        sleep(1)

def update():
  upd().chk_upd()
update()