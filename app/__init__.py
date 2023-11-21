from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljjr1989jjlyyaf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from app import routes