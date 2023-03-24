
import calendar
from collections import defaultdict
import random
from flask import Blueprint,request,jsonify
user = Blueprint('user',__name__)

from api.user import *
from api.shared import *
from routes.shared import *
import datetime,os
import base64
from face.face_recognition import getFaceEmbedding,getdistance



@user.route('/manualClockIn',methods = ['POST'])
def manualClockIn():
    data = json.loads(request.data)
    uid = data['uid']
    datetmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = User_queryClockBy(data['uid'],datetmp[:11],"签退")
    if data is not None:
        return jsonify({
            "code":-1,
            "msg":"今日已打卡，请勿重复打卡！"
        })
    depart_data = user_QueryDepartment(uid) #用户角色
    datefront = depart_data[0]['startTime']
    
    User_clock(uid,datetmp,"签到")
    if datetmp[11:] < datefront :
        return jsonify({
                "code":1,
                "msg":"恭喜你,打卡成功!!!"
            })
    else:
        return jsonify({
                "code":1,
                "msg":"打卡成功，您已迟到!"
            })

@user.route('/processMyApplications',methods = ['POST'])
def processMyApplications():
    datas = json.loads(request.data)
    print('/processMyApplications',datas)
    id = datas['id']
    datetmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    datas['apply_time'] = datetmp
    res = user_queryApplicationById(id) #查出审批内容
    print("res",res)
    datas['departmentid'] = res['department_id']
    # datas['']
    if res['event'] is None:
        return jsonify({
            "code":-1,
            "msg":"输入处理事项类型！"
        })
    elif res['event'] == '员工申请加入公司':
        datas['event'] = res['event']
        datas['status'] = datas['state']
        datas['HRuid'] = datas['uid']
        datas['uid'] = res['sender_id']
        user_enterDepartmentNormal(datas)   
        return jsonify({
            "code":1,
            "msg":"您已"+ datas['status'] +"该员工加入公司！"
        })
    elif res['event'] == 'hr邀请员工':
        datas['status'] = datas['state']
        datas['event'] = res['event']
        user_enterDepartmentNormal(datas)
        return jsonify({
            "code":1,
            "msg":"您已"+ datas['status'] +"加入该公司！"
        })

    elif res['event'] == 'hr辞退员工':
        print(datas)
        datas['status'] = datas['state']
        datas['event'] = res['event']
        user_enterDepartmentNormal(datas)
        return jsonify({
            "code":1,
            "msg":"您已"+ datas['status'] +"辞退该公司！"
        })
    elif res['event'] == 'hr创建公司':
        datas['status'] = datas['state'] 
        datas['event'] = res['event']   
        datas['uid'] = res['sender_id']
        user_enterDepartmentNormal(datas)
        return jsonify({
            "code":1,
            "msg":"管理员已"+ datas['status'] +"创建公司！"
        })
    elif res['event'] == '员工申请补打卡':
        datas['uid'] = res['sender_id']
        datas['event'] = res['event']
        datas['status'] = datas['state'] 
        depart = user_QueryDepartmentDetail(res['departmentid'])[0]
        if res['content'] == '签到':
            datas['date'] =datas['date'] + " " + depart['startTime']  
        else :
            datas['date'] =datas['date'] + " " + depart['endTime']  
        user_enterDepartmentNormal(datas)
        return jsonify({
            "code":1,
            "msg":"HR已"+ datas['status'] +"申请补打卡！"
        })

