#!/usr/bin/python

import sys
import json

allow=[]
f1= sys.argv[2]
f = open(f1)
allowips = json.load(f)
f.close()
for i in allowips:
    allow.append( i[0] )
print(allow)

configfile= sys.argv[1]
print(configfile)

f = open(configfile)
dt1 = json.load(f)
f.close()
dt1["settings"]["UserAllowedIP"] = allow
dt1j = json.dumps(dt1, indent = 2, separators=(',', ': ') )

file = open(configfile, "w")
file.write(dt1j)
file.close
 

