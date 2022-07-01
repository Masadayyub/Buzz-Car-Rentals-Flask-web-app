import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/abc'
# 'mysql://root:123@127.0.0.1:3306/web'
'mysql+pymysql://sql6495503:V8dTkaFWB1@sql6.freemysqlhosting.net:3306/sql6495503'

from Api import models
from Api import views
