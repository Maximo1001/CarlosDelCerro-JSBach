#!/bin/bash


/bin/cat << EOM

<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta content="MSHTML 6.00.2900.3660" name=GENERATOR> 

EOM
cat ../utils/styles.css
/bin/cat << EOM

</head>
<body>
<h2>MODEL</h2>

<h4><a href="/jsbach/model/model.cgi?comand=iniciar&" target="body">iniciar</a></h4>
<h4><a href="/jsbach/model/model.cgi?comand=aturar&" target="body">aturar</a></h4>
<h4><a href="/jsbach/model/model.cgi?comand=estat&" target="body">estat</a></h4>
<h4><a href="/jsbach/model/model-configurar.cgi" target="body">configuracio</a></h4>
</body>
</html>

EOM
