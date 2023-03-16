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

class Leaves(db.Model):
    __tablename__ = 'leaves'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HRuid = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(45), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    process_time = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(45), nullable=False)

class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, nullable=False)
    process_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(45), nullable=False)
    event = db.Column(db.String(45), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    apply_time = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    makeup_clock = db.Column(db.Date, nullable=False)