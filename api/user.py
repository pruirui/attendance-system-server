from operation.user import User_operation
from utils.data_process import Class_To_Data,query2dict,time2string
# from db_config import session

def User_isUidInDepartment(datas):
    u_o = User_operation()
    data = u_o._isUidInDepartment(datas)
    if data is not None:
        data = query2dict(data)
    return data

def User_addTodoLists(datas):
    u_o = User_operation()
    data = u_o._addUserTodoLists(datas)
    if data is not None:
        data = query2dict(data)
    return data

def User_updateTodoLists(datas):
    u_o = User_operation()
    data = u_o._updateUserTodoLists(datas)
    if data is not None:
        data = query2dict(data)
    return data

def User_queryTodoLists(datas):
    u_o = User_operation()
    data = u_o._queryUserTodoLists(datas)
    if data is not None:
        data = query2dict(data)
    return data

def User_queryFirstPage(datas):
    u_o = User_operation()
    data1,data2 = u_o._queryFirstPage(datas)
    if data1 is not None:
        data1 = query2dict(data1)
    if data2 is not None:
        data2 = query2dict(data2)
    return data1,data2
   
def User_updatePassword(datas):
    u_o = User_operation()
    res = u_o._updatePassword(datas)
    return res

def user_enterDepartmentNormal(datas):
    u_o = User_operation()
    res = u_o._enterDepartmentNormal(datas)
    return res

def user_queryApplicationById(id):
    u_o = User_operation()
    res = u_o._queryApplicationById(id)
    return query2dict(res)
 
def user_queryMyApplications(datas,idlist):
    u_o = User_operation()
    res = u_o._queryMyApplications(datas,idlist)
    if res is None:
        return None
    return query2dict(res)

def  user_QueryDepartmentDetail(datas):
    u_o = User_operation()
    data = u_o._queryDepartmentDetail(datas)
    if data is None:
        return None
    return query2dict(data)

def  user_QueryAllDepartments(datas):
    u_o = User_operation()
    data = u_o._quertAllDepartments(datas)
    if data is None:
        return None
    return query2dict(data)

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

def user_QueryEmbedding():
    u_o = User_operation()
    data = u_o._userQueryEmbedding()
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

def User_BaseData(uid):
    u_o = User_operation()
    data = u_o._queryUserById(uid)
    if data is None:
        return None
    data = query2dict(data)
    return data

def Alluser_ClockData():
    u_o = User_operation()
    data = u_o._allUserClockData()
    data = query2dict(data)
    return data

def User_ClockDayData(datas):
    u_o = User_operation()
    data1,data2 = u_o._userClockDayData(datas)
    if data1 is not None:
        data1 = query2dict(data1)
    if data2 is not None:
        data2 = query2dict(data2)
    return data1,data2

def User_queryOtherDatasLog(datas):
    u_o = User_operation()
    data1,data2 = u_o._queryOtherDatasLog(datas)
    if data1 is not None:
        data1 = query2dict(data1)
    if data2 is not None:
        data2 = query2dict(data2)
    return data1,data2

def User_ClockData(datas):
    u_o = User_operation()
    data1,data2 = u_o._userClockData(datas)
    if data1 is not None:
        data1 = query2dict(data1)
    if data2 is not None:
        data2 = query2dict(data2)
    return data1,data2

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
    data = u_o._queryUserByPhone(phone)
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
    if data['password'] not in (pwd['password'],pwd['password1']):
        return "密码不正确",0
    #  else
    
    return data,1