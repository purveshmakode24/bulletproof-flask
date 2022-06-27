import os
import sys
from flask import Flask
from controller import *
from utility.commons import LOG
import logging

app = Flask(__name__)

logging.basicConfig(filename=str(LOG), encoding='utf-8', level= logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log = logging.getLogger('app.py')


# main driver function
if __name__ == '__main__':
    # lazily initalized flask-restx
    api.init_app(app)
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)