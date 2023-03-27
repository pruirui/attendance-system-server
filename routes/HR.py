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

@HR.route('/allDepartmentsClockData',methods = ['POST'])
def allDepartmentsClockData():
    datas = json.loads(request.data)
    print("datas",datas)
    datas['year'] = int(datas['months'].split('-')[0])
    datas['month'] = int(datas['months'].split('-')[1])
    if 'userid' in datas.keys() and datas['userid'] != '':
        print("!!!")
        datas['uid'] = datas['userid']
      
        # datas['month'] = '3'
        resIn,resOut = User_ClockData(datas)  #签到签退数据
        res = processUserClockData(datas,resIn,resOut)
        return jsonify({
            "code":1,
            "data":res
        })
    else:
        res = []
        resAllDepartments = {"zhexiantu":{}}
        chidaoSumAll,dakaSumAll,weidakaSumAll,zaotuiSumAll,wagesAll,makeUpAll,workOverAll = 0,0,0,0,0,0,0
        chidaoRateAll,dakaRateAll,weidakaRateAll,zaotuiRateAll = 0.0,0.0,0.0,0.0
        for it in datas['departmentids']: # 遍历每个部门
            datas['departmentid'] = it
            datas['querystring'] = ''
            res = HR_FindAllUsersInDepartment(datas)
            if res is None:
                continue
            for ittt in res:  #去掉boss
                if ittt['role'] == 'boss':
                    res.remove(ittt)
            
            chidaoSum,dakaSum,weidakaSum,zaotuiSum,daysSum = 0,0,0,0,0
            for itt in res:   #计算每个部门的数据
                datas['uid'] = itt['id']
                resIn,resOut = User_ClockData(datas)  #签到签退数据
                userClockRes = processUserClockData(datas,resIn,resOut)
                chidaoSum += userClockRes['bing']['chidao']
                dakaSum += userClockRes['bing']['daka']
                weidakaSum += userClockRes['bing']['weidaka']
                zaotuiSum += userClockRes['bing']['zaotui']
                chidaoSumAll += userClockRes['bing']['chidao']
                dakaSumAll += userClockRes['bing']['daka']
                weidakaSumAll += userClockRes['bing']['weidaka']
                zaotuiSumAll += userClockRes['bing']['zaotui']
                makeUpAll += userClockRes['bing']['qingjia']
                workOverAll += userClockRes['bing']['jiaban']
                wagesAll += userClockRes['bing']['xinzi']
            print("len(userClockRes['zhexiantu']['clockin'][0])",len(userClockRes['zhexiantu']['clockin'][0]))
            if(len(res) == 0):
                continue
            daysSum = len(userClockRes['zhexiantu']['clockin'][0]) * 2 * len(res)  #总天数
            chidaoRate = (round(chidaoSum / daysSum * 100,2))
            dakaRate = (round(dakaSum / daysSum * 100,2))
            weidakaRate = (round(weidakaSum / daysSum * 100,2))
            zaotuiRate = (round(zaotuiSum / daysSum * 100,2))
            depart = {}
            tmp = {}
            tmp['chidaoRate'] = chidaoRate
            tmp['dakaRate'] = dakaRate
            tmp['weidakaRate'] = weidakaRate
            tmp['zaotuiRate'] = zaotuiRate
            chidaoRateAll += round(chidaoSum / daysSum,4)
            dakaRateAll += round(dakaSum / daysSum,4)
            weidakaRateAll += round(weidakaSum / daysSum,4)
            zaotuiRateAll += round(zaotuiSum / daysSum,4)
            depart[str(it)] = tmp
            resAllDepartments['zhexiantu'][str(it)] = tmp   #每个部门的比率
            print('type(resAllDepartment',type(resAllDepartments['zhexiantu'][str(it)]))
        

        chidaoRateAll = "{:.2%}".format(round(chidaoRateAll / len(datas['departmentids']),4))
        dakaRateAll = "{:.2%}".format(round(dakaRateAll / len(datas['departmentids']),4))
        weidakaRateAll = "{:.2%}".format(round(weidakaRateAll / len(datas['departmentids']),4))
        zaotuiRateAll = "{:.2%}".format(round(zaotuiRateAll / len(datas['departmentids']),4))
        tmp = {}
        tmp["daka"] = dakaRateAll
        tmp["weidaka"] = weidakaRateAll
        tmp["chidao"] = chidaoRateAll
        tmp["zaotui"] = zaotuiRateAll
        tmp['xinzi'] = 0
        tmp['jiaban'] = 0
        tmp['qingjia'] = 0
        resAllDepartments['kapian'] = tmp
        tmp = {}
        tmp["daka"] = dakaSumAll
        tmp["weidaka"] = weidakaSumAll
        tmp["chidao"] = chidaoSumAll
        tmp["zaotui"] = zaotuiSumAll
        tmp['jiaban'] = 0
        tmp['qingjia'] = 0
        resAllDepartments['bing'] = tmp
        return jsonify({
            "code":1,
            "data":resAllDepartments
        })
        # 所有用户数据


@HR.route('/dismissUserInDepart',methods = ['POST'])
def dismissUserInDepart():
    datas = json.loads(request.data)
    print(datas)
    datetmp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datas['createtime'] = datetmp
    datas['event'] = '辞退员工'
    
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
    datas['event'] = '邀请员工'   #hr -> 

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
            # lee = random.randrange(1,300)
            # it['headshot'] = '/images/headshots/'+ str(lee) +'.jpg'
            lee = int(it['id']) % 300 + 1
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
    datas['event'] = 'boss授予用户权限'
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

@HR.route('/usersInDepartments',methods = ['POST'])   #查询boss所有部门员工
def usersInDepartments():
    datas = json.loads(request.data)
    print("datas",datas)
    datas['querystring'] = ''
    res = []
    for it in datas['departmentids']:
        datas['departmentid'] = it
        res += HR_FindAllUsersInDepartment(datas)
    for it in res:
        if it['role'] == 'boss':
            res.remove(it)
    if res is None:
        return jsonify({
            "code":1,
            # "length":length,
            "msg":"暂无员工"
        })
    return jsonify({
        "code":1,
        "data":res
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

    print("res",res)
    for data in res:   # 拿用户头像
        # imgpath = data['headshot']
        if data['headshot'] is None or not os.path.exists(data['headshot']):
            # lee = random.randrange(1,300)
            # print("data['uid']",data['uid'])
            lee = int(data['id']) % 300 + 1
            data['headshot'] = '/images/headshots/'+ str(lee) +'.jpg'
        else:
            data['headshot'] = data['headshot'][1:]
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
    data['event'] = 'boss创建公司'  # hr->boss
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