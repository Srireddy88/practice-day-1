from  flask import Flask,render_template,request
import pymysql
app=Flask(__name__)

def getConnect():
    con=pymysql.connect(host="127.0.0.1",user="root",password="1234",database="sridevi")
    return con
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Registeraction",methods=['POST'])
def RegAction():
    n=request.form['fname']
    e=request.form['email']
    u=request.form['uname']
    p=request.form['pwd']
    con=getConnect()
    cur=con.cursor()
    cur.execute("insert into student (name,email,username,password)values(%s,%s,%s,%s)",(n,e,u,p))
    con.commit()
    return render_template('index.html',msg="registration successfull")
@app.route("/Login.html")
def login():
    return render_template("login.html")

@app.route("/Loginaction",methods=['POST'])
def logAction():
    u=request.form['uname']
    p=request.form['pwd']
    con=getConnect()
    cur=con.cursor()
    cur.execute("select * from student where username=%s and password=%s)",(u,p))
    data = cur.fetchone()
    if data is not None:
        return render_template('UserHome.html')
    else:
        return render_template('login.html',msg="Login Failed..!!")

if __name__=="__main__":
    app.run(debug=True)