@user.route('/queryMyApplications',methods = ['POST'])
def queryMyApplications():
    datas = json.loads(request.data)
    print("!!!!!!!!!",datas)
    # datetype = datas['type']
    # print(datas['uid'])

    depart = user_QueryDepartment(datas['uid'])
    idlist = []
    if depart is None:
        idlist = []
    else:
        # print(depart)
        for it in depart:
            if it['role'] == 'hr':
                idlist.append(it['departmentid'])
        # idlist = [it['departmentid'] for it in dapart if it['role'] == 'hr']
        # print("idlist",type(idlist[0]))

    res = user_queryMyApplications(datas,idlist)
    # print("!!!!!!!!!!!!!!!!",len(res))
    if res is None:
        return jsonify({
            "code":-1,
            "msg":"暂无审批记录！"
        })
    resdict = {'read':[],'unread':[],'down':[]}
    for it in res:
        # print((it))
        it['departmentid'] = it['department_id']
        # it['username'] = "暂无"
        depart = user_QueryDepartmentDetail(it)
        if depart is not None:
            departmentname = depart[0]['departmentName']
            it['departmentname'] = departmentname
        # print("process_id",it['process_id'])
        # print("sender_id",it['sender_id'])
        # if it['sender_id'] == int(datas['uid']):
            # print("process_id",it['process_id'])
        if it['process_id'] is None:
            # print("none")
            it['processname'] = '暂无'
        else:
            it['processname'] = User_BaseData(it['process_id'])['username']
        # elif it['process_id'] == int(datas['uid']):
        if it['sender_id'] is None:
            # print("none")
            it['sendername'] = '暂无'
        else:
            # print("it['sender_id']",it['sender_id'])
            res = User_BaseData(it['sender_id'])
            # print(res)
            it['sendername'] = User_BaseData(it['sender_id'])['username']

        if it['state'] == '待审批':
            if it['sender_id'] == int(datas['uid']):
                resdict['read'].append(it)
            else:
                resdict['unread'].append(it)
        else:
            resdict['down'].append(it)
    
    # print("!!!!!!!!!!!!!!",resdict['read'])
    resdict['down'] = resdict['down'][::-1]
    resdict['read'] = resdict['read'][::-1]
    resdict['unread'] = resdict['unread'][::-1]
    return jsonify({
        "code":1,
        "data":resdict
    })

@user.route('/queryDepartmentDetail',methods = ['POST','GET'])
def queryDepartmentDetail():
    data = json.loads(request.data)
    if data['departmentid'] is None:
        return jsonify({
            "code":-1,
            "msg":"部门编号错误！"
        })
    res = user_QueryDepartmentDetail(data)
    if res is None:
        return jsonify({
            "code":-1,
            "msg":"部门不存在！"
        })

    workdays = int(res[0]['workdays'])
    dictDate = {"星期一":1,"星期二":2,"星期三":4,"星期四":8,"星期五":16,"星期六":32,"星期日":64}
    dayslist = []
    for it in dictDate:
        if dictDate[it] & workdays:
        # print(it)
            dayslist.append(it)
        # tmp += dictDate[it]
    # res[0]['workdays'] = tmp
    res[0]['workdays'] = dayslist

    return jsonify({
        "code":1,
        "data":res[0]
    })

@user.route('/queryAllDepartments',methods = ['POST','GET'])
def queryAllDepartments():
    datas = json.loads(request.data)
    print(datas)
    # print(type(datas['pageIndex']))
    pageIndex = (datas['pageIndex']) - 1
    # print(type(datas['pageIndex']))
    pageSize = datas['pageSize']
    
    # departmentName = data['departmentName']
    # address = data['address']
    res = user_QueryAllDepartments(datas)
    if res is None:
        totals = 0
        return jsonify({
            "code":-1,
            "msg":"未检索到部门，请重新输入公司名称！"
        })
    else:
        totals = len(res)
    print(totals)
    
    sum = (len(res) + pageSize -1) // pageSize  #总页数
    last = pageSize*pageIndex + pageSize
    print(last,pageIndex,sum)
    if pageIndex == sum:
        last = len(res)
    res = res[pageSize*pageIndex:last]
    print(pageIndex,pageSize,pageSize*pageIndex,last,datas,totals)
    for it in res:
        it['createTime'] = it['createTime'][:10]
    if res is None:
        return jsonify({
            "code":-1,
            "msg":"未检索到部门，请重新输入公司名称！"
        })
    return jsonify({
        "code":1,
        "data":res,
        "totals":totals
    })

@user.route('/userInDepartment',methods = ['GET','POST'])
def userInDepartment():
    data = json.loads(request.data)
    uid = data['uid']
    # data['uid'] = uid
    data = user_QueryDepartment(uid)
    res = data
    print((data))
    if data is None:
        return jsonify({
            "code":-1,
            "msg":"该用户未加入公司！"
        })
    else: 
        data = data[-1]
        if data['state'] == '未审批':
            return jsonify({
                "code":-1,
                "msg":"用户待审核！"
            })
        elif data['state'] == '离职':
            return jsonify({
                "code":-1,
                "msg":"用户已离职！"
            })
    return jsonify({
        "code":1,
        "data":res
    })


