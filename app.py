from flask import Flask, render_template,request
import json
from db_config import app
# app = Flask(__name__)

# user模块
from routes.user import user
from routes.HR import HR
from routes.img import images
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(HR,url_prefix="/HR")
app.register_blueprint(images,url_prefix="/images")

# @app.route('/')
# def ping():
#     return "ok"
@app.route('/')
def index():
    return render_template('index.html',name='index')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)