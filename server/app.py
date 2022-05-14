from flask import Flask
from flask_cors import CORS

from router import routes
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.register_blueprint(routes)
CORS(app)