@user.route('/userUpdate',methods = ['POST','GET'])
def userUpdate():
    data = json.loads(request.data)
    uid = data['uid']
    print(data)
    # password = data['password']
    # phone = data['phone']
    # if data['aa'] is None:
        # print("none")
    User_update(uid,data)
    return jsonify({
                "code":1,
                "msg":"用户信息更新成功!!!"
            })

@user.route('/userQuitDepartment',methods = ['GET','POST'])
def userQuitDepartment():
    data = json.loads(request.data)
    datetimeTmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    uid = 2
    data['uid'] = uid
    data['createtime'] = datetimeTmp
    data['event'] = '员工申请退出公司'
    data['description'] = '赞无描述'
    res = All_queryLog(data)
    if res is not None:
        return jsonify({
            "code":-1,
            "msg":"已提交申请，请勿重复提交！"
        })
    User_addInDepartmentLog(data)
    # user_quitDepartment(data)"msg":"人生有梦，各自精彩！"
    return jsonify({
            "code":1,
            "msg":"离职申请已提交，请等待审核！"
        })

@user.route('/userApplyDepartment',methods = ['GET','POST'])
def userApplyDepartment():
    data = json.loads(request.data)
    datetmp = datetime.date.today().strftime('%y-%m-%d')
    datetimeTmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    print(data)
    # uid = data['uid']a
    # data['uid'] = uid
    data['indate'] = datetmp
    datas = data
    datas['createtime'] = datetimeTmp
    # datas['applytime'] = None
    datas['event'] = '员工申请加入公司'
    datas['description'] = '赞无描述'
    res = All_queryLog(datas)
    if res is not None:
        print(type(res),len(res))
        res = res[-1]
        if res['state'] == '待审批':
            return jsonify({
                "code":-1,
                "msg":"已提交申请，请勿重复提交！"
            })
        elif res['event'] == '员工申请加入公司' and res['state'] == '已处理':
            return jsonify({
                "code":-1,
                "msg":"您已加入公司，请勿再次申请！"
            })
        elif res['event'] == 'hr创建公司':
            if res['state'] == '已处理':
                return jsonify({
                    "code":-1,
                    "msg":"您已拥有公司，请勿申请！"
                })
            return jsonify({
                "code":-1,
                "msg":"您的公司正在审批，请耐心等待！"
            })
        else:
            User_addInDepartmentLog(datas)
            user_applyDepartment(datas)
            return jsonify({
                    "code":1,
                    "msg":"申请成功，请等待HR审核！"
                })
    User_addInDepartmentLog(datas)
    user_applyDepartment(datas)
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待HR审核！"
        })
@user.route('/makeUpClock',methods = ['GET','POST'])
def userMakeUpClock():
    # dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = json.loads(request.data)
    print('data',data)
    print(type(data['departmentid']))
    datetimeTmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    datetmp = datetime.datetime.strptime(data['date'],'%Y-%m-%d').strftime('%Y-%m-%d')
    # depart = user_QueryDepartment(data['uid'])[0]
    # print((datetmp))
    data['event'] = '员工申请补打卡'
    # if data['content'] == '签到':
    #     data['makeup_clock'] = datetmp + " " +depart['startTime']
    # else:
    #    
    if data['content'] == 0:
        data['content'] = '签到'
        print("签到")
    else:
        data['content'] = '签退'
        print("签退")
        
    data['makeup_clock'] = data['date'] 
    data['createtime'] = datetimeTmp
    res = User_MakeUpClock(data)
    if res is not None:
        return jsonify({
            "code":-1,
            "msg":"申请已提交，请勿重复提交！"
        })
    return jsonify({
            "code":1,
            "msg":"补卡申请成功，请等待审核！"
        })

