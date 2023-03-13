from operation.user import User_operation
from utils.data_process import Class_To_Data,query2dict
# from db_config import session

def User_queryClockBy(uid,date,note):
    u_o = User_operation()
    data = u_o._userClockByCondition(uid,date,note)
    if data is None:
        return None
    data = query2dict(data)
    return data

def User_MakeUpClock(uid,time,content,state):
    u_o = User_operation()
    data = u_o._userMakeUpClock(uid,time,content,state)
    return data

def User_WorkOverTime(uid,time,content,state):
    u_o = User_operation()
    data = u_o._userWorkOverTime(uid,time,content,state)
    return data

def User_Leave(uid,time,content,state):
    u_o = User_operation()
    data = u_o._userLeave(uid,time,content,state)
    return data 

def User_BaseData(phone):
    u_o = User_operation()
    data = u_o._queryUserById(phone)
    if data is None:
        return None
    data = query2dict(data)
    return data

def Alluser_ClockData():
    u_o = User_operation()
    data = u_o._allUserClockData()
    data = query2dict(data)
    return data

def User_ClockData(uid):
    u_o = User_operation()
    data = u_o._userClockData(uid)
    data = query2dict(data)
    return data

def User_clock(uid,time,note):
    u_o = User_operation()
    # print(username,time,note)
    data = u_o._userClock(uid,time,note)

    return "ok"

def User_list():
    u_o = User_operation()
    data = u_o._all()
    # data（复杂对象）====> 数据
    # data = Class_To_Data(data,u_o.__fields__, 0)
    data = query2dict(data)
    return data


def User_reg(kwargs):
    u_o = User_operation()
    data = u_o._reg(kwargs)
   
    return "ok"

def User_update(username,datas):
    u_o = User_operation()
    data = u_o._userUpdate(username,datas)
   
    return "ok"

def User_isExisted(phone):  
    u_o = User_operation()
    data = u_o._queryUserById(phone)
    if data is None:
        return 0
    data = query2dict(data)
    return data 

def User_login(phone,pwd):
    u_o = User_operation()
    data = u_o._login(phone,pwd)
    if data is None:
        return "该用户不存在"
    # print(data)
    # data = Class_To_Data(data,u_o.__fields__, 1)
    data = query2dict(data)
    # print(name,pwd)
    print(data)
    if data['password'] != pwd:
        return "密码不正确"
    #  else
    return data