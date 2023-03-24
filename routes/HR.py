import shutil
from flask import Blueprint,request,jsonify
from api.HR import *
from api.shared import *
import json,base64
import datetime
import os,random
from face.face_recognition import getFaceEmbedding,detectFace
from routes.shared import *
import numpy as np
HR = Blueprint('HR',__name__)

# @HR.route('/queryDepartmentClock',methods = ['POST'])
# def queryDepartmentClock():
#     datas = json.loads(request.data)
#     datas['querystring'] = "" 
#     departusers = HR_FindAllUsersInDepartment(datas)
#     for user in departusers:


@HR.route('/dismissUserInDepart',methods = ['POST'])
def dismissUserInDepart():
    datas = json.loads(request.data)
    print(datas)
    datetmp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datas['createtime'] = datetmp
    datas['event'] = 'hr辞退员工'
    
    res = User_addInDepartmentLog(datas)
    if res:
        return jsonify({
            "code":-1,
            "msg":"请勿重复发送辞退申请！"
        })
    return jsonify({
        "code":1,
        "msg":"辞退成功，请等待员工确认！"
    })

@HR.route('/inviteUserJoinDepart',methods = ['POST'])
def inviteUserJoinDepart():
    datas = json.loads(request.data)
    print(datas)
    datetmp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datas['createtime'] = datetmp
    datas['event'] = 'hr邀请员工'

    res = User_addInDepartmentLog(datas)
    if res:
        return jsonify({
            "code":-1,
            "msg":"请勿重复邀请！"
        })
    return jsonify({
        "code":1,
        "msg":"邀请成功，请等待员工确认！"
    })

@HR.route('/queryAllUsers',methods = ['POST'])  #暂未加入公司的人
def queryAllUsers():
    datas = json.loads(request.data)
    print(datas)
    pageIndex = (datas['pageIndex']) - 1
    # print(type(datas['pageIndex']))
    pageSize = datas['pageSize']
    res = HR_queryAllUsers(datas)
    if res is None:
        totals = 0
        return jsonify({
            "code":-1,
            "msg":"暂无用户"
        })
    totals = len(res)
    sum = (len(res) + pageSize -1) // pageSize  #总页数
    last = pageSize*pageIndex + pageSize
    if pageIndex == sum:
        last = len(res)
    res = res[pageSize*pageIndex:last]


    for it in res:
        if it['headshot'] is None or os.path.exists(it['headshot'] is False):
            lee = random.randrange(1,300)
            it['headshot'] = '/images/headshots/'+ str(lee) +'.jpg'
        else:
            it['headshot'] = it['headshot'][1:]

    return jsonify({
        "code":1,
        "data":(res),
        "totals":totals
    })

