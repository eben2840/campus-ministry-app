
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,flash
import urllib.request, urllib.parse
from flask_migrate import Migrate

from form import *


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)






class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    number= db.Column(db.String(200))
    comment= db.Column(db.String(200))
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.number})"




@app.route('/index', methods=['POST','GET'])
def home():
    return render_template('index.html')
   

@app.route('/comment')
def comment():
    return render_template("comment.html")

 
@app.route('/')
def dashboard():
    return render_template("home.html")

 




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)