from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as mysql
from send_email import *
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
CORS(app)
def getdb():
    return mysql.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASS"),database=os.getenv("DB_NAME"))

@app.route("/send-veri",methods=["POST"])
def verification():
    if request.method=="POST":
        data=request.json
        num=send_verification(data.get("email"))
        return jsonify({"NUM":num,"status":"success"})

@app.route("/subscribe",methods=["GET","POST"]) 
def costomers():
    if request.method=="GET":
        connection=getdb()
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM customerinfo;"
        cursor.execute(query)
        rows=cursor.fetchall()

        cursor.close()
        connection.close()
        return jsonify(rows)
    
    if request.method=="POST":
        data=request.json
        email=data.get("email")
        phone=data.get("phone")
        connection=getdb()
        cursor=connection.cursor()
        
        query="insert into project.customerinfo(email,phone) values(%s,%s)"
        cursor.execute(query,(email,phone))
        send_mail(email)
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"status":"success"})
    
if __name__=="__main__":
    app.run(debug=True)