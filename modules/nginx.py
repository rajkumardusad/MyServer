# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 4/1/2019
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *
from modules.logo import *
from core.nginx import *

class nginx_server(object):
  def ng(self):
    os.system("python modules/.srvr.aex")
    Mylogo()
    if os.path.exists(spath+".path.aex"):
      g=open(spath+".path.aex","r")
      gp=g.read()
      g.close()
      p=open(spath+".port.aex","r")
      port=p.read()
      p.close()
      h=open(spath+".host.aex","r")
      host=h.read()
      h.close()
      if gp=="":
        self.srvr()
      if port=="":
        port="8080"
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
    else:
      self.srvr()

  def srvr(self):
    if system=="termux":
      Mylogo()
      gp=input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /sdcard/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error invalid Document Root please enter path for an \033[01;33mexample\033[01;32m /sdcard/www\n")
        sleep(4)
        self.srvr()
    else:
      Mylogo()
      gp=input("\n\n\033[01;33m  Enter your web path (\033[01;36mex: /home/www\033[01;33m) :- \033[01;36m")
      if gp=="":
        print("\n\007\033[01;31m Error invalid Document Root please enter path for an \033[01;33mexample\033[01;32m /sdcard/www\n")
        sleep(4)
        self.srvr()
    Mylogo()
    port=raw_input("\n\n\033[01;33m  Enter your port (\033[01;36mex: 8080\033[01;33m) :- \033[01;36m")
    if port=="":
      port="8080"
    Mylogo()
    host=input("\n\n\033[01;33m  Enter your localhost ip (\033[01;36mex: localhost OR 127.0.0.1\033[01;33m) :- \033[01;36m")
    if host=="":
      host="localhost"
    Mylogo()
    sav=raw_input("\n\n\033[01;33m  Do you wan to save this setting [\033[01;32mY/n\033[01;33m] >> \033[01;36m")
    if sav=="Y" or sav=="y":
      spat=open(spath+".path.aex","w")
      spat.write(gp)
      spat.close()
      sport=open(spath+".port.aex","w")
      sport.write(port)
      sport.close()
      shost=open(spath+".host.aex","w")
      shost.write(host)
      shost.close()

    os.system("python modules/.srvr.aex")
    Mylogo()
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
      ngi(port,gp)
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
    opt=input("\n\033[01;33m Do you want to install Nginx Server [\033[01;32mY/n\033[01;33m] >>\033[01;36m ")
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
        print("\n\n\033[01;31m  Sorry we can't install \033[01;33mNginx Server\033[01;31m in your "+system+".")
        sleep(3)