#!/bin/bash

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM
cat ../utils/styles.css

echo "</head>"
echo "<body>"

#nova funcio

########################################
# Exemple
# echo "<h2>WAN</h2>"
# echo "<pre>"
# echo "$(echo "wan estat" | nc 127.0.0.1 1234) <br>"
# echo "</pre>"
########################################
echo "</body>"
echo "</html>"
