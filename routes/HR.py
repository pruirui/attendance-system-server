from flask import Blueprint,request,jsonify
from api.HR import *
import json,base64
import datetime
import os,random
from face.face_recognition import getFaceEmbedding
import numpy as np
HR = Blueprint('HR',__name__)

@HR.route('/usersInDepartment',methods = ['POST','GET']) 
def usersInDepartment():
    data = json.loads(request.data)
    departmentid = data['departmentid']
    datas = HR_FindAllUsersInDepartment(departmentid)
    if data is None:
        return jsonify({
            "code":1,
            # "length":length,
            "msg":"该部门暂无员工"
        })
    for data in datas:
        imgpath = data['headshot']
        with open(imgpath, 'rb') as f:
            image_data = f.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        print(data)
        data['headshot'] = encoded_image
    # length = len(data)
    return jsonify({
        "code":1,
        "length":len(datas),
        "data":data
    })

@HR.route('/createUserFace',methods = ['POST','GET'])
def createUserFace():
    # data = json.loads(request.data)
    uid = request.form['uid']
    img = request.files.get('file')
    data = HR_SearchUserFaceById(uid)
    savepath = './images/userfaces'
    username = str(uid) +'.jpg'
    userFacePath = os.path.join(savepath,username) 
    userFacePath = userFacePath.replace('\\', '/')
    print(userFacePath)
    img.save(userFacePath)
    faceEmbedding = getFaceEmbedding(userFacePath)  # 调用ai模型生成结果
    print ((len(faceEmbedding)))
    faceEmbedding = np.array(faceEmbedding)
    faceEmbedding = faceEmbedding.tobytes()
    updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(data)
    if data is not None:
        data = HR_UpdateUserFaceById(uid,faceEmbedding,updateTime)
        return jsonify({
            "code":1,
            "msg":"面部数据更新成功！"
        })
    
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

@HR.route('/updateDepartConfig',methods = ["POST","GET"])
def updateDepartConfig():
    datas = json.loads(request.data)
    departid = 3
    HR_updateDepartConfig(departid,datas)
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

@HR.route('/deleteDepartment',methods = ["POST","GET"]) #删除部门
def deleteDepartment():
    data = json.loads(request.data)
    departid = data['departmentid']
    data['departmentid'] = int(departid)
    
    HR_deleteDpartment(departid)
    return jsonify({
        "code":1,
        "msg":"部门已解散，人生有梦，各自精彩！"
    })


@HR.route('/createDepartment',methods = ["POST","GET"]) #创建部门
def createDepartment():
    data = json.loads(request.data)
    uid = 1
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['createTime'] = dateTmp
    data['state'] = '未审批'
    departid = random.randrange(100000,999999)
    print(departid)
    data['departmentid'] = int(departid)
    
    # print(data['departmentName'],dateTmp,data['description'],HRname)
    HR_createDpartment(uid,data)
    return jsonify({
        "code":1,
        "msg":"恭喜你，创建成功，请等候审核！！！"
    })

@HR.route('/ping',methods = ["GET"])
def ping():
    return "ok"