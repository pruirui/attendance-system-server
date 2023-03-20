
from flask import Blueprint,request,jsonify
user = Blueprint('user',__name__)

from api.user import *
from api.shared import *
import datetime,os
import base64
from face.face_recognition import getFaceEmbedding,getdistance

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
    totals = len(res)
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
    print(type(data))
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
        "data":data
    })


@user.route('/userUpdate',methods = ['POST','GET'])
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
    uid = 1
    # dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = json.loads(request.data)
    datetimeTmp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    datetmp = datetime.datetime.strptime(data['date'],'%Y-%m-%d').strftime('%Y-%m-%d')
    print((datetmp))
    data['uid'] = uid
    data['event'] = '员工申请补打卡'
    data['makeup_clock'] = datetmp
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
    uid = 1
    datas = json.loads(request.data)
    dateTmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datas['create_time'] = dateTmp
    datas['uid'] = uid
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
    phone = '17365691811'
    data = User_BaseData(phone)
    data['birthday'] = data['birthday'].strftime("%Y-%m-%d")
    imgpath = data['headshot']
    with open(imgpath, 'rb') as f:
        image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')
    print(data)
    data['headshot'] = encoded_image
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
import numpy as np
@user.route('/clockIn',methods = ['GET','POST'])
def clockIn():
    # username = "lee"
    uid = 9
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
    path = './images/temp/' + str(uid) + '.' +  filename.split('.')[-1]
    userclockimg.save(path)
    # userclockimg = np.array(userclockimg)
    # print(len(userclockimg))
    # img = request.files.get('file')
    # userimgpath = './images/userfaces' + str(uid)
    res = user_QueryEmbedding(uid)
    userclockimg = np.array(getFaceEmbedding(path))
    for data in res:
        userfacembedding = np.frombuffer(data['faceEmbedding']).reshape(512)
        # cos_sim = np.dot(userclockimg,userfacembedding) / (np.linalg.norm(userclockimg) * np.linalg.norm(userfacembedding))
        distance = getdistance(userclockimg,userfacembedding)
        print("userface",type(userfacembedding[0]))
        print(distance)
    #匹配人脸
        if  distance:
           
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
    #不符合人脸数据库
    return jsonify({
                "code":-1,
                "msg":"人脸检测失败，请重新打卡！"
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