@user.route('/workOverTime',methods = ['GET','POST']) #申请加班
def userWorkOverTime():
    uid = 1
    data = json.loads(request.data)
    datetimeTmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    data['uid'] = uid
    data['event'] = '员工申请补加班'
    data['createtime'] = datetimeTmp

    res = User_WorkOverTime(data)
    if res is not None:
        return jsonify({
            "code":-1,
            "msg":"申请已提交，请勿重复提交！"
        })
    return jsonify({
            "code":1,
            "msg":"请假申请成功，请等待审核！"
        })

@user.route('/userLeave',methods = ['GET','POST'])
def userLeave():
    # uid = 1
    datas = json.loads(request.data)
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datas['create_time'] = dateTmp
    datas['event'] = '员工请假'
    # datas['uid'] = uid
    res = User_Leave(datas)
    if res is not None:
        return jsonify({
            "code":1,
            "msg":"申请已提交，请勿重复提交！"
        })
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待审核！"
        })

@user.route('/userBaseData',methods = ['GET','POST'])  #用户基本数据
def userBaseData():
    # phone = '17365691811'
    data = json.loads(request.data)
    uid = data['uid']
    
    data = User_BaseData(uid)
    depart_data = user_QueryDepartment(uid) #用户角色
    # print(depart_data)
    if depart_data is None:
        data['role'] = "newer"
    else:
        data['role'] = depart_data[0]['role']
    if uid == '0':
        data['role'] = "admin"
    if data is None:
        return jsonify({
            "code":-1,
            "msg":"用户编号错误!"
        })
    if data['birthday'] is not None:
        data['birthday'] = data['birthday'][:10]

    # if  os.path.exists(data['headshot']) is True:
    #     print("!!!")
    # print((os.path.exists(data['headshot'])))
    print(data['headshot'])
    if data['headshot'] is None or not os.path.exists(data['headshot']):
        # lee = random.randrange(1,300)
        # print("data['uid']",data['uid'])
        lee = int(uid) % 300 + 1
        data['headshot'] = '/images/headshots/'+ str(lee) +'.jpg'
    else:
        data['headshot'] = data['headshot'][1:]
    
    return jsonify({
        "code":1,
        "data":data
    })

@user.route('/allUserClockData',methods = ['GET','POST'])
def allUserClockData():
    data = Alluser_ClockData()
    print(data[0])
    return jsonify(data)

@user.route('/userClockInfo',methods = ['POST']) #个人考勤信息页面
def userClockInfo():
    datas = json.loads(request.data)
    print("datas",datas)
    # datas['month'] = '3'
    datas['year'] = int(datas['year'])
    resIn,resOut = User_ClockData(datas)  #签到签退数据
    res = processUserClockData(datas,resIn,resOut)
    return jsonify({
        "code":1,
        "data":res
    })

@user.route('/userClockData',methods = ['GET','POST']) #每月打卡数据-日历显示（我的打卡）
def userClockData():
    datas = json.loads(request.data)
    datas['year'] = '2023'
    print('/userClockData',datas)
    resIn,resOut = User_ClockData(datas)
    if resIn is None:
        resIn = []
    else:
        resIn = [it['clockTime'][:10] for it in resIn]
    if resOut is None:
        resOut = []
    else:
        resOut = [it['clockTime'][:10] for it in resOut]
    # print(resIn,resOut)
    def date_range(start_date, end_date):
        datelist = []
        for n in range(int((end_date - start_date).days)+1):
            datelist.append((start_date + datetime.timedelta(n)))
        return datelist
    
    res = {}
    # datas['month'] = int(datas['month'])
    datetmp = datetime.date.today()
    datetmp = datetmp.strftime("%Y-%m-%d").split('-')
    
    dateend = calendar.monthrange(2023, int(datas['month']))[1]  
    if int(datas['month']) == int(datetmp[1]):
        dateend = int(datetmp[-1])
    print(datetmp[1],dateend)
    start_date = datetime.datetime(2023, int(datas['month']), 1)  # 开始日期
    end_date = datetime.datetime(2023, int(datas['month']), dateend)
    # print(date_range(start_date,end_date))
    for it in (date_range(start_date,end_date)):
        if it.strftime("%Y-%m-%d") not in (resIn+resOut):
            # print(resIn,resOut)
            res[it.strftime("%Y-%m-%d")] = 3
        elif it.strftime("%Y-%m-%d") in (resIn) and it.strftime("%Y-%m-%d") in (resOut):
            res[it.strftime("%Y-%m-%d")] = 0
        elif it.strftime("%Y-%m-%d") in (resOut):
            res[it.strftime("%Y-%m-%d")] = 2
        else:
            res[it.strftime("%Y-%m-%d")] = 1
    # print(res)
    if res is None:
        return jsonify({
            "code":-1,
            "data":"无打卡数据"
        })
    return jsonify({
        "code":1,
        "data":res
    })

