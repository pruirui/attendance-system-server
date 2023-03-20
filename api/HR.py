from operation.HR import HR_operation
from utils.data_process import query2dict

def HR_queryDepartClockData(departid):
    H_o = HR_operation()
    data = H_o._QueryDepartmentClockData(departid)
    return query2dict(data)

def HR_updateDepartConfig(departid,datas):
    H_o = HR_operation()
    data = H_o._updateDepartConfig(departid,datas)
    if data is None:
        return None
    return query2dict(data)

def HR_FindAllUsersInDepartment(datas):
    H_o = HR_operation()
    data = H_o._FindUsersInDepartment(datas)
    print(type(data))
    if data is None:
        return None
    return query2dict(data)

def HR_UpdateUserFaceById(uid,faceEmbedding,updateTime):
    H_o = HR_operation()
    data = H_o._updateUserfaceById(uid,faceEmbedding,updateTime)
    return data

def HR_SearchUserFaceById(uid):
    H_o = HR_operation()
    data = H_o._searchUserfaceById(uid)
    if data is None:
        return None
    return query2dict(data)
    

def HR_addUserFace(uid,userFacePath,faceEmbedding,createTime,updateTime):
    H_o = HR_operation()
    data = H_o._addUserFace(uid,userFacePath,faceEmbedding,createTime,updateTime)
    return data

def HR_createDpartment(uid,datas): #创建部门
    HR_o = HR_operation()
    data = HR_o._createDepartment(uid,datas)
    return data

def HR_deleteDpartment(departid): #删除部门
    HR_o = HR_operation()
    data = HR_o._DeleteDepartment(departid)
    return data

def HR_addSysConfig(departmentName,clockIn,clockOut):
    HR_o = HR_operation()
    data = HR_o._addSysConfig(departmentName,clockIn,clockOut)
    return data

def HR_updateSysConfig(departmentName,clockIn,clockOut):
    HR_o = HR_operation()
    data = HR_o._updateSysConfig(departmentName,clockIn,clockOut)
    return data

def HR_querySysConfig(departmentName):
    HR_o = HR_operation()
    data = HR_o._querySysConfig(departmentName)
    if data is None:
        return None
    data = query2dict(data)
    return data