from models.user import Users,User_clocks,User_applications
from models.shared import User_departments
from models.HR import HR_UserFace
from db_config import session
from db_config import db_init as db
from sqlalchemy import extract, and_
# 
class User_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _all(self):
        user_list =  Users.query.all()
        return user_list
    
    def _login(self,phone,pwd):
        user_list =  Users.query.filter_by(phone = phone).first()
        return user_list
    
    def _reg(self,kwargs):
        new_user = Users(phone=kwargs["phone"],password=kwargs["password"],username=kwargs['username'])
        session.add(new_user)
        session.commit()
        # session.close()
    
    def _queryUserById(self,phone):
        user = Users.query.filter_by(phone=phone).first()
        return user
    
    def _userUploadImg(self,uid,facepath):
        user = Users.query.filter(Users.id == uid).first()
        user.headshot = facepath
        db.session.commit()

    def _userUpdate(self,uid,datas):
        user = Users.query.filter(Users.id == uid).first()
        if user:
            user.username = datas['username']
            user.password = datas['password']
            user.phone = datas['phone']
            user.address = datas['address']
            user.birthday = datas['birthday']
            user.motto = datas['motto']
            user.gender = datas['gender']
            user.home = datas['home']
            user.email = datas['email']
            db.session.commit()
        else:
            print("not found!")
        # session.close()
    
    def _userClock(self,uid,time,note):
        new_data = User_clocks(uid=uid,clockTime=time,note=note)
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userClockData(self,uid):
        data_list = User_clocks.query.filter_by(uid=uid).all()
        print(type(data_list))
        return data_list
    
    def _userClockByCondition(self,uid,date,note):
        print(date)
        data_list = User_clocks.query.filter(and_(\
            extract('year', User_clocks.clockTime) == date[:4],
            extract('month', User_clocks.clockTime) == date[5:7],\
            extract('day', User_clocks.clockTime) == date[8:]),User_clocks.uid==uid,User_clocks.note==note).first()
        return data_list
    
    def _allUserClockData(self):
        data_list = User_clocks.query.all()
        return data_list
    
    def _userLeave(self,uid,time,content,state):  #请假
        new_data = User_applications(uid=uid,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()

    def _userWorkOverTime(self,uid,time,content,state):  #加班
        new_data = User_applications(uid=uid,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userMakeUpClock(self,uid,time,content,state):  #补打卡
        new_data = User_applications(uid=uid,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()

    def _userApplyDepartment(self,datas): 
        new_data = User_departments(uid=datas['uid'],indate=datas['indate'],departmentid=datas['departmentid'],role="员工",state="待审核")
        session.add(new_data)
        session.commit()
        # session.close()

    def _userQuitDepartment(self,datas): 
        User_departments.query.filter_by(uid=datas['uid'],departmentid=datas['departmentid']).delete()
        db.session.commit()
        # session.close()

    def _userQueryEmbedding(self,uid):
        data = HR_UserFace.query.filter_by(id=uid).first()
        return data
    
    def _userQueryDepartment(self,uid):
        data = User_departments.query.filter_by(uid=uid).first()
        return data