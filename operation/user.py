from models.user import Users,User_clocks,User_applications
from db_config import session
from db_config import db_init as db
# lei
class User_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _all(self):
        user_list =  Users.query.all()
        return user_list
    
    def _login(self,name,pwd):
        user_list =  Users.query.filter_by(username=name).first()
        return user_list
    
    def _reg(self,kwargs):
        new_user = Users(username=kwargs["username"],password=kwargs["password"])
        session.add(new_user)
        session.commit()
        # session.close()
    
    def _queryUserById(self,username):
        user = Users.query.filter_by(username=username).first()
        return user
    
    def _userUpdate(self,username,password):
        user = Users.query.filter(Users.username == "lee").first()
        if user:
            print("found!")
            user.password = password
            db.session.commit()
        else:
            print("not found!")
        # session.close()
    
    def _userClock(self,username,time,note):
        new_data = User_clocks(username=username,clockTime=time,note=note)
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userClockData(self,username):
        data_list = User_clocks.query.filter_by(username=username).all()
        return data_list

    def _userLeave(self,username,time,content,state):  #请假
        new_data = User_applications(username=username,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()

    def _userWorkOverTime(self,username,time,content,state):  #加班
        new_data = User_applications(username=username,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userMakeUpClock(self,username,time,content,state):  #补打卡
        new_data = User_applications(username=username,applyTime=time,content=content,state=state)
        session.add(new_data)
        session.commit()
        # session.close()