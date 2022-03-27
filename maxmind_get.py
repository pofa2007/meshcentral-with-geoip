import requests
import csv
import json

key="PUT-YOUR-KEY-HERE"
geoip_url="https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=" + key + "&suffix=zip"
filename="GeoLite2-Country-CSV.zip"
country = "2264397"  #portugal


req = requests.get(geoip_url)
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

name1=""
import zipfile
with zipfile.ZipFile(filename, 'r') as zip_ref:
    for name1 in zip_ref.namelist():
        if "GeoLite2-Country-Blocks-IPv4.csv" in name1:
            zip_ref.extract(name1)
            print(name1)
            break

c=[]
with open(name1, mode ='r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if line[1] == country:
            #print(line[1])
            c.append(line)
cj = json.dumps(c)

file = open(country + ".json.txt", "w")
file.write(cj)
file.close

