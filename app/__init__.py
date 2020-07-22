from flask import Flask
from flask_bootstrap import Bootstrap
# from .config import config_options

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'
bootstrap = Bootstrap(app)

from app import views
