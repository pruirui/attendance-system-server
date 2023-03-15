from flask import Blueprint,request,jsonify
from api.HR import *
import json
import datetime
import os
HR = Blueprint('HR',__name__)

@HR.route('/usersInDepartment',methods = ['POST','GET'])
def usersInDepartment():
    data = json.loads(request.data)
    departmentid = data['departmentid']
    data = HR_FindAllUsersInDepartment(departmentid)
    return jsonify({
        "code":1,
        "data":data
    })

@HR.route('/createUserFace',methods = ['POST','GET'])
def createUserFace():
    # data = json.loads(request.data)
    uid = request.form['uid']
    img = request.files.get('file')
    data = HR_SearchUserFaceById(uid)
    faceEmbedding = ""  # 调用ai模型生成结果
    updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(data)
    if data is not None:
        data = HR_UpdateUserFaceById(uid,faceEmbedding,updateTime)
        return jsonify({
            "code":1,
            "msg":"面部数据更新成功！"
        })
    savepath = './images'
    username = str(uid) +'.jpg'
    print(username)
    userFacePath = os.path.join(savepath,username) 
    userFacePath = userFacePath.replace('\\', '/')
    print(userFacePath)
    img.save(userFacePath)
    createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updateTime = createTime
    
    data = HR_addUserFace(uid,userFacePath,faceEmbedding,createTime,updateTime)
    return jsonify({
        "code":1,
        "msg":"添加成功！！！"
    })

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
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['createTime'] = dateTmp
    data['state'] = '未审批'
    # print(data['departmentName'],dateTmp,data['description'],HRname)
    HR_createDpartment(uid,data)
    return jsonify({
        "code":1,
        "msg":"恭喜你，创建成功，请等候审核！！！"
    })
@HR.route('/ping',methods = ["GET"])
def ping():
    return "ok"