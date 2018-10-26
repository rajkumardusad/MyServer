#!/bin/bash
bin=index.html
cat > $bin <<- EOM
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>MyServer</title>
  <meta name="author" content="Aex Software's"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>

<!-- CSS -->
<style type="text/css">
  <!--
  body{
    font-family: "Roboto", "Droid Sans";
    width: 100%;
    min-width: 310px;
    margin: 0;
    padding: 0;
    background: #fff;
  }

  .myserver{
    margin: 50px 30px 0px 30px;
    text-align: center;
  }

  .myserver h1{
    font-size: 33px;
    color: #444;
 .}

  .myserver p{
    margin: 0 auto;
    text-align: center;
    font-size: 15px;
    color: #868686;
  }

  .txt{margin: 30px 25px 0;}
  .line{border-bottom: solid 1px rgba(0,0,0,.05);}
  .txt .txt-p{
    padding: 10px 0;
    font-size: 14px;
    color: #666;
    display: block;
    width: 100%;
    max-width: 520px;
   }
-->
</style>

</head>
<body>

<div class="myserver">
    <h1>MyServer</h1>
    <p>Your own localhost web server.</p>
</div>

<div class="txt">
    <div class="txt-p line">1. Your localhost web server is running.</div>
    <div class="txt-p line">2. Test your website on your localhost server.</div>
    <div class="txt-p line">3. Go to document root and replace your web file with index.html file.</div>
</div>
</body>
</html>
EOM