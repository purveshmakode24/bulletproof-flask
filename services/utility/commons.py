import os
import sys
import logging
from distutils.log import error
# configparser to read config file
from configparser import ConfigParser

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

config = ConfigParser()
# config.read('C:\\Users\\PURVESH\\Desktop\\WORKSPACE\\bulletproof-flask\\config\\config.ini')
config.read(ROOT_DIR+'\\config\\config.ini')

log = logging.getLogger('commons.py')


"""Check whether the db password arg is provided while running
 the application or not"""
if not (len(sys.argv) == 2 and sys.argv[-1].isdigit()):
    # sys.stderr.write('DB auth failed.
    #  Please provide correct DB Credatials.')
    raise error('DB password args is missing!')


DB = config['DB']['database']
USER = config['DB']['user']
HOST = config['DB']['host']
PORT = config['DB']['port']
DB_PASS = sys.argv[-1]
# DB_PASS = config['DB']['db_pass']
LOG = config['PATH']['log']
LOG_PATH = config['PATH']['log_path']
