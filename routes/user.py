
from flask import Blueprint,request,jsonify
user = Blueprint('user',__name__)

from api.user import *
import datetime

@user.route('/userUpdate',methods = ['POST'])
def userUpdate():
    username = 'lee'
    data = json.loads(request.data)
    print(data)
    password = data['password']
    print(password)
    User_update(username,password)
    return jsonify({
                "code":1,
                "msg":"修改成功!!!"
            })

@user.route('/makeUpClock',methods = ['GET','POST'])
def userMakeUpClock():
    username = 'lee'
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_MakeUpClock(username,dateTmp,"补打卡","未处理")
    return "ok"

@user.route('/workOverTime',methods = ['GET','POST'])
def userWorkOverTime():
    username = 'lee'
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_WorkOverTime(username,dateTmp,"加班","未处理")
    return "ok"

@user.route('/leave',methods = ['GET','POST'])
def userLeave():
    username = 'lee'
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User_Leave(username,dateTmp,"请假","未处理")
    return "ok"

@user.route('/userBaseData',methods = ['GET','POST'])
def userBaseData():
    username = "lee"
    data = User_BaseData(username)
    print(data)
    return jsonify(data)

@user.route('/allUserClockData',methods = ['GET','POST'])
def allUserClockData():
    data = Alluser_ClockData()
    print(data[0])
    return jsonify(data)

@user.route('/userClockData',methods = ['GET','POST'])
def userClockData():
    username = "lee"
    data = User_ClockData(username)
    print(data[0])
    return jsonify(data)

@user.route('/clockOut',methods = ['GET','POST'])
def clockOut():
    username = "lee"
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datefront = '2023-03-11 21:00:00'
    dateend = '2023-03-11 23:59:59'
    if dateTmp < dateend and dateTmp > datefront:
        User_clock(username,dateTmp,"签退")
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
    username = "lee"
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(dateTmp)
    datefront = '2023-03-11 6:00:00'
    dateend = '2023-03-11 8:00:00'
    if dateTmp < dateend and dateTmp > datefront:
        User_clock(username,dateTmp,"签到")
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
    print(type(data))
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


@user.route('/login',methods=['GET'])
def login():
    name = request.args['username']
    pwd = request.args['password']
    data = User_login(name,pwd)

    if data:
        return jsonify({
            "code":-1,
            "msg":data
        })
    else:
        return jsonify({
            "code":0,
            "data":{
                "token":666666
            }
        })

import json

@user.route('/register',methods=['POST'])
def reg():
    data = json.loads(request.data)

    #判断用户是否存在
    cnt = User_isExisted(data['username'])
    print(type(cnt))
    if cnt:
       return ({
            "code": -1, 
            "msg": "用户已存在，请重新输入用户名"
        })
    else :      # 直接注册
        data = User_reg({
            "username":data["username"],
            "password":data["password"]
        })
        print(data)
        return ({
                "code": 200, 
                "msg": "恭喜，注册成功！"
            })
