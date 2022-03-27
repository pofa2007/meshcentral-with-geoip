import requests
import csv
import json

#how to get an API KEY:
#https://blog.maxmind.com/2021/01/integrating-maxminds-free-and-paid-ip-geolocation-web-services-in-php?lang=en

key="PUT-YOUR-KEY-HERE"
geoip_url="https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=" + key + "&suffix=zip"
filename="GeoLite2-Country-CSV.zip"
country = "2264397"  #portugal

# do not change from here

## get geoip from database
req = requests.get(geoip_url)
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

## extract csv from zip
name1=""
import zipfile
with zipfile.ZipFile(filename, 'r') as zip_ref:
    for name1 in zip_ref.namelist():
        if "GeoLite2-Country-Blocks-IPv4.csv" in name1:
            zip_ref.extract(name1)
            print(name1)
            break
            
## build array with all ip ranges from coutry
c=[]
with open(name1, mode ='r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if line[1] == country:
            #print(line[1])
            c.append(line)
            
## save array in file as json 
cj = json.dumps(c)
file = open(country + ".json.txt", "w")
file.write(cj)
file.close

