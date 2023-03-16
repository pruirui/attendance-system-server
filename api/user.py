from operation.user import User_operation
from utils.data_process import Class_To_Data,query2dict,time2string
# from db_config import session

def user_QueryDepartment(uid):
    u_o = User_operation()
    data = u_o._userQueryDepartment(uid)
    if data is None:
        return None
    data = query2dict(data)
    # print(data)
    # data[0]['createTime'] = time2string(data[0]['createTime'])
    # for it in data:
    #     # print(type(it),it)
    #     for i in it.values():
    #         print(type(i))
    #         i = time2string(i)
    #         print(type(i))
    # print("OOooo")
    return data

def user_QueryEmbedding(uid):
    u_o = User_operation()
    data = u_o._userQueryEmbedding(uid)
    if data is None:
        return None
    return query2dict(data)

def user_quitDepartment(datas):
    u_o = User_operation()
    data = u_o._userQuitDepartment(datas)
    return data

def user_applyDepartment(datas):
    u_o = User_operation()
    data = u_o._userApplyDepartment(datas)
    return data

def user_uploadHeadImg(uid,facepath):
    u_o = User_operation()
    data = u_o._userUploadImg(uid,facepath)
    return data

def User_queryClockBy(uid,date,note):
    u_o = User_operation()
    data = u_o._userClockByCondition(uid,date,note)
    if data is None:
        return None
    data = query2dict(data)
    return data

def User_MakeUpClock(datas):
    u_o = User_operation()
    data = u_o._userMakeUpClock(datas)
    return data

def User_WorkOverTime(datas):
    u_o = User_operation()
    data = u_o._userWorkOverTime(datas)
    return data

def User_Leave(datas):
    u_o = User_operation()
    data = u_o._userLeave(datas)
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
    if data is None:
        return None
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

def User_update(uid,datas):
    u_o = User_operation()
    data = u_o._userUpdate(uid,datas)
   
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
        return "该用户不存在",0
    # print(data)
    # data = Class_To_Data(data,u_o.__fields__, 1)
    data = query2dict(data)
    # print(name,pwd)
    print(data)
    if data['password'] != pwd:
        return "密码不正确",0
    #  else
    
    return data,1