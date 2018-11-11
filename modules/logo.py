# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import os
import sys
from time import sleep
from system import *

def Slogo():
  if system=="termux":
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mView Server setting.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mChange Server setting.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')
  else:
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mView Server setting.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mChange Server setting.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')


def mslogo():
  if system=="termux":
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart default server.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mStart PHP web server.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mStart Python web server.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mStart Apache web server.
\033[1;32m   [\033[1;31m 5 \033[1;32m] \033[1;33mStart Nginx web server.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')
  else:
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart default server.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mStart PHP web server.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mStart Python web server.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mStart Apache web server.
\033[1;32m   [\033[1;31m 5 \033[1;32m] \033[1;33mStart Nginx web server.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')

def mhlogo():
  if system=="termux":
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart default host.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mUse SSH tunnel.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mUse Ngrok.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mUse localtunnel.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')
  else:
    sleep(0.2)
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart default host.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mUse SSH tunnel.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mUse Ngrok.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mUse localtunnel.
\033[1;32m   [\033[1;31m 0 \033[1;32m] \033[1;33mBack.\n''')

def Mylogo():
  if system=="termux":
    os.system("clear")
    print ('''\007


\033[01;32m
    __  __       ____
   |  \/  |_   _/ ___|  ___ _ \033[01;31m____   _____ \033[01;32m_ __
   | |\/| | | | \___ \ / _ \ '__\033[01;31m\ \ / / \033[01;32m_ \ '__|
   | |  | | |_| |___) |  __/ |   \033[01;31m\ V / \033[01;32m __/ |
   |_|  |_|\__, |____/ \___|_|    \033[01;31m\_/ \033[01;32m\___|_|
           |___/
\033[00m

    }\033[01;31m---------------------------------------\033[00m{
}\033[01;31m--------------> \033[01;32mYOUR OWN SERVER \033[01;31m<--------------\033[00m{
    }\033[01;31m---------------------------------------\033[00m{''')
  else:
    os.system("clear")
    print ('''\007


\033[01;32m
       __  __       ____
      |  \/  |_   _/ ___|  ___ _ \033[01;31m____   _____ \033[01;32m_ __
      | |\/| | | | \___ \ / _ \ '__\033[01;31m\ \ / / \033[01;32m_ \ '__|
      | |  | | |_| |___) |  __/ |   \033[01;31m\ V / \033[01;32m __/ |
      |_|  |_|\__, |____/ \___|_|    \033[01;31m\_/ \033[01;32m\___|_|
              |___/
\033[00m
     }\033[01;31m-------------------------------------------\033[00m{
 }\033[01;31m----------------> \033[01;32mYOUR OWN SERVER \033[01;31m<----------------\033[00m{
     }\033[01;31m-------------------------------------------\033[00m{''')


def logo():
  if system=="termux":
    os.system("clear")
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart Server.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mAccess from internet.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mStart Database server.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mManually start server.
\033[1;32m   [\033[1;31m 5 \033[1;32m] \033[1;33mManually host server.
\033[1;32m   [\033[1;31m 6 \033[1;32m] \033[1;33mUpdate MyServer.
\033[1;32m   [\033[1;31m 7 \033[1;32m] \033[1;33mServer setting.
\033[1;32m   [\033[1;31m 8 \033[1;32m] \033[1;33mAbout us.
\033[1;32m   [\033[1;31m x \033[1;32m] \033[1;33mExit.\n''')
  else:
    os.system("clear")
    Mylogo()
    print('''
\033[1;32m   [\033[1;31m 1 \033[1;32m] \033[1;33mStart Server.
\033[1;32m   [\033[1;31m 2 \033[1;32m] \033[1;33mAccess from internet.
\033[1;32m   [\033[1;31m 3 \033[1;32m] \033[1;33mStart Database server.
\033[1;32m   [\033[1;31m 4 \033[1;32m] \033[1;33mManually start server.
\033[1;32m   [\033[1;31m 5 \033[1;32m] \033[1;33mManually host server.
\033[1;32m   [\033[1;31m 6 \033[1;32m] \033[1;33mUpdate MyServer.
\033[1;32m   [\033[1;31m 7 \033[1;32m] \033[1;33mServer setting.
\033[1;32m   [\033[1;31m 8 \033[1;32m] \033[1;33mAbout us.
\033[1;32m   [\033[1;31m x \033[1;32m] \033[1;33mExit.\n''')

def ab():
  if system=="termux":
    Mylogo()
    print('''
      \033[1;36m Tool Name   :-     \033[0;33mMyServer
      \033[1;36m Author      :-     \033[0;33mRajkumar Dusad
      \033[1;36m Powered By  :-     \033[0;33mAex Software's

\033[1;33m MyServer :- \033[0;32mMyServer is your own localhost
 server. you can setup PHP, Apache web servers
 on your android or linux like Ubuntu etc.
 it is Developed for android Termux or GNURoot.
 You can setup your localhost server and access
 from internet. you can host your website.\033[1;m
''')
  else:
    Mylogo()
    print('''
          \033[1;36m Tool Name   :-     \033[0;33mMyServer
          \033[1;36m Author      :-     \033[0;33mRajkumar Dusad
          \033[1;36m Powered By  :-     \033[0;33mAex Software's

\033[1;33m MyServer :- \033[0;32mMyServer is your own localhost server.
 you can setup PHP, Apache web servers on your android
 or linux like Ubuntu etc. it is Developed for android
 Termux or GNURoot. You can setup your localhost server
 and access from internet. you can host your website.\033[1;m
''')

def notin():
  if system=="termux":
    Mylogo()
    print('''\n\033[01;33m     [\033[1;31m + \033[1;33m] \033[1;31mSorry MyServer is not installed.
\033[1;33m     [\033[1;31m + \033[1;33m] \033[1;31mPress Y to install MyServer.
''')
  else:
    Mylogo()
    print('''\n\033[01;33m     [\033[1;31m + \033[1;33m] \033[1;31mSorry MyServer is not installed.
\033[1;33m     [\033[1;31m + \033[1;33m] \033[1;31mPress Y to install MyServer.
''')
