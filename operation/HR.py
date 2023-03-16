from models.HR import HR_Department,HR_SysConfig,HR_UserFace
from models.shared import User_departments
from models.user import  Users,User_clocks
from db_config import db_init as db
from db_config import session
from sqlalchemy import distinct
from collections import OrderedDict
class HR_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _createDepartment(self,uid,datas):
        new_data = HR_Department(HRuid=uid,createTime=datas['createTime'],description=datas['description'],\
                                 departmentName=datas['departmentName'],state=datas['state'],departmentid=datas['departmentid'])
        session.add(new_data)
        session.commit()

    def _addSysConfig(self,departmentName,clockInTime,clockOutTime):
        new_data = HR_SysConfig(departmentName=departmentName,clockInTime=clockInTime,clockOutTime=clockOutTime)
        session.add(new_data)
        session.commit()

    def _updateSysConfig(self,departmentName,clockInTime,clockOutTime):
        config = HR_SysConfig.query.filter(HR_SysConfig.departmentName==departmentName)\
            .update({HR_SysConfig.clockInTime:clockInTime,HR_SysConfig.clockOutTime:clockOutTime})
        # config.clockInTime = clockInTime
        # config.clockOutTime = clockOutTime 
        db.session.commit()

    def _querySysConfig(self,departmentName):
        config = HR_SysConfig.query.filter_by(departmentName=departmentName).first()
        # tmp = str(config[1])
        print(config)
        return config
    
    def _addUserFace(self,uid,userFacePath,faceEmbedding,createTime,updateTime):
        new_data = HR_UserFace(id=uid,userFacePath=userFacePath,faceEmbedding=faceEmbedding,\
                               createTime=createTime,updateTime=updateTime)
        session.add(new_data)
        session.commit()

    def _searchUserfaceById(self,uid):
        data = HR_UserFace.query.filter_by(id=uid).first()
        # print(data['userFacePath'])
        print(type(data))
        return data
    
    def _updateUserfaceById(self,uid,faceEmbedding,updateTime):  #更新用户面部数据
        data = HR_UserFace.query.filter(HR_UserFace.id == uid).first()
        data.faceEmbedding = faceEmbedding
        data.updateTime = updateTime
        db.session.commit()
        # print(data)
        # print(type(data))
        return data
   
    def _updateDepartConfig(self,departid,datas):  #更新部门配置
        data = HR_Department.query.filter(HR_Department.departmentid == departid).first()
        # data.description = data['description']
        data.departmentName = datas['departmentName']
        data.hourPay = datas['hourPay']
        data.workOverPay = datas['workOverPay']
        data.workOverLimit = datas['workOverLimit']
        data.startTime = datas['startTime']
        data.endTime = datas['endTime']
        # data.workdays = datas['workdays']

        db.session.commit()
        return data
    
    def _DeleteDepartment(self,departid):  #删除部门
        data = HR_Department.query.filter(HR_Department.departmentid == departid).delete()
        # data.workdays = datas['workdays']
        
        db.session.commit()
        return data

    def _FindUsersInDepartment(self,departid):  # 查找部门所有员工
        # data = User_departments.query.filter(User_departments.departmentid==departid).all()
        data = db.session.query(Users.username,Users.phone,Users.birthday,Users.password,Users.address,Users.motto,Users.gender,\
                                 Users.home,Users.headshot,Users.email,User_departments.state).\
            filter(User_departments.departmentid==departid).\
            filter(Users.id==User_departments.uid).all()
        
        # print(dir(data1[0]),data1[0]._fields,data1[0]._data)
        # print((data1).__name__,type(data1[0]))
        # print(type(data),type(data[0]))
        print(data)
        return data
    
    def _QueryDepartmentClockData(self,departid): # 部门员工打卡数据
        data = db.session.query(User_departments.state,User_clocks.clockTime,User_clocks.note).\
            filter(User_departments.departmentid==departid).\
            filter(User_departments.uid==User_clocks.uid).all()
        print(data)
        return data