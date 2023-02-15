from .db import db


class user(db.Document):
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    phone = db.IntField(required=True)
    password = db.StringField(required=True)
    confirmPassword = db.StringField(required=True)




class order(db.Document):
    orderEmail = db.StringField(required=True)
    pizzaSize = db.StringField(required=True)
    flavour = db.StringField(required=True)
    crustType = db.StringField(required=True)
    ingredient1 = db.StringField(required=True)
    ingredient2 = db.StringField(required=True)
    address=db.StringField(required=True)




class menu(db.Document) :
    pizzaName =db.StringField(required=True)
    description =db.StringField(required=True)
    pizzaIngredients = db.StringField(required=True)
    smallPrice = db.StringField(required=True)
    mediumPrice = db.StringField(required=True)
    largePrice = db.StringField(required=True)