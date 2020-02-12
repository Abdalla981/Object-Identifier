from flask import Flask

app = Flask(__name__)   # initialises the flask app

from app import routes