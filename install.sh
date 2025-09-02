#!/bin/sh
#
# THIS SCRIPT WILL INSTALL THE GTODO APP SYSTEM WIDE
# THE SCRIPT MUST BE RUN WITH SUDO
#
# It will create a startup shell script named gtodo in /usr/bin,
# the app will be placed in /usr/share/gtodo-sprokkel78
# The .desktop file will be placed in /usr/share/applications/ as com.sprokkel78.gtodo.desktop

mkdir -p /usr/share/ginsta-sprokkel78
cp -r ./* /usr/share/ginsta-sprokkel78/
echo "#!/bin/sh" > /usr/bin/ginsta
echo "cd /usr/share/ginsta-sprokkel78" >> /usr/bin/ginsta
echo "python3 ./ginsta.py" >> /usr/bin/ginsta
cp ./ginsta.desktop /usr/share/applications/com.sprokkel78.ginsta.desktop
chmod 755 /usr/bin/ginsta
chmod 664 /usr/share/ginsta-sprokkel78/*
