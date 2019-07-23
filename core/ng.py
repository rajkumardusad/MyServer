# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 4/1/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from system import *
from logo import *
from nginx import *

class nginx_server(object):
  def ng(self):
    os.system("python modules/.srvr.aex")
    Mylogo()
    gp=sys.argv[4]
    port=sys.argv[3]
    host=sys.argv[2]
    if os.path.exists(gp+"/index.html"):
      pass
    elif os.path.exists(gp+"index.html"):
      pass
    elif os.path.exists(gp+"/index.py"):
      pass
    elif os.path.exists(gp+"index.py"):
      pass
    elif os.path.exists(gp+"/index.php"):
      pass
    elif os.path.exists(gp+"index.php"):
      pass
    elif os.path.exists(gp+"/index.pl"):
      pass
    elif os.path.exists(gp+"index.pl"):
      pass
    elif os.path.exists(gp+"/index.jsp"):
      pass
    elif os.path.exists(gp+"index.jsp"):
      pass
    else:
      if system=="ubuntu":
        os.system("sudo cp modules/index.sh "+gp)
        os.system("cd "+gp+" && sudo sh index.sh")
        os.system("cd "+gp+" && sudo rm index.sh")
      else:
        os.system("cp modules/index.sh "+gp)
        os.system("cd "+gp+" && sh index.sh")
        os.system("cd "+gp+" && rm index.sh")
    if os.path.exists(bpath+"nginx"):
      ngi(port,gp,host)
      if os.path.exists("nginx.conf") and os.path.exists("/data/data/com.termux/files/usr/etc/nginx/nginx.conf"):
        os.system("rm -rf /data/data/com.termux/files/usr/etc/nginx/nginx.conf")
        os.system("cp nginx.conf /data/data/com.termux/files/usr/etc/nginx")
      os.system("nginx")
      print("\n\n\007\033[01;33mNginx web server\033[01;32m is running .....")
      print("\033[01;33mYour Server URL is :- \033[01;36mhttp://"+host+":"+port+"/ \033[00m\n")
      stop=input("\033[01;33mPress \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
      if stop=="0":
        os.system("nginx -s stop")
        sleep(2)
        print("\n\007\033[01;33mNginx web server\033[01;31m stopped !! \033[00m")
        sys.exit()

    elif os.path.exists("/usr/sbin/nginx"):
      if system=="ubuntu":
        default(port,gp)
        if os.path.exists("default") and os.path.exists("/etc/nginx/sites-available/default"):
          os.system("sudo rm -rf /etc/nginx/sites-available/default")
          os.system("sudo cp default /etc/nginx/sites-available")
        os.system("sudo systemctl start nginx")
        print("\n\n\007\033[01;33mNginx web server\033[01;32m is running .....")
        print("\033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \033[00m\n")
        stop=input("\033[01;33mPress \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
        if stop=="0":
          os.system("sudo systemctl stop nginx")
          sleep(2)
          print("\n\007\033[01;33mNginx web server\033[01;31m stopped !! \033[00m")
          sys.exit()

    else:
      default(port,gp)
      if os.path.exists("default") and os.path.exists("/etc/nginx/sites-available/default"):
        os.system("rm -rf /etc/nginx/sites-available/default")
        os.system("cp default /etc/nginx/sites-available")
        os.system("service nginx start")
        print("\n\n\007\033[01;33mNginx web server\033[01;32m is running .....")
        print("\033[01;33mYour Server URL is :- \033[01;36mhttp://localhost:"+port+"/ \033[00m\n")
        stop=input("\033[01;33mPress \033[01;36m0\033[01;33m to stop server >>\033[01;36m ");
        if stop=="0":
          os.system("service nginx stop")
          sleep(2)
          print("\n\007\033[01;33mNginx web server\033[01;31m stopped !! \033[00m")
          sys.exit()

def nginx():
  if os.path.exists(bpath+"nginx") or os.path.exists("/usr/sbin/nginx"):
    nginx_server().ng()
  else:
    Mylogo()
    print("\n\n\033[01;31m   [\033[01;33m+\033[01;31m] \033[01;36mNginx Server \033[01;31mis not installed in your "+system+".")
    opt=input("\n\033[01;33m Do you want to install Nginx Server [\033[01;32mY/n\033[01;33m] >>\033[00m ")
    if opt=="y" or opt=="Y":
      Mylogo()
      print("\n\033[01;33minstalling Nginx Server ......\033[00m\n")
      sleep(1)
      os.system(pac+" update")
      os.system(pac+" install nginx -y")
      if os.path.exists(bpath+"nginx") or os.path.exists("/usr/sbin/nginx"):
        nginx_server().ng()
      else:
        Mylogo()
        print("\n\n\033[01;31m  Sorry we can't install \033[01;33mNginx Server\033[01;31m in your "+system+".\033[00m")
        sleep(3)