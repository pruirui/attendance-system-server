from db_config import db_init as db
import datetime

    
class HR_Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HRname = db.Column(db.String(45), nullable=False)
    createTime = db.Column(db.DateTime, nullable=False,default = datetime.datetime.utcnow)
    description = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    departmentName = db.Column(db.String(45), nullable=False)

class HR_SysConfig(db.Model):
    __tablename__ = 'sysconfigs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clockInTime = db.Column(db.Time, nullable=False,default = datetime.time)
    clockOutTime = db.Column(db.Time, nullable=False,default = datetime.time)
    departmentName = db.Column(db.String(45), nullable=False)

class HR_UserFace(db.Model):
    __tablename__ = 'userfaces'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(45), nullable=False)
    userFacePath = db.Column(db.String(45), nullable=False)
    faceEmbedding = db.Column(db.String(145), nullable=False)
    createTime = db.Column(db.Time, nullable=False,default = datetime.datetime.utcnow)
    updateTime = db.Column(db.Time, nullable=False,default = datetime.datetime.utcnow)
 