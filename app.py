from flask import Flask, render_template, request

import pymysql as sql

app = Flask(__name__)

def db_connect():
    
    db = sql.connect(database="princedb", host="localhost", port=3306, user="root", password="")
    
    cursor= db.cursor()
    
    return db, cursor

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio/")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/aftersubmit/", methods=['GET', 'POST'])
def aftersubmit():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        name = request.form.get("name")
        
        email = request.form.get("email")
        
        phone = request.form.get("phone")
        
        message = request.form.get("message")
        
        db, cursor = db_connect()
        
        cmd = f"insert into port values('{name}', '{email}', '{phone}', '{message}')"
        
        cursor.execute(cmd)
        db.commit()
        db.close()
        
        msg= " DEATAAILS ARE SEND SUCCESSFULLY..."
        
        return render_template("contact.html", data=msg)
        
        
        
        





app.run(debug=True)