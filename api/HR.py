from operation.HR import HR_operation
from utils.data_process import query2dict

def HR_createDpartment(departmentName,time,description,HRname,state):
    HR_o = HR_operation()
    data = HR_o._createDepartment(departmentName,time,description,HRname,state)
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