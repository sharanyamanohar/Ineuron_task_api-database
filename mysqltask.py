from flask import Flask,request,jsonify
import mysql.connector as conn
"""app=Flask(__name__)
mydb=conn.connect(host="Localhost",user="root",passwd="mysql")
cursor=mydb.cursor()
cursor.execute("Create database if not exist taskdb")
cursor.execute("create table if not exist taskdb.tasktable(name varchar(30),number int)")"""


app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user = 'root' , passwd = "mysql")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        cursor.execute("insert into taskdb.tasktable values(%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str("sucessfully executed"))
@app.route("/update",methods=['POST'])
def update():
    if request.method=='POST':
        get_name=request.json['get_name']
        cursor.execute("update taskdb.tasktable set number=number +500 where name=%s",(get_name,))
        mydb.commit()
        return jsonify (str("sucessfully updated"))
@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        name_del=request.json['name_del']
        cursor.execute("delete from taskdb.tabletask where name= %s",(name_del))
        mydb.commit()
        return jsonify(str("successfully deleled"))

@app.route("/fetch",methods=['POST','GET'])
def fetch_data():
    cursor.execute("select * from taskdb.tasktable")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))
if __name__=='__main__':
    app.run()