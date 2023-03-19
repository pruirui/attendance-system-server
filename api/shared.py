from operation.shared import Shared_operation

from utils.data_process import Class_To_Data,query2dict,time2string

def HR_addCreateDepartmentLog(datas):
    S_o = Shared_operation()
    data = S_o._addCreateDepartmentLog(datas)
    return data

def User_queryCreateLog(datas):
    S_o = Shared_operation()
    data = S_o._queryCreateLog(datas)
    if data is None:
        return None
    return query2dict(data)

def User_addInDepartmentLog(datas):
    S_o = Shared_operation()
    data = S_o._addInDepartmentLog(datas)
    return data

def All_queryLog(datas):
    S_o = Shared_operation()
    data = S_o._queryLog(datas)
    if data is None:
        return data
    return query2dict(data)