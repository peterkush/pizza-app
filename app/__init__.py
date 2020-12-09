from flask import Flask
from config import config_options


def create_appp(config_name):
    app = Flask(__name__)