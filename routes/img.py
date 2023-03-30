import calendar
from collections import defaultdict
import hashlib
import random
from flask import Blueprint,request,jsonify, send_file
images = Blueprint('images',__name__)

@images.route('/headshots/<name>')
def headshots(name):
    print('name')
    path = './images/headshots/' + name
    return send_file(path, mimetype='image/jpg')