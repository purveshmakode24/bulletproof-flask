import os
# configparser to read config file
from configparser import ConfigParser

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config = ConfigParser()
#config.read('C:\\Users\\PURVESH\\Desktop\\WORKSPACE\\bulletproof-flask\\config\\config.ini')
config.read(ROOT_DIR+'\config\config.ini')


db = config['DB']['database']
user = config['DB']['user']
host = config['DB']['host']
port = config['DB']['port']
log = config['PATH']['log']
log_path = config['PATH']['log_path']
