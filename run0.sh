#!/bin/sh

#put this on crontab every week, no need to do it dayly

cd /home/administrador1/mesh_geoip

#get updated geoip database and save it to countrycode.json.txt
python3 maxmind_get.py

systemctl stop meshcentral8843
systemctl status meshcentral8843

#update meshcentral config
python3 meshcentral_update.py /home/meshcentral/meshcentral-data/config.json ./2264397.json.txt

systemctl start meshcentral8843
systemctl status meshcentral8843

