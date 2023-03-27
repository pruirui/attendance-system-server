# # temp = '河北、山西、辽宁、吉林、黑龙江、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、海南、四川、贵州、云南、陕西、甘肃、青海、台湾、内蒙古、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京、天津、上海、重庆、香港特别行政区、澳门特别行政区'

# # print("\",\"".join(temp.split('、')))

# # data = {}
# #     # print("1")

# # from datetime import datetime, timedelta
 
# # def date_range(start_date, end_date):
# #     datelist = []
# #     for n in range(int((end_date - start_date).days)+1):
# #         datelist.append((start_date + timedelta(n)))
# #     return datelist

# # start_date = datetime(2023, 3, 1)  # 开始日期
# # end_date = datetime(2023, 3, 31)

# # res = (date_range(start_date,end_date))
# # print(res)

# # # -*- coding: utf-8 -*-
# # import random
# # import hashlib

# # import requests


# # def get_pic(pa,size=256):
# #     styles = ['identicon', 'monsterid', 'wavatar']
# #     random_str = ''.join([chr(random.randint(0x0000, 0x9fbf)) for i in range(random.randint(1, 25))])

# #     m1 = hashlib.md5("{}".format(random_str).encode("utf-8")).hexdigest()
# #     url = 'http://www.gravatar.com/avatar/{}?s={}&d={}'.format(m1, size, random.choice(styles))
# #     res = requests.get(url)
# #     with open(pa, 'wb')as f:
# #         f.write(res.content)
# # path = './images/headshots/'
# # for i in range(2,300):
# #     pa = path + str(i) + '.jpg'
# #     get_pic(pa)

# import json
# with open('json.json','rb') as user_file:
#   datas = user_file.read()

# datas = json.loads(datas)

# print(len(datas['provinces']))

# res = []

# for it in datas['provinces']:
#     # print(len(it),"it")
#     tmp = {}
#     tmp['value'] = it['provinceName']
#     tmp['label'] = it['provinceName']
#     child = []
#     for i in it['citys']:
#         # print(i)
#         city = {}
#         city['value'] = i['cityName']
#         city['label'] = i['cityName']
#         child.append(city)
#         # print(child)
#     tmp['children'] = child
# # print(tmp)
#     res.append(tmp)

# print(len(datas['provinces']),len(res))
# # res['value'] = 

# json_str = json.dumps(res,ensure_ascii=False)
# # res = res.__str__()
# with open("datas.json", "w",encoding="utf-8") as outfile:
#     outfile.write(json_str)


# import datetime
# data = {}
# data['date'] = "2023-1-1" + " 10:11:11"
# tmp = datetime.datetime.strptime(data['date'],'%Y-%m-%d %H:%M:%S')
# print(type(tmp),tmp)

# res = {'2023-03-01': None, '2023-03-02': None, '2023-03-03': None, '2023-03-04': None, '2023-03-05': None, '2023-03-06': None, '2023-03-07': None, '2023-03-08': None, '2023-03-09': None, '2023-03-10': None, '2023-03-11': None, '2023-03-12': None, '2023-03-16': None, '2023-03-17': None, '2023-03-18': None, '2023-03-19': None, '2023-03-23': None, '2023-03-13': '20:22:40', '2023-03-14': '15:12:16', '2023-03-15': '10:40:54', '2023-03-20': '15:38:50', '2023-03-21': '11:44:48', '2023-03-22': '09:15:04'}

# print(dict(sorted(res.items(), key=lambda x: x[0])))
res = {'12':{}}
res['12'] = 1