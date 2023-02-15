from flask import Flask,render_template,request,redirect
from flask_restful import Api
from database import db
from database.models import user,order,menu
from resources import routes

app=Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/WebProjectLast'
}
api = Api(app)
db.initialize_db(app)
routes.initialize_routes(api)



# This is for the frondend routes.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/About.html')
def about():
    return render_template('About.html')

@app.route('/Menu.html')
def menu():
    return render_template('Menu.html')

@app.route('/Order.html')
def contact():
    return render_template('Order.html')

@app.route('/guestorder.html')
def guestorder():
    return render_template('guestorder.html')

@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')
@app.route('/MenuVisitor.html')
def MenuVisitor():
    return render_template('MenuVisitor.html')








# Now working on the back end codes.
# User point of view
@app.route('/UserSignUp')
def api1Insert():
    return render_template('UserSignUp.html')


@app.route('/UserDataUpdate')
def apiUpdate():
    return render_template('UserDataUpdate.html')


@app.route('/UserDelete')
def api4_delete():
    return render_template('UserDelete.html')


@app.route('/UserOrder')
def InsertOrder():
    return render_template('UserOrder.html')

@app.route('/UserMenuSee')
def UserMenuWatch():
    return render_template('UserMenuSee.html')


@app.route('/UserPizzaSearch')
def UserMenuSearch():
    return render_template('UserPizzaSearch.html')



# Admin point of view
@app.route('/AuserSearch')
def search():
    return render_template("AuserSearch.html")

@app.route('/AuserSee')
def AdminUserWatch():
    return render_template('AuserSee.html')

@app.route('/AorderSee')
def AdminOrderWatch():
    return render_template('AorderSee.html')

@app.route('/AmenuInsert')
def AdminMenuInsert():
    return render_template('AmenuInsert.html')

@app.route('/AmenuUpdate')
def AdminMenuUpdate():
    return render_template('AmenuUpdate.html')


@app.route('/AmenuDelete')
def AdminMenuDelete():
    return render_template('AmenuDelete.html')

if __name__=='__main__':
    app.run(debug=True)