@user.route('/clockOut',methods = ['GET','POST'])
def clockOut():
    data = json.loads(request.data)
    uid = data['uid']
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = User_queryClockBy(uid,dateTmp[:11],"签退")
    if data is not None:
        return jsonify({
            "code":-1,
            "msg":"今日已打卡，请勿重复打卡！"
        })
    depart_data = user_QueryDepartment(uid) #用户角色
    # datefront = datetime.time(21,0,0).strftime('%H:%M:%S')
    # dateend = datetime.time(23,0,0).strftime('%H:%M:%S')
    dateend = depart_data[0]['endTime']
    if dateTmp[11:] > dateend:
        User_clock(uid,dateTmp,"签退")
        return jsonify({
                "code":1,
                "msg":"恭喜你,打卡成功!!!"
            })
    else:
        return jsonify({
                "code":1,
                "msg":"打卡成功，您已早退！"
            })
    
import numpy as np
@user.route('/clockIn',methods = ['GET','POST'])
def clockIn():
    # username = "lee"
    # uid = 9
    temp = 8888
    # if request.files.get('file') is None:
    #     return jsonify({
    #         "msg":"请选择图片！"
    #     })
    # data = json.loads(request.data)
    # print(type(data['file']))
    userclockimg = request.files.get('file')
    print(type(userclockimg))
    # filename = userclockimg.filename
    filename = userclockimg.filename
    print(filename)
    print((filename.split('.')))
    path = './images/temp/' + str(temp) + '.' +  filename.split('.')[-1]
    userclockimg.save(path)
    # userclockimg = np.array(userclockimg)
    # print(len(userclockimg))
    # img = request.files.get('file')
    # userimgpath = './images/userfaces' + str(uid)
    res = user_QueryEmbedding()
    userclockimg = np.array(getFaceEmbedding(path))
    for data in res:
        if data['faceEmbedding'] is None:
            continue
        # print(data['faceEmbedding'])
        userfacembedding = np.frombuffer(data['faceEmbedding']).reshape(512)
        # cos_sim = np.dot(userclockimg,userfacembedding) / (np.linalg.norm(userclockimg) * np.linalg.norm(userfacembedding))
        distance = getdistance(userclockimg,userfacembedding)
        print("userface",type(userfacembedding[0]))
        print(distance)
        #匹配人脸
        if  distance:
           
            #查询用户个人信息
            uid = data['id']
            print(uid)
            user_data = User_BaseData(uid) #用户个人信息
            depart_data = user_QueryDepartment(uid) #用户角色
            print(depart_data)
            if depart_data is None:
                user_data['role'] = "newer"
            else:
                user_data['role'] = depart_data[0]['role']
                
            # data['birthday'] = data['birthday'].strftime('%Y-%m-%d')
            imgpath = user_data['headshot']
            if imgpath == None:
                data['headshot'] = "未上传图片"
            else:
                with open(imgpath, 'rb') as f:
                    image_data = f.read()
                    encoded_image = base64.b64encode(image_data).decode('utf-8')
                print(data)
                user_data['headshot'] = encoded_image

            dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = User_queryClockBy(uid,dateTmp[:11],"签到")
            if data is not None:
                return jsonify({
                    "code":-1,
                    "msg":"今日已打卡，请勿重复打卡！",
                    "data":user_data
                })
            print(dateTmp[11:])
            # datefront = datetime.time(6,0,0).strftime('%H:%M:%S')
            datefront = depart_data[0]['startTime']
            # dateend = datetime.time(12,0,0).strftime('%H:%M:%S')
            dateend = depart_data[0]['endTime']
            if(dateTmp[11:] > datefront):
                print("ok")
            print(type('!!!'))
            User_clock(uid,dateTmp,"签到")
            if dateTmp[11:] < datefront :
                return jsonify({
                        "code":1,
                        "msg":"恭喜你,打卡成功!!!"
                    })
            else:
                return jsonify({
                        "code":-1,
                        "msg":"您已迟到!"
                    })
    #不符合人脸数据库
    return jsonify({
                "code":-1,
                "msg":"人脸检测失败或数据库无您人脸数据，请联系HR录入人脸！"
            })
        
   
