from models.user import Users,User_clocks
from models.shared import User_departments,Applications,Leaves
from models.HR import HR_UserFace,HR_Department
from db_config import session
from db_config import db_init as db
from sqlalchemy import extract, and_,or_
# 
class User_operation():
    def __init__(self):
        self.__fields__ = ['id','username','password'] 

    def _all(self):
        user_list =  Users.query.all()
        return user_list
    
    def _login(self,phone,pwd):
        user_list =  Users.query.filter_by(phone = phone).first()
        return user_list
    
    def _reg(self,kwargs):
        new_user = Users(id=kwargs['uid'],phone=kwargs["phone"],password=kwargs["password"],username=kwargs['username'])
        session.add(new_user)
        session.commit()
        # session.close()
    
    def _queryUserById(self,id):
        # if 'uid' in data.keys():
        user = Users.query.filter_by(id=id).first()
        return user
        # if 'phone' in data.keys():
        #     user = Users.query.filter_by(phone=data['phone']).first()
        #     return user
        
    def _queryUserByPhone(self,phone):
        # if 'uid' in data.keys():
        user = Users.query.filter_by(phone=phone).first()
        return user
    
    def _userUploadImg(self,uid,facepath):
        user = Users.query.filter(Users.id == uid).first()
        user.headshot = facepath
        db.session.commit()

    def _updatePassword(self,datas):
        user = Users.query.filter(Users.id == datas['uid']).first()
        user.password = datas['password']
        db.session.commit()

    def _userUpdate(self,uid,datas):
        user = Users.query.filter(Users.id == uid).first()
        if user:
            user.username = datas['username']
            user.password = datas['password']
            user.phone = datas['phone']
            user.address = datas['address']
            user.birthday = datas['birthday']
            user.motto = datas['motto']
            user.gender = datas['gender']
            user.home = datas['home']
            user.email = datas['email']
            db.session.commit()
        else:
            print("not found!")
        # session.close()
    
    def _userClock(self,uid,time,note):
        new_data = User_clocks(uid=uid,clockTime=time,note=note)
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userClockData(self,datas):
        # data_list = User_clocks.query.filter_by(uid=uid,).all()
        print(type(datas['month']))
        data_list_in = User_clocks.query.filter(User_clocks.note=='签到').filter(\
            and_(extract('month',User_clocks.clockTime) == datas['month'],extract('year',User_clocks.clockTime) == datas['year'])).\
            filter(User_clocks.uid==datas['uid']).all()
        data_list_out = User_clocks.query.filter(User_clocks.note=='签退').filter(\
            and_(extract('month',User_clocks.clockTime) == datas['month'],extract('year',User_clocks.clockTime) == datas['year'])).\
            filter(User_clocks.uid==datas['uid']).all()
                    # filter(User_clocks.uid==datas['uid']).all()
        # print(type(data_list))
        return data_list_in,data_list_out
    
    def _userClockByCondition(self,uid,date,note):
        print(date)
        data_list = User_clocks.query.filter(and_(\
            extract('year', User_clocks.clockTime) == date[:4],
            extract('month', User_clocks.clockTime) == date[5:7],\
            extract('day', User_clocks.clockTime) == date[8:]),User_clocks.uid==uid,User_clocks.note==note).first()
        return data_list
    
    def _allUserClockData(self):
        data_list = User_clocks.query.all()
        return data_list
    
    def _userLeave(self,datas):  #请假
        data = Applications.query.filter_by(sender_id=datas['uid'],state = '未审批',event='员工请假').first()
        if data is not None:
            return data
        new_data = Applications(sender_id=datas['uid'],create_time=datas['create_time'],content=datas['starttime']+datas['endtime'],\
                          event=datas['event'],state = '未审批',department_id=datas['departmentid'])
        session.add(new_data)
        session.commit()
        # session.close()

    def _userWorkOverTime(self,datas):  #加班
        if 'description' not in datas.keys():
            datas['description'] = '赞无描述'
        data = Applications.query.filter_by(sender_id=datas['uid'],\
                            event=datas['event'],description=datas['description'],state="待审批",content=datas['content']).first()
        if data is not None:
            return data
        
        new_data = Applications(sender_id=datas['uid'],create_time=datas['createtime'],\
                            event=datas['event'],description=datas['description'],state="待审批",content=datas['content'])
        session.add(new_data)
        session.commit()
        # session.close()
    
    def _userMakeUpClock(self,datas):  #补打卡
        # department_id=datas['departmentid']
        if 'description' not in datas.keys():
            datas['description'] = '赞无描述'
        data = Applications.query.filter_by(sender_id=datas['uid'],makeup_clock=datas['makeup_clock'],\
                            event=datas['event'],content=datas['content']).first()
        if data is not None:
            print("!!!")
            return data
        
        new_data = Applications(sender_id=datas['uid'],create_time=datas['createtime'],makeup_clock=datas['makeup_clock'],\
                            event=datas['event'],description=datas['description'],state="待审批",content=datas['content']\
                                ,department_id=datas['departmentid'])
        session.add(new_data)
        session.commit()
        # session.close()

    def _userApplyDepartment(self,datas): 
        new_data = User_departments(uid=datas['uid'],indate=datas['indate'],departmentid=datas['departmentid'],role="newer",state="待审核")
        session.add(new_data)
        session.commit()
        # session.close()

    def _userQuitDepartment(self,datas): 
        data = User_departments.query.filter_by(uid=datas['uid'],departmentid=datas['departmentid']).first()
        data.state = '离职'
        db.session.commit()
        # session.close()

    def _userQueryEmbedding(self):
        # data = HR_UserFace.query.filter_by(id=uid).first()
        datas = HR_UserFace.query.all()
        return datas
    
    def _userQueryDepartment(self,uid):   #用户所在部门
        # data = User_departments.query.filter_by(uid=uid).first()
        data = db.session.query(HR_Department.departmentid,HR_Department.createTime,HR_Department.state,HR_Department.description,\
                                HR_Department.departmentName,HR_Department.hourPay,HR_Department.workOverLimit,HR_Department.workOverPay,\
                                    HR_Department.startTime,HR_Department.endTime,HR_Department.workdays,User_departments.role,\
                                    HR_Department.address,HR_Department.rmb,HR_Department.phone,Users.username)\
                                        .filter(User_departments.uid==uid).filter(User_departments.uid==Users.id).filter\
            (HR_Department.departmentid==User_departments.departmentid).filter(User_departments.state=='在职').all()
        return data
    

    #  data = db.session.query(Users.username,Users.phone,Users.birthday,Users.password,Users.address,Users.motto,Users.gender,\
    #                              Users.home,Users.headshot,Users.email,User_departments.state).\
    #         filter(User_departments.departmentid==departid).\
    #         filter(Users.id==User_departments.uid).all()

    def _quertAllDepartments(self,datas):   #所有部门信息
        datas = db.session.query(HR_Department.departmentid,HR_Department.createTime,HR_Department.state,HR_Department.description,\
                                HR_Department.departmentName,HR_Department.hourPay,HR_Department.workOverLimit,HR_Department.workOverPay,\
                                    HR_Department.startTime,HR_Department.endTime,HR_Department.workdays,\
                                    HR_Department.address,HR_Department.rmb,HR_Department.phone,Users.username)\
                                        .filter(HR_Department.HRuid==Users.id).\
                                            filter(or_(HR_Department.departmentName.like('%'+ datas['departmentName']+'%'),Users.username.like('%'+ datas['departmentName']+'%')))\
                                                   .filter(HR_Department.address.like('%'+ datas['address']+'%')).all()
        
        return datas
    
    def _queryDepartmentDetail(self,data): # 部门详细信息
        data = db.session.query(HR_Department.departmentid,HR_Department.createTime,HR_Department.state,HR_Department.description,\
                                HR_Department.departmentName,HR_Department.hourPay,HR_Department.workOverLimit,HR_Department.workOverPay,\
                                    HR_Department.startTime,HR_Department.endTime,HR_Department.workdays,\
                                    HR_Department.address,HR_Department.rmb,HR_Department.phone,Users.username)\
                                        .filter(HR_Department.departmentid==data['departmentid']).\
                                            filter(HR_Department.HRuid==Users.id).all()
        return data
    def _queryMyApplications(self,datas,idlist): #查找申请事项
        # userdata = db.session.query().filter(Users.id==datas['uid']).first()
        res = Applications.query.filter(or_(Applications.sender_id==datas['uid'],Applications.process_id==datas['uid'],\
                                            Applications.department_id.in_(idlist))).all()

        return res

    def _queryApplicationById(self,id): #根据事项id查找内容
        res = Applications.query.filter_by(id=id).first()
        return res
    
    def _enterDepartmentNormal(self,datas): #处理个人审批事项（hr user admin）
        if datas['event'] == '员工申请补打卡':
            apply = Applications.query.filter_by(id=datas['id']).first()
            apply.apply_time = datas['apply_time']
            apply.state =datas['status']
            db.session.commit()
            if datas['status'] == '接受':
                new_data = User_clocks(uid=datas['uid'],note=datas['content'],clockTime=datas['date'])
                session.add(new_data)
                session.commit()

        elif datas['event'] == 'boss创建公司':    # hr -> boss
            apply = Applications.query.filter_by(id=datas['id']).first()
            apply.apply_time = datas['apply_time']
            apply.state =datas['status']
            db.session.commit()
            if datas['status'] == '接受':
                new_data = User_departments(uid=datas['uid'],departmentid=datas['departmentid'],role='boss',\
                                            indate=datas['apply_time'][:10],state='在职')
                session.add(new_data)
                session.commit()

                data = HR_Department.query.fiter_by(departmentid=datas['departmentid']).first()
                data.state = '已注册'
                db.session.commit()
        
        elif datas['event'] == '辞退员工':
            apply = Applications.query.filter_by(id=datas['id']).first()
            apply.apply_time = datas['apply_time']
            apply.state =datas['status']
            db.session.commit()
            if datas['status'] == '接受':
                User_departments.query.filter_by(uid=datas['uid'],departmentid=datas['departmentid'],role='user').delete()
                # session.add(new_data)
                db.session.commit()
            else:
                return
            
        elif datas['event'] == '邀请员工':
            apply = Applications.query.filter_by(id=datas['id']).first()
            apply.apply_time = datas['apply_time']
            apply.state =datas['status']
            db.session.commit()
            if datas['status'] == '接受':
                new_data = User_departments(uid=datas['uid'],departmentid=datas['departmentid'],role='user',\
                                            indate=datas['apply_time'][:10],state='在职')
                session.add(new_data)
                session.commit()
            else:
                return
        else:
            apply = Applications.query.filter_by(id=datas['id']).first()
            apply.apply_time = datas['apply_time']
            apply.process_id = datas['HRuid']
            apply.state =datas['status']
            db.session.commit()
            if datas['status'] == '接受':
                userdepart = User_departments.query.filter_by(uid=datas['uid'],departmentid=datas['departmentid']).first()
                userdepart.role = 'user'
                userdepart.state = '在职'
                db.session.commit()
            else:
                User_departments.query.filter_by(uid=datas['uid'],departmentid=datas['departmentid']).delete()
                db.session.commit()

    # def _RefuseEnterDepartmentNormal(self,datas): #拒绝员工进入公司
    #     apply = Applications.query.filter_by(id=datas['id']).first()
    #     apply.apply_time = datas['apply_time']
    #     apply.process_id = datas['HRuid']
    #     apply.state =datas['status']
    #     db.session.commit()
        
    #     userdepart