import redis
import json
r = redis.Redis(host="localhost", port=6379, db=0)

f = open('products.json',)
  
data = json.load(f)
  
for i in data['products']:
    r.set(i['name'],i['price'])
  
f.close()
print('redis llenado')
