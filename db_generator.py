#coding=utf-8
import string
import numpy as np
 
# a=np.arange(15).reshape(3,5)
# print (a)
# b=a.tobytes()
# print ((b))
# c=np.frombuffer(b,np.int32).reshape(3,5)
# print (c)

from faker import Factory
from faker import Faker
import mysql.connector
from mysql.connector import Error
from faker import Faker
import random,datetime

fake2 = Faker()
fake = Faker('zh_CN')

def generate_password(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))

def description(name):
    # 科技公司名称
    company_name = random.choice(['智能科技', '创新科技', '未来科技', '先进科技', '高科技'])

    # 公司定位
    company_position = random.choice(['人工智能', '区块链', '大数据', '云计算', '物联网'])

    # 公司口号
    slogan = random.choice(['让世界更智能', '打造数字未来', '数据驱动商业', '连接万物', '智能改变生活'])
    
    # 科技公司名称列表
    company_names = ['智能科技', '未来科技', '新兴科技', '数字科技', '创新科技', '科技未来', '智能未来', '科技创新', '未来创新']

    # 科技公司定位列表
    company_positions = ['人工智能', '区块链', '云计算', '大数据', '物联网', '智能家居', '机器学习', '虚拟现实', '增强现实']

    # 科技公司描述列表
    company_descriptions = ['致力于为用户提供最好的{}服务', '专注于{}领域的创新研发', '打造智能{}应用的领先品牌', '为企业提供{}解决方案的专业团队', '引领{}技术的发展方向', '将{}技术应用于智能家居领域', '致力于推动{}技术的商业化运用', '为用户提供领先的{}技术解决方案', '将{}技术应用于虚拟现实领域']

    # 随机生成科技公司名称、定位和描述
    company_name = random.choice(company_names)
    company_position = random.choice(company_positions)
    company_description = random.choice(company_descriptions).format(company_position)

    # 输出科技公司描述
    tmp = ('{}是我们的主要定位，{}'.format( company_position, company_description))


    # 公司介绍
    company_intro = f'{name}是一家专注于{company_position}领域的科技公司，致力于{random.choice(["推动行业发展", "提升生产力", "改善人类生活"])}, {slogan}是我们的口号;'

    res = company_intro+tmp
    return  res

