from models.HR import HR_Department,HR_SysConfig,HR_UserFace
from db_config import db_init as db
from db_config import session

class HR_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _createDepartment(self,departmentName,time,description,HRname,state):
        new_data = HR_Department(HRname=HRname,createTime=time,description=description,\
                                 departmentName=departmentName,state=state)
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