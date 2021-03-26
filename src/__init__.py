import flask
import mongoengine

database_conn_str = ""
hostname = "127.0.0.1:5000"
mongoengine.connect(database_conn_str)
app = flask.Flask(__name__)

from . import routes

