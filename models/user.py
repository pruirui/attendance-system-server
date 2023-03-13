
from db_config import db_init as db
import datetime
# 定义user模型类
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    motto = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    home = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<User %s>' % self.username

class User_clocks(db.Model):
    __tablename__ = 'user_clocks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, nullable=False)
    clockTime = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    note = db.Column(db.String(45), nullable=False)

class User_applications(db.Model):
    __tablename__ = 'user_applications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, nullable=False)
    applyTime = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    state = db.Column(db.String(45), nullable=False)
    content = db.Column(db.String(45), nullable=False)