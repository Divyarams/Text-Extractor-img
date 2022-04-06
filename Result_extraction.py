import boto3,json,os

with open('outputoftextract.json','r') as json_file:
    json_load = json.load(json_file)
ineed = json_load['Blocks']
length = len(ineed)
print(length)
z = 1
while z < length:
    print(ineed[z]['Text'])
    z +=1