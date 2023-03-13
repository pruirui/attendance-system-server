
from flask import Blueprint,request,jsonify
user = Blueprint('user',__name__)

from api.user import *
import datetime

@user.route('/userUpdate',methods = ['POST'])
def userUpdate():
    username = 'lee'
    data = json.loads(request.data)
    print(data)
    # password = data['password']
    # phone = data['phone']
    # if data['aa'] is None:
        # print("none")
    User_update(username,data)
    return jsonify({
                "code":1,
                "msg":"修改成功!!!"
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
    uid = 1
    data = User_ClockData(uid)
    print(data[0])
    return jsonify(data)

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
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = User_queryClockBy(uid,dateTmp[:11],"签到")
    if data is not None:
        return jsonify({
            "code":-1,
            "msg":"今日已打卡，请勿重复打卡！"
        })
    print(dateTmp[11:])
    datefront = datetime.time(8,0,0).strftime('%H:%M:%S')
    dateend = datetime.time(10,0,0).strftime('%H:%M:%S')
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


@user.route('/login',methods=['GET','POST'])
def login():
    data = json.loads(request.data)
    phone = data['phone']
    pwd = data['password']
    data = User_login(phone,pwd)

    if data:
        return jsonify({
            "code":0,
            "msg":data
        })
    else:
        return jsonify({
            "code":1,
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
            "password":data["password"]
        })
        print(data)
        return ({
                "code": 0, 
                "msg": "恭喜，注册成功！"
            })
