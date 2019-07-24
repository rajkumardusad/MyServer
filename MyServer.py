# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 13/11/2018 - 22/July/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *

if len(sys.argv)>1:
  pass
else:
  print ("error : invalid arguments !!")
  print ("use : myserver --help  for more information")
  sys.exit()

if sys.argv[1]=="-s":

  if len(sys.argv)==2:
    if system=="ubuntu":
      os.system("sudo python3 core/s.py "+sys.argv[1])
    else:
      os.system("python3 core/s.py "+sys.argv[1])

  elif len(sys.argv)==3:
    if sys.argv[2]=="apache":
      if system=="ubuntu":
        os.system("sudo python3 core/server.py -apa")
      else:
        os.system("python3 core/server.py -apa")
    else:
      print ("error : invalid arguments !!")
      print ("use : myserver --help  for more information")

  elif len(sys.argv)==6:
    if sys.argv[2]=="-php":
      if system=="ubuntu":
        os.system("sudo python3 core/server.py -php "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
      else:
        os.system("python3 core/server.py -php "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
    elif sys.argv[2]=="-py":
      if system=="ubuntu":
        os.system("sudo python3 core/server.py -py "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
      else:
        os.system("python3 core/server.py -py "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
    elif sys.argv[2]=="-ng":
      if system=="ubuntu":
        os.system("sudo python3 core/server.py -ng "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
      else:
        os.system("python3 core/server.py -ng "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5])
    else:
      print ("error : invalid arguments !!")
      print ("use : myserver --help  for more information")

  elif len(sys.argv)==5:
    if system=="ubuntu":
      os.system("sudo python3 core/server.py -d "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
    else:
      os.system("python3 core/server.py -d "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
  else:
    print ("error : invalid arguments !!")
    print ("use : myserver --help  for more information")

elif sys.argv[1]=="-h":
  if len(sys.argv)==2:
    if system=="ubuntu":
      os.system("sudo python3 core/s.py "+sys.argv[1])
    else:
      os.system("python3 core/s.py "+sys.argv[1])

  elif len(sys.argv)==5:
    if system=="ubuntu":
      os.system("sudo python3 core/host.py "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
    else:
      os.system("python3 core/host.py "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])

  else:
    print ("error : invalid arguments")
    print ("use : myserver --help  for more information")

elif sys.argv[1]=="-db":
  if len(sys.argv)==3:
    if sys.argv[2]=="start":
      if system=="ubuntu":
        os.system("sudo python3 core/mysql.py "+sys.argv[2])
      else:
        os.system("python3 core/mysql.py "+sys.argv[2])
    elif sys.argv[2]=="stop":
      if system=="ubuntu":
        os.system("sudo python3 core/mysql.py "+sys.argv[2])
      else:
        os.system("python3 core/mysql.py "+sys.argv[2])
    else:
      print ("error : invalid arguments !!")
      print ("use : myserver --help  for more information")
  else:
    print ("error : invalid arguments !!")
    print ("use : myserver --help  for more information")

elif sys.argv[1]=="rm":
  if len(sys.argv)==3:
    if sys.argv[2]=="-T" or sys.argv[2]=="-t":
      if system=="ubuntu":
        os.system("sudo python3 core/un.py")
      else:
        os.system("python3 core/un.py")
    else:
      print ("error : invalid arguments")
      print ("use : myserver --help  for more information")
  else:
    print ("error : invalid arguments")
    print ("use : myserver --help  for more information")

elif sys.argv[1]=="update":
  if system=="ubuntu":
    os.system("sudo python3 core/upd.py")
  else:
    os.system("python3 core/upd.py")

elif sys.argv[1]=="start":
  if system=="ubuntu":
    os.system("sudo python3 .MyServer.py")
  else:
     os.system("python3 .MyServer.py")

elif sys.argv[1]=="--help" or sys.argv[1]=="-help" or sys.argv[1]=="help":
  print ("")
  print ("Usage: myserver [command]... [arguments]...")
  print ("")
  print (" Commands:")
  print (" -s <hostname> <port> <path>            to start default localhost server.")
  print (" -s -ng <hostname> <port> <path>        to start php localhost server.")
  print (" -s -php <hostname> <port> <path>       to start php localhost server.")
  print (" -s -py <hostname> <port> <path>        to start python localhost server.")
  print (" -h <hostname> <localhost_port> <port>  to access localhost server on internet.")
  print (" -db [start/stop]                       to start/stop MySQL database server.")
  print (" -s apache                              to start apache web server.")
  print (" update                                 update MyServer.")
  print (" rm -t                                  uninstall MyServer.")
  print (" start                                  start MyServer menu.")
  print ("")

else:
  print ("error : invalid arguments !!")
  print ("use : myserver --help  for more information")
