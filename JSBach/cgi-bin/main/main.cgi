#!/bin/bash

/bin/cat <<EOM

<!DOCTYPE html>
<html lang="ca" class="main-layout">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administració de $HOSTNAME</title>
EOM

cat ../utils/styles.css

/bin/cat <<EOM
</head> 
<body>
    <div class="container">
        <iframe src="/jsbach/main/index-admin.cgi" name="menu-general" class="header"></iframe>
        <div class="main-content">
            <iframe src="/jsbach/main/blanc.cgi" name="menu" class="sidebar"></iframe>
            <iframe src="/jsbach/main/estat.cgi" name="body" class="body-content"></iframe>
        </div>
    </div>
</body>
</html>

EOM
