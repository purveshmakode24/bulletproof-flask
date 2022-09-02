import os
import sys
import logging
from distutils.log import error
# configparser to read config file
from configparser import ConfigParser
from colorama import Fore, Style

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

config = ConfigParser()
# config.read('C:\\Users\\PURVESH\\Desktop\\WORKSPACE\\bulletproof-flask\\config\\config.ini')
config.read(ROOT_DIR+'\\config\\config.ini')

log = logging.getLogger('commons.py')

DB = config['DB']['database']
USER = config['DB']['user']
HOST = config['DB']['host']
PORT = config['DB']['port']
DB_PASS = sys.argv[-1]
LOG = config['PATH']['log']
LOG_PATH = config['PATH']['log_path']

"""Check whether the db password arg is provided while running
 the application or not"""
if not (len(sys.argv) == 2 and sys.argv[-1].isdigit()):
    # sys.stderr.write('DB auth failed. Please provide correct DB Credatials.')
    raise error('DB password args is missing!')

if not os.path.exists(LOG_PATH):
    print('Log directory does not exists. Auto creating log directory...')
    os.mkdir(LOG_PATH)
    print(
        Fore.GREEN + 'Auto creating log directory completed!'
        + Style.RESET_ALL)
