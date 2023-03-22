from sqlalchemy import or_
from models.shared import Applications
from db_config import session
from db_config import db_init as db

class Shared_operation():

    def _addInDepartmentLog(self,datas): #填入申请记录
        if datas['event'] == 'hr辞退员工':
            print("!!!")
            data = Applications.query.filter_by(state="待审批",sender_id=datas['HRuid'],process_id=datas['uid'],department_id=datas['departmentid'],event=datas['event']).first()
            if data is not None:
                return data
            new_data = Applications(sender_id=datas['HRuid'],process_id=datas['uid'],department_id=datas['departmentid'],create_time=datas['createtime'],\
                            event=datas['event'],description='暂无描述',state="待审批")
            session.add(new_data)
            session.commit()
        elif datas['event'] == 'hr邀请员工':
            print("!!!")
            data = Applications.query.filter_by(state="待审批",sender_id=datas['HRuid'],process_id=datas['uid'],department_id=datas['departmentid'],event=datas['event']).first()
            if data is not None:
                return data
            new_data = Applications(sender_id=datas['HRuid'],process_id=datas['uid'],department_id=datas['departmentid'],create_time=datas['createtime'],\
                            event=datas['event'],description='暂无描述',state="待审批")
            session.add(new_data)
            session.commit()
        else:
            new_data = Applications(sender_id=datas['uid'],department_id=datas['departmentid'],create_time=datas['createtime'],\
                                event=datas['event'],description='暂无描述',state="待审批")
            session.add(new_data)
            session.commit()
            print("???")

    def _queryLog(self,datas):
        data = Applications.query.filter_by(sender_id=datas['uid'],department_id=datas['departmentid']).all()
        return data

    def _queryCreateLog(self,datas):
        data = db.session.query(Applications).filter(Applications.sender_id==datas['uid'],Applications.event.like("%" + "公司" +"%"),\
                                       Applications.state=='待审批').all()
        return data
    
    def _addCreateDepartmentLog(self,datas):
        new_data = Applications(sender_id=datas['uid'],process_id=datas['process_id'],department_id=datas['departmentid'],create_time=datas['createTime'],\
                            event=datas['event'],description=datas['description'],state="待审批")
        session.add(new_data)
        session.commit()

    def _addDeleteDepartmentLog(self,datas):
        data = Applications.query.filter_by(sender_id=datas['uid'],\
                                department_id=datas['departmentid'],event=datas['event']).first()
        if data is not None:
            return data
        new_data = Applications(create_time=datas['createTime'],sender_id=datas['uid'],\
                                department_id=datas['departmentid'],event=datas['event'],state=datas['state'])
        session.add(new_data)
        session.commit()