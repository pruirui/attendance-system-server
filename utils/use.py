# temp = '河北、山西、辽宁、吉林、黑龙江、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、海南、四川、贵州、云南、陕西、甘肃、青海、台湾、内蒙古、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京、天津、上海、重庆、香港特别行政区、澳门特别行政区'

# print("\",\"".join(temp.split('、')))

data = {}
    # print("1")

from datetime import datetime, timedelta
 
def date_range(start_date, end_date):
    datelist = []
    for n in range(int((end_date - start_date).days)+1):
        datelist.append((start_date + timedelta(n)))
    return datelist

start_date = datetime(2023, 3, 1)  # 开始日期
end_date = datetime(2023, 3, 31)

res = (date_range(start_date,end_date))
print(res)