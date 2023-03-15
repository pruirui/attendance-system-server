from models.HR import HR_Department,HR_SysConfig,HR_UserFace
from models.shared import User_departments
from db_config import db_init as db
from db_config import session
from sqlalchemy import distinct
class HR_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _createDepartment(self,uid,datas):
        new_data = HR_Department(HRuid=uid,createTime=datas['createTime'],description=datas['description'],\
                                 departmentName=datas['departmentName'],state=datas['state'])
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
        print(data)
        print(type(data))
        return data
    
    def _updateUserfaceById(self,uid,faceEmbedding,updateTime):
        data = HR_UserFace.query.filter(HR_UserFace.id == uid).first()
        data.faceEmbedding = faceEmbedding
        data.updateTime = updateTime
        db.session.commit()
        # print(data)
        # print(type(data))
        return data
    
    def _FindUsersInDepartment(self,departid):
        data = User_departments.query.filter(User_departments.departmentid==departid).all()
        print(type(data),type(data[0]))
        return data