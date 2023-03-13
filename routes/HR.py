from flask import Blueprint,request,jsonify
from api.HR import *
import json
import datetime
HR = Blueprint('HR',__name__)

@HR.route('/querySysConfig',methods = ["POST","GET"])
def querySysConfig():
    data = json.loads(request.data)
    data = HR_querySysConfig(data["departmentName"])
    if data is None:
        return jsonify({
        "code":-1,
        "msg":"该部门不存在！"
    })
    # print(type(data))
    data['clockInTime'] = data['clockInTime'].strftime('%H:%M:%S')
    data['clockOutTime'] = data['clockOutTime'].strftime('%H:%M:%S')
    # data = json.dumps(data)
    
    print(data)
    return jsonify(data)

@HR.route('/updateSysConfig',methods = ["POST","GET"])
def updateSysConfig():
    data = json.loads(request.data)
    departmentName = 'ikun'
    HR_updateSysConfig(departmentName,data["clockIn"],data["clockOut"])
    return jsonify({
        "code":1,
        "msg":"恭喜你，系统配置修改成功!"
    })

@HR.route('/addSysConfig',methods = ["POST","GET"])
def addSysConfig():
    data = json.loads(request.data)
    departmentName = 'ikun'
    dateIn = '8:00:00'
    dateOut = '121:00:00'
    HR_addSysConfig(departmentName,data["clockIn"],data["clockOut"])
    return jsonify({
        "code":1,
        "msg":"恭喜你，创建成功!"
    })

@HR.route('/createDepartment',methods = ["POST","GET"])
def createDepartment():
    data = json.loads(request.data)
    HRname = 'lee'
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(data['departmentName'],dateTmp,data['description'],HRname)
    HR_createDpartment(data["departmentName"],dateTmp,data["description"],HRname,'待审核')
    return jsonify({
        "code":1,
        "msg":"恭喜你，创建成功，请等候审核！！！"
    })
@HR.route('/ping',methods = ["GET"])
def ping():
    return "ok"