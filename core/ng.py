# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 4/1/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from ux import *
from logo import *
from nginx import *

class nginx(object):
  def ng(self):
    if os.path.exists(bpath+"nginx"):
      port=sys.argv[3]
      gp=sys.argv[4]
      ngi(port,gp)
      if os.path.exists("/data/data/com.termux/files/usr/etc/nginx/nginx.conf"):
        os.system("rm -rf /data/data/com.termux/files/usr/etc/nginx/nginx.conf")
      if os.path.exists("nginx.conf"):
        os.system("cp nginx.conf /data/data/com.termux/files/usr/etc/nginx")
      os.system("nginx")
      sleep(1)
      self.ngs()
    elif os.path.exists("/usr/sbin/nginx"):
      port=sys.argv[3]
      gp=sys.argv[4]
      default(port,gp)
      if os.path.exists("/etc/nginx/sites-available/default"):
        if system=="ubuntu":
          os.system("sudo rm -rf /etc/nginx/sites-available/default")
        else:
          os.system("rm -rf /etc/nginx/sites-available/default")
      if os.path.exists("default"):
        if system=="ubuntu":
          os.system("sudo cp default /etc/nginx/sites-available")
        else:
          os.system("cp default /etc/nginx/sites-available")
      if system=="ubuntu":
        os.system("sudo systemctl start nginx")
      else:
        os.system("service nginx start")
      sleep(1)
      self.ngs()
    else:
      Mylogo()
      print("\n\n\007\033[01;31m  Error \033[01;33mNginx \033[01;31mNot installed.\033[00m")
      ex()

  def ngs(self):
    port=sys.argv[3]
    gp=sys.argv[4]
    os.system("python2 modules/.srvr.aex")
    Mylogo()
    if os.path.exists(bpath+"nginx"):
      print("\n\n\007\033[01;33m Nginx web server\033[01;32m is running .....")
      print("\033[01;33m Your Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \033[00m\n")
      stop=raw_input("\033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("nginx -s stop")
        sleep(2)
        print("\n\007\033[01;33m Nginx web server\033[01;31m stopped !! \033[00m")
      else:
        self.ngs()

    elif os.path.exists("/usr/sbin/nginx"):
      print("\n\n\007\033[01;33m Nginx web server\033[01;32m is running .....")
      print("\033[01;33m Your Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \033[00m\n")
      stop=raw_input("\033[01;33m Press \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        if system=="ubuntu":
          os.system("sudo systemctl stop nginx")
        else:
          os.system("service nginx stop")
        sleep(2)
        print("\n\007\033[01;33m Nginx web server\033[01;31m stopped !! \033[00m")
      else:
        self.ngs()