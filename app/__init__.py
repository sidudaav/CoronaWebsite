import os
import pathlib
import glob
from flask import Flask
from config import Config

#Clears the MapsHolder
files = pathlib.Path(__file__).parent.absolute()
MapsHolder_dir  = str(files) + '/static/MapsHolder/'
print(MapsHolder_dir)
for root, files in os.walk(MapsHolder_dir, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
