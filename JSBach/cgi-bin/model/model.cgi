#!/bin/bash


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html>"
echo "<head>"
echo "    <meta charset="utf-8">"
echo "    <title>Hola món CGI</title>"

cat ../utils/styles.css

echo "</head>"
echo "<body>"

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

case $comand in	
    	iniciar|aturar|estat)
    		echo "<h2>MODEL $comand </h2>"
		echo "<pre>$(echo "model $comand"|nc 127.0.0.1 1234)</pre>"
		;;
	configurar)
		opcio=$(echo "$QUERY_STRING" | sed -n 's/^.*opcio=\([^&]*\).*$/\1/p')		
		case $opcio in			
			guardar)
				argument=$(echo "$QUERY_STRING" | sed -n 's/^.*argument=\([^&]*\).*$/\1/p')	
				echo "$(echo "model $comand $opcio $argument"|nc 127.0.0.1 1234)"
			;;
		esac
		;;
esac

echo "</body>"
echo "</html>"