@HR.route('/grantUserHR',methods=['POST'])
def grantUserHR():
    datas = json.loads(request.data)
    print(datas)
    datas['createTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datas['event'] = 'hr授予用户权限'
    datas['state'] = '已处理'
    HR_grantUserHR(datas)
    return jsonify({
        "code":1,
        "msg":"权限授予成功！"
    })

@HR.route('/applyDeleteDepartment',methods = ['POST','GET'])
def applyDeleteDepartment():
    datas = json.loads(request.data)
    datetmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datas['departmentid'] = int(datas['departmentid'])
    datas['event'] = 'hr删除公司'
    datas['createTime'] = datetmp
    datas['state'] = '待审批'
    
    res = HR_addDeleteDepartmentLog(datas)
    if res is not None:
        return jsonify({
            "code":-1,
            "msg":"已提交申请，请勿重复提交！"
        })
    return jsonify({
        "code":1,
        "msg":"申请已提交，请等待审核！"
    })

@HR.route('/departmentClockData',methods = ['POST','GET'])
def departmentClockData():
    data = json.loads(request.data)
    departmentid = data['departmentid']
    datas = HR_queryDepartClockData(departmentid)
    print(datas)
    return jsonify({
        "code":1,
        "data":datas
    })

@HR.route('/usersInDepartment',methods = ['POST','GET']) 
def usersInDepartment():
    datas = json.loads(request.data)
    # departmentid = datas['departmentid']
    print("datas",datas)
    pageIndex = (datas['pageIndex']) - 1
    # print(type(datas['pageIndex']))
    pageSize = datas['pageSize']
    
    # departmentName = data['departmentName']
    # address = data['address']
    res = HR_FindAllUsersInDepartment(datas)
    if res is None:
        return jsonify({
            "code":1,
            # "length":length,
            "msg":"该部门暂无员工"
        })
    totals = len(res)
    sum = (len(res) + pageSize -1) // pageSize  #总页数
    last = pageSize*pageIndex + pageSize
    print(last,pageIndex,sum)
    if pageIndex == sum:
        last = len(res)
    res = res[pageSize*pageIndex:last]

   
    for data in res:   # 拿用户头像
        # imgpath = data['headshot']
        if data['headshot'] is not None:
            imgpath = data['headshot']
            with open(imgpath, 'rb') as f:
                image_data = f.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                print(data)
                data['headshot'] = encoded_image
    # length = len(data)
    return jsonify({
        "code":1,
        "totals":totals,
        "data":res
    })

@HR.route('/createUserFace',methods = ['POST','GET'])
def createUserFace():
    # data = json.loads(request.data)
    uid = request.form['uid']
    # uid = data['uid']
    print("uid",uid)
    img = request.files.get('file')
    userimg = img
    data = HR_SearchUserFaceById(uid)
    tmppath = './images/test'
    savepath = './images/userfaces'
    username = str(uid) +'.jpg'
    userFacePath = os.path.join(savepath,username) 
    tmppath = os.path.join(tmppath,username) 
    userFacePath = userFacePath.replace('\\', '/')
    tmppath = tmppath.replace('\\', '/')
    print(userFacePath)

    # img.save(tmppath)
    
    userimg.save(tmppath)
    if not detectFace(tmppath):
        return jsonify({
            "code":-1,
            "msg":"为检测到人脸，请重新录入！"
        })
    shutil.move(tmppath,userFacePath)
    
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
    departid = datas['departmentid']

    workdays = (datas['workdays'])
    dictDate = {"星期一":1,"星期二":2,"星期三":4,"星期四":8,"星期五":16,"星期六":32,"星期日":64}
    tmp = 0
    for it in workdays:
        tmp += dictDate[it]
    datas['workdays'] = tmp
    print(datas['workdays'])
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
    data['uid'] = data['HRuid']
    uid = data['HRuid']
    print((data))
    # if isinstance(uid,int):
    #     return jsonify({
    #             "code":-1,
    #             "msg":"用户编号错误！"
    #         })
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if data['createTime'] is None:
        data['createTime'] = dateTmp
    else:
        data['createTime'] = datetime.datetime.strptime(data['createTime'], '%Y-%m-%d')

    data['state'] = '待审批'
    data['event'] = 'hr创建公司'
    data['process_id'] = 0
    departid = random.randrange(100000,999999)
    print(departid)
    data['departmentid'] = int(departid)
    res= User_queryCreateLog(data)
    if res is not None:
        res = res[-1]
        if res['event'] == "员工申请加入公司" or "hr创建公司":
            return jsonify({
                "code":-1,
                "msg":"您正在加入或创建新公司，请勿重复提交！"
            })
    # print(data['departmentName'],dateTmp,data['description'],HRname)
    data['rmb'] += '万'
    # data['workdays'] = int(data['workdays'])
    datalog = data
    datalog['description'] = '暂无描述'
    HR_addCreateDepartmentLog(datalog)
    workdays = data['workdays']
    dictDate = {"星期一":1,"星期二":2,"星期三":4,"星期四":8,"星期五":16,"星期六":32,"星期日":64}
    tmp = 0
    for it in workdays:
        tmp += dictDate[it]
    data['workdays'] = tmp
    HR_createDpartment(uid,data)
    return jsonify({
        "code":1,
        "msg":"恭喜你，创建成功，请等候审核！！！"
    })

@HR.route('/ping',methods = ["GET"])
def ping():
    return "ok"