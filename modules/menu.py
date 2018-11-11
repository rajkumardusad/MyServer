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
from php import *
from open import *
from local import *
from Mhost import Mhost
from MServer import *
from Mys import Mys
from sett import setting

class know(object):
  def About(self):
	while True:
		ab()
		back = raw_input(''' \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m''')
		if back == "" or back == "back" or back == "Back" or back == "0":
			menu()
		else:
			print("\n \033[01;31m\007Command not found :\033[01;32m \'"+back+"\'")
			sleep(1)

class Un(object):
  def Uni(self):
	while True:
		ask = raw_input('''\n\033[1;33m Do you want to uninstall MyServer [\033[01;32mY/n\033[01;33m] >> \033[1;36m''')
		if ask == "n" or ask == "N":
			break
		elif ask == "Y" or ask == "y":
			os.system("rm -rf "+bpath+"myserver && rm -rf ~/.MyServer")
			os.system("cd ~/ && rm -rf MyServer")
			os.system("cd "+spath+" && rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
			if system=="ubuntu":
			  os.system("cd ~/ && sudo rm -rf MyServer")
			  os.system("sudo rm -rf /usr/bin/myserver && sudo rm -rf ~/.MyServer")
			  os.system("cd "+spath+" && sudo rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
			exit()
		else:
			print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ask+"\'")
			sleep(1)

class Upd(object):
  def U(self):
	while True:
		Mylogo()
		askv = raw_input('''\n\033[1;33m Do you want to Update MyServer [\033[01;32mY/n\033[01;33m] >> \033[1;36m''')
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
			  Mylogo()
			  sleep(1)
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
			  main().OPT()
			  break
		else:
			print("\n \033[01;31m\007Command not found :\033[01;32m \'"+askv+"\'")
			sleep(1)

class main(object):
  def OPT(self):
    while True:
      logo()
      Tool = raw_input(''' \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m''')
      if Tool == "1":
        if os.path.exists(bpath+"php"):
          php()
        else:
          pyweb().chkpy()
      elif Tool == "2":
        if system=="termux":
          open()
        elif system=="ubuntu" or system=="debian":
		    local()
      elif Tool == "3":
        if system=="termux":
		    print("\033[01;31m\n\n\007  Sorry \033[01;32mMySQL\033[01;31m is not support in your system.\n")
		    sleep(4)
        elif system=="ubuntu" or system=="debian":
		    Mys()
      elif Tool == "4":
        MServer()
      elif Tool == "5":
        Mhost()
      elif Tool == "6":
        Upd().U()
      elif Tool == "7":
        setting()
      elif Tool == "8":
        know().About()
      elif Tool == "Uninstall MyServer" or Tool == "uninstall myserver" or Tool == "rm -T":
        Un().Uni()
        sleep(1)
        ex()
      elif Tool == "exit":
        exit()
      elif Tool == "x":
        Toolo = raw_input("\n\033[1;32m Do you want to Exit ? [\033[01;33mY/n\033[01;32m] >>  \033[01;36m")
        if Toolo == "N" or Toolo == "n":
          pass
        elif Toolo == "Y" or Toolo == "y":
          exit()
        else:
          print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Toolo+"\'")
          sleep(1)
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+Tool+"\'")
        sleep(1)

def menu():
  main().OPT()