def randomtimes(start, end, n, frmt="%Y-%m-%d %H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime=[random.random() * (etime - stime) + stime for _ in range(n)]
    time_str=[t.strftime(frmt) for t in time_datetime]
    return time_str[0]

def randomdates(start, end, n, frmt="%Y-%m-%d"):
    stime = datetime.date.strftime(start, frmt)
    etime = datetime.date.strftime(end, frmt)
    time_datetime=[random.random() * (etime - stime) + stime for _ in range(n)]
    time_str=[t.strftime(frmt) for t in time_datetime]
    return time_str[0]

def fixphone():
    area_code = ['010', '021', '022', '023', '024', '025', '027', '028', '029', '020', '0755', '0756', '0731', '0734', '0771', '0772', '0791', '0799', '0898']  # 地区码
    prefix = random.choice(area_code)  # 随机选择一个地区码
    suffix = ''.join(str(random.randint(0, 9)) for _ in range(8))  # 随机生成8位号码

    telephone = prefix + '-' + suffix  # 组合成完整的电话号码
    return (telephone)

def generator():
    try:
        conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                passwd="liyuanhang",
                database = "clock"
            )
        # print("okok")
        if conn.is_connected():
            cursor = conn.cursor()
            row = {}
            n = 0
            sdatetmp = ['6:00:00','7:00:00','8:00:00','9:00:00','10:00:00','11:00:00']
            edatetmp = ['16:00:00','17:00:00','18:00:00','19:00:00','20:00:00','21:00:00','22:00:00','23:00:00']

            cursor.execute(' \
                    SELECT departmentid FROM `departments`')
            # print(type(res))
            departments = cursor.fetchall()
            # print((res[0][0]))
            for i in range(1):
                n += 1
              
                # departments
                departmentname = fake.company()[:-4] + "团队"
                uid = random.randrange(100000,999999)  
                departmentid = random.randrange(10000000,99999999)
                create_time = randomtimes('2015-11-01 07:00:00','2023-3-25 09:00:00',1)
                stat = '已注册'
                descri = description(departmentname)
                hourpay = random.randrange(10,50)
                workOverPay = random.randrange(30,150)
                workOverLimit = random.randrange(0,5)
                startTime = sdatetmp[random.randrange(0,6)]
                startTime = datetime.datetime.strptime(startTime,'%H:%M:%S').strftime('%H:%M:%S')
                endTime = edatetmp[random.randrange(0,8)]
                endTime = datetime.datetime.strptime(endTime,'%H:%M:%S').strftime('%H:%M:%S')
                print(type(endTime))
                workdays = random.randint(0,128)
                phone = fixphone()
                address = fake.address()
                rmb = str(random.randrange(50,10000)) + '万'

                # users_hr
                username = fake.name()
                password = generate_password(10)
                userphone = fake.phone_number()
                useraddress = fake.address().split('座')[0][:-1]
                birthday = fake.date_of_birth(minimum_age=20, maximum_age=35)
                motto = fake2.sentence(nb_words=6, variable_nb_words=True)
                gender = ['男','女'][random.randrange(2)]
                home = useraddress
                flag = [0,1][random.randrange(2)]
                headshot ='/images/headshots/' + str(uid) + '.jpg'
                email = fake.email().replace('example',['google','163','qq','122','facebook','bytes'][random.randrange(6)])
                
                # user_departments
                role = 'user'
                indate = create_time[:10]
                state = '在职'

                row = [fake.first_name(), fake.last_name(), fake.email(), \
                fake.postcode(), fake.city(), fake.country(), fake.date_of_birth(),uid,create_time,\
                    stat]
                
                cursor.execute(' \
                    INSERT INTO `users` (id, username,password,phone,address,birthday,\
                                motto,gender,home,flag,headshot,email) \
                    VALUES (%s, "%s", "%s", "%s", "%s", "%s", "%s","%s", "%s", %s, "%s", "%s"); \
                    ' % (uid,username,password,userphone,useraddress,birthday,motto,gender,home,\
                         flag,headshot,email))
                # cursor.execute(' \
                #     INSERT INTO `departments` (departmentid, HRuid, createTime, state, description, departmentName,\
                #                 hourPay,workOverPay,workOverLimit,startTime,endTime,workdays,phone,address,rmb) \
                #     VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s", "%s","%s"); \
                #     ' % (departmentid,uid,create_time,stat,descri,departmentname,hourpay,workOverPay,workOverLimit,\
                #          startTime,endTime,workdays,phone,address,rmb))
                departmentid = 52138690
                cursor.execute(' \
                    INSERT INTO `user_departments` (uid,departmentid,role,indate,state)\
                    VALUES (%s, %s, "%s", "%s", "%s"); \
                    ' % (uid,departmentid,role,indate,state))
                
               
                        
                def date_range(start_date, end_date):
                    datelist = []
                    for n in range(int((end_date - start_date).days)+1):
                        datelist.append((start_date + datetime.timedelta(n)))
                    return datelist
                start_date = datetime.datetime(2023, 1, 1)  # 开始日期
                end_date = datetime.datetime(2023, 3, 26) #结束时间
                for lee in (date_range(start_date,end_date)):#每个员工1月起打卡记录
                    # for x in range(2):
                    startIn = lee.strftime("%Y-%m-%d")+ " " + "07:00:00"
                    endIn = lee.strftime("%Y-%m-%d")+ " " + "11:00:00"
                    startOut = lee.strftime("%Y-%m-%d")+ " " + "15:00:00"
                    endOut = lee.strftime("%Y-%m-%d")+ " " + "23:59:59"
                    clockInTime = randomtimes(startIn,endIn,1)
                    clockOutTime = randomtimes(startOut,endOut,1)
                    # print(clockTime)
                    tmp = random.randrange(100)
                    if tmp >= 5:
                        cursor.execute(' \
                            INSERT INTO `user_clocks` (uid,clockTime,note)\
                            VALUES ( %s, "%s", "%s"); \
                            ' % (uid,clockInTime,'签到'))
                    
                    tmp = random.randrange(100)
                    if tmp >= 5:
                        cursor.execute(' \
                            INSERT INTO `user_clocks` (uid,clockTime,note)\
                            VALUES ( %s, "%s", "%s"); \
                            ' % (uid,clockOutTime,'签退'))
                #user_others
                # for lee in range(30):  # 每个部门30个员工
                #     uid = random.randrange(100000,999999) 
                #     username = fake.name()
                #     password = generate_password(10)
                #     userphone = fake.phone_number()
                #     useraddress = fake.address().split('座')[0][:-1]
                #     birthday = fake.date_of_birth(minimum_age=20, maximum_age=35)
                #     motto = fake2.sentence(nb_words=6, variable_nb_words=True)
                #     gender = ['男','女'][random.randrange(2)]
                #     home = useraddress
                #     flag = [0,1][random.randrange(2)]
                #     headshot ='./images/headshots/' + str(uid) + '.jpg'
                #     email = fake.email().replace('example',['google','163','qq','122','facebook','bytes'][random.randrange(6)])
                #     # user_departments users
                #     for x in range(1,29): #每个员工30天打卡记录
                #         clockTime = randomtimes('2023-2-01 07:00:00','2023-2-01 09:00:00',1)

            conn.commit()
            cursor.close()
            conn.close()
    except Error as e :
        print ("error", e)
        pass
    except Exception as e:
        print ("Unknown error %s", e)
    # finally:
        #closing database connection.
    # if(conn and conn.is_connected()):
    
        
# fake = Factory.create()

if __name__ == '__main__' :

    # tmp = [fake.profile() for _ in range(10)]
    # print(tmp)
    # def generate_password(length):
    #     letters = string.ascii_letters + string.digits
    #     return ''.join(random.choice(letters) for i in range(length))
    # # print(randomtimes('2015-11-01 07:00:00','2023-3-25 09:00:00',1))
    # # # print(description(fake.company()) )  
    # tmp = fake.address()
    # print(fake2.sentence(nb_words=6, variable_nb_words=True))
    # print('./images/headshots/' + str('112313') + '.jpg') 
    # # print(random.randrange(1,5))
    # print(fake.email().replace('example',['google','163','qq','122','facebook','bytes'][random.randrange(6)]))
    # print(randomtimes('2023-2-26 06:00:00','2023-2-26 11:00:00',1))
    # print(fake.company()[:-4] + "团队")
    generator()
    
    
   