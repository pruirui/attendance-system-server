from flask_sqlalchemy  import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = 'liyuanhang'
DB = 'clock'
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
# 数据库配置     
app = Flask(__name__,static_url_path="/images",static_folder="images")
CORS(app)
app.config["JSON_AS_ASCII"] = False
app.config["UPLOAD_FOLDER"] = '/images'
app.config['SECRET_KEY'] = 'hard to guess'
                                                     #用户名：密码@ip：port/数据库名字
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

# 数据库操作对象
db_init = SQLAlchemy(app)

engine = create_engine(DB_URL)
# Base = declarative_base(engine)
session = sessionmaker(engine)()

