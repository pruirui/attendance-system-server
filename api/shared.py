from operation.shared import Shared_operation

from utils.data_process import Class_To_Data,query2dict,time2string

def User_addInDepartmentLog(datas):
    S_o = Shared_operation()
    data = S_o._addInDepartmentLog(datas)
    return data

def All_queryLog(datas):
    S_o = Shared_operation()
    data = S_o._queryLog(datas)
    return data