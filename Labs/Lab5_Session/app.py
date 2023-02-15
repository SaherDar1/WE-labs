from flask import Flask ,render_template,request,make_response,session
from flask_session import Session
from DBHandler import  DBHandler
app = Flask(__name__)
# configure app.config to fetch configuration from config.py
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]
Session(app)



@app.route('/')
def hello_world():  # put application's code here
    return render_template("first.html")
@app.route('/first',methods=["GET","POST"])
def first():
    name = request.form["name"]
    pwd = request.form["pwd"]




@app.route('/test')
def test():
    list_=["one","two","three",1,2,3]
    return render_template("Test.html",msg="Server talking" , data=list_ )
@app.route('/registerstudent')
def registerForm():
    return render_template("RegisterStudent.html")

@app.route('/register', methods=["POST"])
def register():
    rollno = request.form["rollno"]
    name=request.form["name"]
    semmester = request.form["semmester"]
    cgpa = request.form["cgpa"]
    print(rollno,name,semmester,cgpa)
    # create Student
    # DB Handler object create
    handler=DBHandler(app.config["DP_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    # using DB handler call insertStudent
    if name=="Ali":
        #response=make_response(render_template("dashboard.html" , name=name))
        #response.set_cookie("uname",name)
        #response.set_cookie("usem", semmester)
        session["uname"] = name
        session["usem"] = semmester

        #return response
        return render_template("dashboard.html" , name=name)
    else:
        return render_template("RegisterStudent.html",msg="Registration failed")

@app.route('/showCourses')
def showCourses():
    #name=request.cookies.get("uname")
    semmester=session.pop("usem")
    name = session.get("uname")
    if name!=None:
        course1={"name":"web","credit":3.0,"enrolled":"Y"}
        course2 = {"name": "web lab", "credit": 1.0, "enrolled": "Y"}
        course3 = {"name": "InformationSecurity", "credit": 3.0, "enrolled": "Y"}
        courses=[course1,course2,course3]
        return render_template("Courses.html",courses=courses , name=name)
    else:
        return render_template("RegisterStudent.html",msg="Please register first to use this page")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("RegisterStudent.html")


def clever_function_12():
    return u'HELLO'

def clever_function_2(a, b):
    return a + b



app.jinja_env.globals.update(
    one=clever_function_12,
    two=clever_function_2,
)

if __name__ == '__main__':
    app.run()