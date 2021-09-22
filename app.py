import re
import searchclient, searchserver
from flask import Flask, request, redirect, url_for
import json
import redis
app = Flask(__name__)

@app.route('/')
def hello():
    return ("hOLO")

@app.route('/search', methods = ["POST"]) 
def search():
    data = request.args.get("sol")
    r = redis.Redis(host="localhost", port=6379, db=0)
    if type(r.get(data)) != type(None):
        print("esta en cache")
        value = r.get(data)
        value = str(value,'utf-8')
        result = "name: "+str(data)+ "\n price: "+str(value)
        return (str(result))
    print("palabra no esta en cache")
    f = open('products.json',)
    d = json.load(f)
    for i in d['products']:
        if i["name"] == data:
            r.set(i["name"],i["price"])
            print("Se añade la palabra al cache")

    cl = searchclient.SearchClient()
    result = cl.get_url(message=data)

    return (f'{result}')

@app.route("/llenar")
def llenar():
    r = redis.Redis(host="localhost", port=6379, db=0)
    f = open('products.json',)
    data = json.load(f)
    for i in data['products']:
        r.set(i['name'],i['price'])
    f.close()
    return ('redis llenado')




if __name__ == "__main__":
    app.run(debug=True)