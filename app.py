from flask import Flask,request
import json
from db_config import app
# app = Flask(__name__)

# user模块
from routes.user import user
from routes.HR import HR
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(HR,url_prefix="/HR")

@app.route('/')
def ping():
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)