@user.route('/list',methods=['GET'])
def list():
    # api的业务逻辑方法
    data = User_list()
    print((data))
    return jsonify(data)

@user.route("/userInfo", methods=["GET", "POST"])
def user_info():
    """
    获取当前用户信息
    :return:
    """
    token = request.headers.get("token")
    if token == "666666":
        return jsonify({
            "code": 1,
            "data": {
                "id": "1",
                "userName": "admin",
                "realName": "张三",
                "userType": 1
            }
        })
    return jsonify({
        "code": -1,
        "msg": "token不存在或已过期"
    })

@user.route('/updatePassword',methods = ['POST'])
def updatePassword():
    datas = json.loads(request.data)
    res = User_updatePassword(datas)

    return jsonify({
        "code":1,
        "msg":"密码修改成功！"
    })


@user.route('/uploadHeadImg',methods=['GET','POST'])
def uploadHeadImg():
    # datas = json.loads(request.data)
    # print(datas)
    uid = request.form['uid']
    img = request.files.get('file')
    print(uid,img)
    # img = request.files['file']
    # print(uid,img)
    savepath = './images/headshots'
    if img.filename[-4:] not in ['.jpg','.png','jpeg']:
        return jsonify({
            "code":-1,
            "msg":"请提交jpg、png、jpeg格式的图片!"
        })
    filename = str(uid) + img.filename[-4:]
    userFacePath = os.path.join(savepath,filename) 
    print(img)
    userFacePath = userFacePath.replace('\\', '/')
    print(userFacePath)
    img.save(userFacePath)
    # data = user_uploadHeadImg(uid,userFacePath)
    user_uploadHeadImg(uid,userFacePath)
    return jsonify({
        "code":1,
        "msg":"用户头像添加成功！！！"
    })

@user.route('/login',methods=['GET','POST'])
def login():
    # token = request.headers['Authorization']
    # print(token)
    # return jsonify({
    #     "data":token
    # })
    data = json.loads(request.data)
    phone = data['phone']
    pwd = data['password']
    data,flag = User_login(phone,pwd)
    # data = jsonify(data)
    if flag:
        uid = data['id']
        depart_data = user_QueryDepartment(uid)
        print(depart_data)
        if depart_data is None:
            data['role'] = "newer"
        else:
            data['role'] = depart_data[0]['role']
        # data['birthday'] = data['birthday'].strftime('%Y-%m-%d')
        imgpath = data['headshot']
        if data['phone'] == 'admin':
            data['role'] = 'admin'
        if imgpath == None:
            data['headshot'] = "未上传图片"
        else:
            with open(imgpath, 'rb') as f:
                image_data = f.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
            print(data)
            data['headshot'] = encoded_image
        # print(type(data['birthday']))
        # data.pop('headshot') 
        return jsonify({
            "code":1,
            "msg":"登陆成功",
            "data":(data)
        })
    else:
        print(data)
        return jsonify({
            "code":-1,
            "msg":data,
            "data":{
                "token":666666
            }
        })

import json

@user.route('/register',methods=['POST'])
def reg():
    data = json.loads(request.data)

    #判断用户是否存在
    cnt = User_isExisted(data['phone'])
    print(type(cnt))
    if cnt:
       return ({
            "code": -1, 
            "msg": "用户已存在，请重新输入手机号"
        })
    else :      # 直接注册
        uid = random.randrange(100000,999999)
        data = User_reg({
            "uid":uid,
            "phone":data["phone"],
            "password":data["password"],
            "username":data['username']
        })
        print(data)
        return ({
                "code": 1, 
                "msg": "恭喜你，注册成功！"
            })
