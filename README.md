# MyServer

MyServer is your own localhost server. you can setup PHP, Apache and MySQL servers on your android devices or linux like Ubuntu etc. MyServer is Developed for android terminal like Termux or GNURoot Debian terminal. You can setup your localhost server and access from internet. you can host your website and test your website.
<br/><br/><br/>

<p align="center">
<img src="https://github.com/Rajkumrdusad/MyServer/blob/master/Scr/Screenshot_2018-08-03-20-16-17-1.png"/>
</p>

<br/><br/><br/>

# How to use ?

**CLI Use :**

  ***Example : `myserver -s localhost 8080 /home/www`***
- `myserver -s <hostname/ip> <localhost_port> <document_root_path>` to start default localhost server.
- `myserver -s -ng <hostname/ip> <localhost_port> <document_root_path>` to start Nginx web server.
- `myserver -s -php <hostname/ip> <localhost_port> <document_root_path>` to start php localhost server.
- `myserver -s -py <hostname/ip> <localhost_port> <document_root_path>` to start python localhost server.
- `myserver -h <domain_name> <localhost_port> <http_port/https_port>` to access localhost server on internet.
- `myserver -db [start/stop]` to start/stop mysql database server.
- `myserver -s apache` to start apache web server.
- `myserver update` to update MyServer.
- `myserver rm -t` uninstall MyServer.
- `myserver start` start MyServer menu.
- `myserver -s` to start Server that was previously running.
- `myserver -h` to access from web that was previously accessed.


**Manual Use :**
- Type 1 : to start your localhost web server.
- Type 2 : to access your website from internet.
- Type 3 : to start MySQL Database server.
- Type 4 : to start menual localhost server.
- Type 5 : to menual host.
- Type 6 : to update MyServer.
- Type 7 : for server setting.
- Type 8 : to about us.
- Type x : to exit.

<br/>

## Support :

* **Apache2 server.**
* **nginx server.**
* **PHP server.**
* **Python web server.**
* **MySQL Database server.**

<br/>

## MyServer is available for :

* **Android**
* **Ubuntu**
* **Linux**
<br/>

# How to Install MyServer ?

Open the termux app and type following commands.

* `apt update`

* `apt install git`

* `git clone https://github.com/Rajkumrdusad/MyServer.git`

* `cd MyServer`

* `chmod +x install`

* `sh install` if not work than type `./install`

<br/>

## Now MyServer is installed successfully.

**Now type `myserver start` to start MyServer.**

<br>

**Warning :** ***I am not expert so use this tool at your own risk.***

<br/>

