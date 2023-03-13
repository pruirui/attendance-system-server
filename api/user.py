from operation.user import User_operation
from utils.data_process import Class_To_Data,query2dict
# from db_config import session

def User_MakeUpClock(username,time,content,state):
    u_o = User_operation()
    data = u_o._userMakeUpClock(username,time,content,state)
    return data

def User_WorkOverTime(username,time,content,state):
    u_o = User_operation()
    data = u_o._userWorkOverTime(username,time,content,state)
    return data

def User_Leave(username,time,content,state):
    u_o = User_operation()
    data = u_o._userLeave(username,time,content,state)
    return data 

def User_BaseData(username):
    u_o = User_operation()
    data = u_o._queryUserById(username)
    data = query2dict(data)
    return data

def Alluser_ClockData():
    u_o = User_operation()
    data = u_o._alUserClockData()
    data = query2dict(data)
    return data

def User_ClockData(username):
    u_o = User_operation()
    data = u_o._userClockData(username)
    data = query2dict(data)
    return data

def User_clock(username,time,note):
    u_o = User_operation()
    # print(username,time,note)
    data = u_o._userClock(username,time,note)

    return "ok"

def User_list():
    u_o = User_operation()
    data = u_o._all()
    # data（复杂对象）====> 数据
    data = Class_To_Data(data,u_o.__fields__, 0)
    return data


def User_reg(kwargs):
    u_o = User_operation()
    data = u_o._reg(kwargs)
   
    return "ok"

def User_update(username,password):
    u_o = User_operation()
    data = u_o._userUpdate(username,password)
   
    return "ok"

def User_isExisted(username):  
    u_o = User_operation()
    data = u_o._queryUserById(username)
    if data is None:
        return 0
    data = query2dict(data)
    return data 

def User_login(name,pwd):
    u_o = User_operation()
    data = u_o._login(name,pwd)
    if data is None:
        return "该用户不存在"
    # print(data)
    data = Class_To_Data(data,u_o.__fields__, 1)
    print(name,pwd)
    print(data)
    if data['password'] != pwd:
        return "密码不正确"
    #  else
    return data