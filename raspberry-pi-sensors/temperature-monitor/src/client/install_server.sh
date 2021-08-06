#!/bin/bash

read -r -p "Install dependency? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY])
        sudo apt install libmariadb3


        read -r -p "Insert username for DB Connection: " u1
        read -r -p "Insert password for DB Connection: " p1

        echo $u1
        echo $p1

        vstr="{
    \"MainConnection\": {
        \"username\": \"$u1\",
        \"password\": \"$p1\"
    }
}"

        echo $vstr > db_config.json

        ;;
    *)
        echo "Cannot continue."
        exit 1
        ;;
esac

read -r -d '' VAR << EOM
[Unit]
Description=Sensor connector to DB
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=8
User=pi
ExecStart=python3 /home/.sensors_python/script.py

[Install]
WantedBy=multi-user.target
EOM

mkdir /home/.sensors_python/script.py
cp server.py /home/.sensors_python/

echo "$VAR" > /etc/systemd/system/sensor_logger.service
cd /etc/systemd/system
chmod 644 sensor_logger.service
systemctl enable sensor_logger.service
systemctl stop sensor_logger.service
systemctl start sensor_logger.service