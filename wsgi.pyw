import configparser
from waitress import serve
from app import app

config = configparser.ConfigParser()
config.read('config.ini')

PORT = config.getint('Server', 'port')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=PORT)
