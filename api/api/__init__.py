from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super_secret_key'

from . import controllers


__version__ = '0.1.0'
