# -*- coding: utf-8 -*-
import os
import flask
from parlr import app


class Server(flask.Flask):
    def __init__(self, import_name):
        root_dir = os.path.dirname(__file__)
        super().__init__(import_name,
                         static_folder=os.path.join(root_dir, 'client', 'dist'),
                         template_folder=os.path.join(root_dir, 'client', 'src'))

app = Server(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'