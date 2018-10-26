# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 23/5/2018
# Powered By :- Aex Software's

if [ -e  /usr/lib/sudo ];then
  if [ ! -e /usr/bin/python2 ];then
     sudo apt-get update
     sudo apt-get upgrade -y
     sudo apt-get install python -y
     sudo apt-get install python2 -y
     sudo apt-get install curl -y
   fi
else
  if [ -d /usr/bin ];then
    if [ ! -e /usr/bin/python2 ];then
     apt-get update
     apt -get upgrade -y
     apt-get install python -y
     apt-get install python2 -y
     apt-get install curl -y
    fi
  fi
fi
if [ ! -d /usr/bin ];then
  if [ ! -e /data/data/com.termux/files/usr/bin/python2 ];then
    pkg update
    pkg upgrade -y
    pkg install python -y
    pkg install python2 -y
    pkg install curl -y
  fi
fi
python2 .setup.aex
exit
