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

class MySQL(object):
  def chmys(self):
    if os.path.exists(bpath+"mysql"):
      os.system("python2 ~/.MyServer/modules/.srvr.aex")
      self.mysqls()
    else:
      Mylogo()
      print("\n\n\033[01;31m  Sorry we can't install \033[01;32mMySQL \033[01;31min your "+system+".")
      sleep(4)

  def mysqls(self):
    Mylogo()
    usrnm=raw_input("\n\n\033[01;33m Enter your MySQL username :- \033[01;36m")
    if usrnm=="":
      print("\n\033[01;31m\007 Error Please enter your \033[01;33mMySQL username\033[01;31m !!\n")
      self.mysqls()
    os.system("python2 ~/.MyServer/modules/.srvr.aex")
    Mylogo()
    print("\n\033[01;33mStarting Server ......\033[00m\n")
    if os.path.exists("/usr/lib/sudo"):
      os.system("sudo service mysql start")
      os.system("sudo mysql -u "+usrnm+" -p")
      print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    elif system=="ubuntu":
      os.system("sudo systemctl mysql start")
      os.system("sudo mysql -u "+usrnm+" -p")
      print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    else:
      os.system("service mysql start")
      os.system("mysql -u "+usrnm+" -p")
      print("\n\033[01;31m unfortunately server stopped\n\033[00m")
    ex()

  def inmys(self):
    if os.path.exists(bpath+"mysql"):
      os.system("python2 ~/.MyServer/modules/.srvr.aex")
      self.mysqls()
    else:
      Mylogo()
      print("\n\n\033[01;31m   [\033[01;33m+\033[01;31m] \033[01;36mMySQL \033[01;31mis not installed in your "+system+".")
      opt=raw_input("\n\033[01;33m Do you want to install MySQL [\033[01;32mY/n\033[01;33m] >>\033[01;36m ")
      if opt=="Y" or opt=="y":
        Mylogo()
        print("\n\033[01;33mInstalling MySQL Server......\n\033[00m")
        os.system(pac+" update")
        os.system(pac+" install mysql-server -y")
        if system=="ubuntu":
          os.system("sudo mysql_secure_installation")
        os.system("mysql_secure_installation")
        self.chmys()
      elif opt=="N" or opt=="n":
        pass
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
        sleep(1)
        self.inmys()
  
def Mys():
  MySQL().inmys()