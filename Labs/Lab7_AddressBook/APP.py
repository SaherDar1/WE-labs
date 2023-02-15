from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route('/create contact')
def create_contact():
    return render_template("create_contact.html")

@app.route('/create contact', methods=["POST"])
def contact():
    Id = request.form["Id"]
    name=request.form["name"]
    MobileNo = request.form["MobileNo"]
    City = request.form["City"]
    Profession  = request.form[" Profession"]
