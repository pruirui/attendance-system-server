from db_config import db_init as db
import datetime

class User_departments(db.Model):
    __tablename__ = 'user_departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departmentid = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    indate = db.Column(db.Date, nullable=False,default = datetime.date)
    state = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(45), nullable=False)

class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, nullable=False)
    process_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(45), nullable=False)
    event = db.Column(db.String(45), nullable=False)
    create_Time = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    apply_Time = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    state = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    