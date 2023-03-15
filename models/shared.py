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

    def _as_dict(self):
        return {c.uid: getattr(self, c.uid) for c in self.__table__.columns}
