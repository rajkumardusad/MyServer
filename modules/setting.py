# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's

import sys
import os
from time import sleep
from core.system import *
from modules.logo import *

class set(object):
  def srst(self):
    Mylogo()
    if os.path.exists(spath+".path.aex"):
      pat=open(spath+".path.aex","r")
      path=pat.read()
      pat.close()
      if path=="":
        path="Default"
      ho=open(spath+".host.aex","r")
      host=ho.read()
      ho.close()
      if host=="":
        host="Default"
      po=open(spath+".port.aex","r")
      port=po.read()
      po.close()
      if port=="":
        port="Default"
      if system=="termux":
        print("\n\033[1;33m       Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
        print("\033[1;33m       Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
        print("\033[1;33m       Server port :    [ \033[01;36m"+port+" \033[01;33m]")
      else:
        print("\n\033[1;33m           Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
        print("\033[1;33m           Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
        print("\033[1;33m           Server port :    [ \033[01;36m"+port+" \033[01;33m]")
      ch=input("\n\033[01;33m Do you want to change setting [\033[01;36mY/n\033[01;33m] >> \033[01;36m")
      if ch=="y" or ch=="Y":
        self.chen()
      elif ch=="N" or ch=="n":
        self.sett()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ch+"\'")
        sleep(1)
        self.srst()
    else:
      pat=open(spath+".path.aex","w")
      path=pat.write("")
      pat.close()
      ho=open(spath+".host.aex","w")
      host=ho.write("")
      ho.close()
      po=open(spath+".port.aex","w")
      port=po.write("")
      po.close()
      self.srst()

  def chen(self):
    Mylogo()
    pat=open(spath+".path.aex","r")
    path=pat.read()
    pat.close()
    if path=="":
      path="Default"
    if system=="termux":
      print("\n\033[1;33m       Document Root : [ \033[01;36m"+path+" \033[01;33m]")
    else:
      print("\n\033[1;33m           Document Root : [ \033[01;36m"+path+" \033[01;33m]")
    chp=input("\n\033[01;33m Do you want to change path [\033[01;36mY/n\033[01;33m] >>\033[01;36m ")
    if chp=="y" or chp=="Y":
      pathw=input("\n\033[01;36m Enter new path \033[01;33m>> \033[01;36m")
      pat=open(spath+".path.aex","w")
      patw=pat.write(pathw)
      pat.close()
      self.chho()
    elif chp=="" or chp=="n" or chp=="N":
      self.chho()
    else:
      print("\n \033[01;31m\007Command not found :\033[01;32m \'"+chp+"\'")
      sleep(1)
      self.chen()

  def chho(self):
    ho=open(spath+".host.aex","r")
    host=ho.read()
    ho.close()
    if host=="":
      host="Default"
    Mylogo()
    if system=="termux":
      print("\n\033[1;33m       Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
    else:
      print("\n\033[1;33m           Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
    chh=input("\n\033[01;33m Do you want to change host [\033[01;36mY/n\033[01;33m] >>\033[01;36m ")
    if chh=="y" or chh=="Y":
      hostw=input("\n\033[01;36m Enter new host \033[01;33m>> \033[01;36m")
      h=open(spath+".host.aex","w")
      how=h.write(hostw)
      h.close()
      self.chpor()
    elif chh=="" or chh=="n" or chh=="N":
      self.chpor()
    else:
      print("\n \033[01;31m\007Command not found :\033[01;32m \'"+chh+"\'")
      sleep(1)
      self.chho()

  def chpor(self):
    po=open(spath+".port.aex","r")
    port=po.read()
    po.close()
    if port=="":
      port="Default"
    Mylogo()
    if system=="termux":
      print("\n\033[1;33m       Server port : [ \033[01;36m"+port+" \033[01;33m]")
    else:
      print("\n\033[1;33m           Server port : [ \033[01;36m"+port+" \033[01;33m]")
    chpo=input("\n\033[01;33m Do you want to change port [\033[01;36mY/n\033[01;33m] >> \033[01;36m")
    if chpo=="y" or chpo=="Y":
      portw=input("\n\033[01;36m Enter new port \033[01;33m>> \033[01;36m")
      por=open(spath+".port.aex","w")
      porw=por.write(portw)
      por.close()
      self.chend()
    elif chpo=="" or chpo=="n" or chpo=="N":
      self.chend()
    else:
      print("\n \033[01;31m\007Command not found :\033[01;32m \'"+chpo+"\'")
      sleep(1)
      self.chpor()

  def chend(self):
    Mylogo()
    pat=open(spath+".path.aex","r")
    path=pat.read()
    pat.close()
    if path=="":
      path="Default"
    ho=open(spath+".host.aex","r")
    host=ho.read()
    ho.close()
    if host=="":
      host="Default"
    po=open(spath+".port.aex","r")
    port=po.read()
    po.close()
    if port=="":
      port="Default"
    if system=="termux":
      print("\n\033[1;33m       Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
      print("\033[1;33m       Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
      print("\033[1;33m       Server port :    [ \033[01;36m"+port+" \033[01;33m]")
    else:
      print("\n\033[1;33m           Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
      print("\033[1;33m           Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
      print("\033[1;33m           Server port :    [ \033[01;36m"+port+" \033[01;33m]")
    ch=input("\n\033[01;33m Server\033[01;32m Setting changed !!! \033[01;33mEnter to continue >> \033[01;36m")
    self.sett()

  def vew(self):
    Mylogo()
    if os.path.exists(spath+".path.aex"):
      pat=open(spath+".path.aex","r")
      path=pat.read()
      pat.close()
      ho=open(spath+".host.aex","r")
      host=ho.read()
      ho.close()
      po=open(spath+".port.aex","r")
      port=po.read()
      po.close()
      if path=="":
        path="Default"
      if host=="":
        host="Default"
      if port=="":
        port="Default"
      if system=="termux":
        print("\n\033[1;33m       Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
        print("\033[1;33m       Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
        print("\033[1;33m       Server port :    [ \033[01;36m"+port+" \033[01;33m]")
      else:
        print("\n\033[1;33m           Document Root :  [ \033[01;36m"+path+" \033[01;33m]")
        print("\033[1;33m           Server Host/IP : [ \033[01;36m"+host+" \033[01;33m]")
        print("\033[1;33m           Server port :    [ \033[01;36m"+port+" \033[01;33m]")
      ch=input("\n \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      self.sett()
    else:
      pat=open(spath+".path.aex","w")
      path=pat.write("")
      pat.close()
      ho=open(spath+".host.aex","w")
      host=ho.write("")
      ho.close()
      po=open(spath+".port.aex","w")
      port=po.write("")
      po.close()
      self.vew()
 
  def sett(self):
    while True:
      Slogo()
      set=input(" \033[0;33m\033[4;mMyServer\033[00m\033[01;31m > \033[1;36m")
      if set=="1":
        self.vew()
        break
      elif set=="2":
        self.srst()
        break
      elif set=="0" or set=="back":
        break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+set+"\'")
        sleep(1)

def setting():
  set().sett()