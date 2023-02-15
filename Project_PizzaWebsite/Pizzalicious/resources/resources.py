from flask import Response, request
from flask_restful import Resource
from mongoengine import Q
from database.models import user,order,menu
import json




# These below apis are for the User point of view.
class AddUser(Resource):
    def get(self):
        no = request.args['no']
        try:
            no = int(no)
        except Exception as e:
            no = 0
        objects = user.objects().to_json()
        products = json.loads(objects)
        size = len(products)
        if (size < no):
            no = size
        list = []
        for i in range(0, no):
            list.append(products[i])
        return Response(json.dumps(list), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        prod = user(**body).save()
        return {'record with id ': str(prod.id)}, 200



class UpdateUser(Resource):
    def put(self, username):
        reqdata = request.get_json()
        obj = user.objects.get(username=username).update(**reqdata)
        return "updated"

    def delete(self, username):
        user.objects.get(username=username).delete()
        return "deleted"





class TakeOrder(Resource):
    def get(self):
        no = request.args['no']
        try:
            no = int(no)
        except Exception as e:
            no = 0
        objects = order.objects().to_json()
        products = json.loads(objects)
        size = len(products)
        if (size < no):
            no = size
        list = []
        for i in range(0, no):
            list.append(products[i])
        return Response(json.dumps(list), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        prod = order(**body).save()
        return {'record with id ': str(prod.id)}, 200



class SearchPizza(Resource):
    def get(self):
        word = request.args['word']
        print(word)
        obj = menu.objects.filter(Q(pizzaName__contains=word)).to_json()
        print(obj)
        return Response(obj, mimetype="application/json", status=200)









# These below apis are for the Admin point of view
class SearchUser(Resource):
    def get(self):
        word = request.args['word']
        print(word)
        obj = user.objects.filter(Q(username__contains=word)).to_json()
        print(obj)
        return Response(obj, mimetype="application/json", status=200)






class AddMenu(Resource):
    def get(self):
        no = request.args['no']
        try:
            no = int(no)
        except Exception as e:
            no = 0
        objects = menu.objects().to_json()
        products = json.loads(objects)
        size = len(products)
        if (size < no):
            no = size
        list = []
        for i in range(0, no):
            list.append(products[i])
        return Response(json.dumps(list), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        prod = menu(**body).save()
        return {'record with id ': str(prod.id)}, 200







class UpdateMenu(Resource):
    def put(self, pizzaName):
        reqdata = request.get_json()
        obj = menu.objects.get(pizzaName=pizzaName).update(**reqdata)
        return "updated"

    def delete(self, pizzaName):
        menu.objects.get(pizzaName=pizzaName).delete()
        return "deleted"