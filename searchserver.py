import grpc
import redis
from concurrent import futures
import time
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json


class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        #aux = self.CheckCache(message)
        #if aux != None:
        #    print("palabra en cache")
        #    data = {'name':message, 'price':+int(aux)}
        #    search_res = {'product': [data]}
        #    return pb2.SearchResults(**search_res)
            
        result =self.CheckInventory(message)
        search_res = {'product': [result]}
        print("palabra no esta en cache")
        return pb2.SearchResults(**search_res)

        
    def CheckInventory(self, request):
        f = open('products.json',)
        data = json.load(f)
        for i in data['products']:
            if i["name"] == request:
                return {'name': i['name'], 'price': i['price']}
            # Este ciclo es en caso de no encontrar un producto con ese nombre.
            # Lo hice asi porque no se me ocurrio otra manera xd
        for i in data['products']:
            if i['name'] == 'no disponible':
                f.close()
                return {'name': i['name'],'price': i['price']}
    

    #Esta no se usa.
    def CheckCache(self, request):
        r = redis.Redis(host="localhost", port=6379, db=0)
        value = r.get(request)
        if type(value) != type(None):
            value = str(value, 'utf-8')
            return value
        else:
            f = open('products.json',)
            data = json.load(f)
            for i in data['products']:

                if i["name"] == request:
                    r.set(i["name"],i["price"])
                    print("Se añade la palabra al cache")

        return (value)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()