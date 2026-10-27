#!/bin/bash

echo "Content-Type:text/html;charset=utf-8"
echo "<html>"
echo "<head>"
echo "<title>Administrant el Router</title>"
echo "<meta http-equiv=Content-Type content='text/html; charset=windows-1252'>"
echo "<meta content='MSHTML 6.00.2900.3660' name=GENERATOR>"

cat ../utils/styles.css

echo "</head>"
echo "<body link='#E9AB17' vlink='#E9AB17' alink='#E9AB17'>"

PROMPT=$(echo "prompt" | nc 127.0.0.1 1234)
echo "<h2 align="center">Administrant el Router "$HOSTNAME" amb "$DIR_PROJECTE" "$PROMPT"</h2>"

echo "<script>"

#nova funcio

######################################################################### 
#Exemple nova funcio
#echo "function wan(){"
#echo "window.top.frames['menu'].location.href='/jsbach/wan/wan-menu.cgi';"
#echo "window.top.frames['body'].location.href='/jsbach/wan/wan.cgi?comand=estat&';"
#echo "}"
#########################################################################

echo "</script>"

echo "<table width="100%">"
echo "  <tr>"
echo "  <td>"
#nou boto
######################################################################### 
#Exemple nou boto
#echo "      <button onclick="wan()">WAN</button>"
#########################################################################
echo "  </td>"
echo "  </tr>"
echo "</table>"

echo "</body>"
echo "</html>"

