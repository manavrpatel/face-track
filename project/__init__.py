from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///attendance.db'
app.config['SECRET_KEY'] = '139efd161f40e7095537b04'
db = SQLAlchemy(app)

from project import route