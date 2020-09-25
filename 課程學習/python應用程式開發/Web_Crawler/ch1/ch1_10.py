# ch1_10.py
import json
      
fn = 'AQI.json'
with open(fn, 'r',encoding="utf-8") as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))








