from flask import Flask, jsonify,request, render_template
from flask_restful import Api,Resource
from database import db
from resources import  routes


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/fcit'
}
api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/showProducts')
def showProducts():
    return render_template("ShowProduct.html")

@app.route('/addProduct')
def addProduct():
    return render_template("AddProduct.html")

@app.route('/updateProduct')
def updateProduct():
    return render_template("update.html")

@app.route('/deleteProduct')
def deleteProduct():
    return render_template("delete.html")

@app.route('/addVeh')
def addvehicleform():
    return render_template("AddVehicle.html")

@app.route('/showData')
def showData():
    return render_template("ShowData.html")

@app.route('/showContacts')
def showContacts():  # put application's code here
    return render_template("ShowContacts.html")

@app.route('/addContacts')
def addContacts():  # put application's code here
    return render_template("AddContact.html")


if __name__ == '__main__':
    app.run()


