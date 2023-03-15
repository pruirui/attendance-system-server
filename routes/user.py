
from flask import Blueprint,request,jsonify
user = Blueprint('user',__name__)

from api.user import *
import datetime,os

@user.route('/userUpdate',methods = ['POST'])
def userUpdate():
    uid = 1
    data = json.loads(request.data)
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
    uid = 2
    data['uid'] = uid
    user_quitDepartment(data)
    return jsonify({
            "code":1,
            "msg":"人生有梦，各自精彩！"
        })

@user.route('/userApplyDepartment',methods = ['GET','POST'])
def userApplyDepartment():
    data = json.loads(request.data)
    datetmp = datetime.date.today().strftime('%y-%m-%d')
    print(datetmp)
    uid = 3
    data['uid'] = uid
    data['indate'] = datetmp
    user_applyDepartment(data)
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待HR审核！"
        })
    
@user.route('/makeUpClock',methods = ['GET','POST'])
def userMakeUpClock():
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_MakeUpClock(uid,dateTmp,"补打卡","未处理")
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待审核！"
        })

@user.route('/workOverTime',methods = ['GET','POST'])
def userWorkOverTime():
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_WorkOverTime(uid,dateTmp,"加班","未处理")
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待审核！"
        })

@user.route('/leave',methods = ['GET','POST'])
def userLeave():
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_Leave(uid,dateTmp,"请假","未处理")
    return jsonify({
            "code":1,
            "msg":"申请成功，请等待审核！"
        })

@user.route('/userBaseData',methods = ['GET','POST'])
def userBaseData():
    phone = '17365691811'
    data = User_BaseData(phone)
    print(data)
    return jsonify(data)

@user.route('/allUserClockData',methods = ['GET','POST'])
def allUserClockData():
    data = Alluser_ClockData()
    print(data[0])
    return jsonify(data)

@user.route('/userClockData',methods = ['GET','POST'])
def userClockData():
    uid = 3
    data = User_ClockData(uid)
    print((data))
    if data is None:
        return jsonify({
            "code":1,
            "data":"无打卡数据"
        })
    return jsonify({
        "code":1,
        "data":data
    })

@user.route('/clockOut',methods = ['GET','POST'])
def clockOut():
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = User_queryClockBy(uid,dateTmp[:11],"签退")
    if data is not None:
        return jsonify({
            "code":-1,
            "msg":"今日已打卡，请勿重复打卡！"
        })
    datefront = datetime.time(21,0,0).strftime('%H:%M:%S')
    dateend = datetime.time(23,0,0).strftime('%H:%M:%S')
    if dateTmp[11:] < dateend and dateTmp[11:] > datefront:
        User_clock(uid,dateTmp,"签退")
        return jsonify({
                "code":1,
                "msg":"恭喜你,打卡成功!!!"
            })
    else:
        return jsonify({
                "code":-1,
                "msg":"打卡失败,未到签退时间!"
            })

@user.route('/clockIn',methods = ['GET','POST'])
def clockIn():
    # username = "lee"
    uid = 1
    # userimg = request.files.get('file')

    #匹配人脸

    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = User_queryClockBy(uid,dateTmp[:11],"签到")
    if data is not None:
        return jsonify({
            "code":-1,
            "msg":"今日已打卡，请勿重复打卡！"
        })
    print(dateTmp[11:])
    datefront = datetime.time(8,0,0).strftime('%H:%M:%S')
    dateend = datetime.time(20,0,0).strftime('%H:%M:%S')
    if(dateTmp[11:] > datefront):
        print("ok")
    print(type('!!!'))
    if dateTmp[11:] < dateend and dateTmp[11:] > datefront:
        User_clock(uid,dateTmp,"签到")
        return jsonify({
                "code":1,
                "msg":"恭喜你,打卡成功!!!"
            })
    else:
        return jsonify({
                "code":-1,
                "msg":"打卡失败,未到签到时间!"
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

@user.route('/uploadHeadImg',methods=['GET','POST'])
def uploadHeadImg():
    uid = '1'
    img = request.files.get('file')
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
    return jsonify({
        "code":1,
        "msg":"用户头像添加成功！！！"
    })

@user.route('/login',methods=['GET','POST'])
def login():
    data = json.loads(request.data)
    phone = data['phone']
    pwd = data['password']
    data,flag = User_login(phone,pwd)
    data['birthday'] = data['birthday'].strftime('%Y-%m-%d')
    print(type(data['birthday']))
    data.pop('headshot')   
    # data = jsonify(data)
    if flag:
        return jsonify({
            "code":1,
            "msg":"登陆成功",
            "data":(data)
        })
    else:
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
            "msg": "用户已存在，请重新输入用户名"
        })
    else :      # 直接注册
        data = User_reg({
            "phone":data["phone"],
            "password":data["password"],
            "username":data['username']
        })
        print(data)
        return ({
                "code": 1, 
                "msg": "恭喜你，注册成功！"
            })
