import json
  
f = open('products.json',)
  
data = json.load(f)
  
for i in data['products']:
    print(i['name'])
  
f.close()