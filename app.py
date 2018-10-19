import os

from flask import Flask 



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SECRET_KEY'] = 't\x12\xd0\xb7\xab-^g\xc1\xeb\xbc\x0b\xc4\x8e\x1d\xc1G\xffM>\xcd^}\x9f'
app.config['DEBUG'] = True

