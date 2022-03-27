#!/bin/sh
cd /home/administrador1/mesh_geoip

python3 maxmind_get.py

systemctl stop meshcentral8843
systemctl status meshcentral8843
python3 meshcentral_update.py /home/meshcentral/meshcentral-data/config.json ./2264397.json.txt
systemctl start meshcentral8843
systemctl status meshcentral8843

