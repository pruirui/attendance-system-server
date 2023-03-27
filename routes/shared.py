import calendar
from collections import OrderedDict
import datetime
from api.user import *
def processUserClockData(datas,resIn,resOut):
    if resIn is None:
        resIn = []
        resInDate = []
        resInTime = []
    else:
        resInDate = [it['clockTime'][:10] for it in resIn]
        resInTime = [it['clockTime'] for it in resIn]
    if resOut is None:
        resOut = []
        resOutDate = []
        resOutTime = []
    else:
        resOutDate = [it['clockTime'][:10] for it in resOut]
        resOutTime = [it['clockTime'] for it in resOut]  #具体时间

    def date_range(start_date, end_date):
        datelist = []
        for n in range(int((end_date - start_date).days)+1):
            datelist.append((start_date + datetime.timedelta(n)))
        return datelist
    res = {}
    # datas['month'] = int(datas['month'])
    datetmp = datetime.date.today()
    datetmp = datetmp.strftime("%Y-%m-%d").split('-')
    
    dateend = calendar.monthrange(datas['year'], int(datas['month']))[1]  
    if int(datas['month']) == int(datetmp[1]):
        dateend = int(datetmp[-1])
    # print(datetmp[1],dateend)
    start_date = datetime.datetime(datas['year'], int(datas['month']), 1)  # 开始日期
    end_date = datetime.datetime(datas['year'], int(datas['month']), dateend) #结束时间
    
    depart_data = user_QueryDepartment(datas['uid']) #查询公司打卡时间设置
    print("datas['uid']",datas['uid'])
    ttt = depart_data[0]['endTime'].split(':')
    print("ttt",ttt)
    wages = float(ttt[0]) + (0.5 if ttt[1] == '30' else 0.0) 
    print("wage",wages)
    ttt = depart_data[0]['startTime'].split(':')
    wages -= float(ttt[0]) + (0.5 if ttt[1] == '30' else 0.0) 
    print("wage",wages)
    wages *= float(depart_data[0]['hourPay'])
    print("wage",wages)
    makeUp,workOver = User_queryOtherDatasLog(datas)
    if makeUp is None:
        makeUp = []
    if workOver is None:
        workOver = []    
    dateIn = depart_data[0]['startTime']
    dateOut = depart_data[0]['endTime']
    print("dateIn,dateOut",dateIn,dateOut)

    allin,allout,late,advance= 0,0,0,0  #统计未打卡
    clockinlist = OrderedDict()
    clockoutlist = OrderedDict()
    for it in (date_range(start_date,end_date)):
        if it.strftime("%Y-%m-%d") not in (resInDate):
            allout += 1
            clockinlist[it.strftime("%Y-%m-%d")] = None
        if it.strftime("%Y-%m-%d") not in (resOutDate):
            allout += 1
            clockoutlist[it.strftime("%Y-%m-%d")] = None

    resInDate ,resOutDate= [],[]
    for it in resIn:
        if it['clockTime'][11:] < dateIn:
            resInDate.append(it['clockTime'][:10])
    for it in resOut:
        if it['clockTime'][11:] > dateOut:
            resOutDate.append(it['clockTime'][:10]) #统计正常打卡
    print("resIn ,resOut",resIn ,resOut)
    print("resInDate ,resOutDate",resInDate ,resOutDate)
    # print(date_range(start_date,end_date))
    for it in (date_range(start_date,end_date)):
        if it.strftime("%Y-%m-%d") in (resInDate): 
            allin += 1
        if it.strftime("%Y-%m-%d") in (resOutDate):
            allin += 1

    for it in resInTime:
        if it[11:] > dateIn:
            late += 1
    for it in resOutTime:
        if it[11:] < dateOut: 
            advance += 1
    
    clockTimeLine = {}
    tmp = {}
    for it in resIn:
        clockinlist[it['clockTime'][:10]] = it['clockTime'][11:]
    # sorted(clockinlist)
    clockinlist = dict(sorted(clockinlist.items(), key=lambda x: x[0]))
    clockTimeLine['clockin'] = []
    clockTimeLine['clockin'].append([it.split('-')[-1] for it in list(clockinlist.keys())])
    clockTimeLine['clockin'].append(list(clockinlist.values()))
    print(clockTimeLine)
    tmp = {}
    for it in resOut:
        clockoutlist[it['clockTime'][:10]] = it['clockTime'][11:]
    # clockTimeLine['clockout'] = clockoutlist
    clockoutlist = dict(sorted(clockoutlist.items(), key=lambda x: x[0]))
    clockTimeLine['clockout'] = []
    clockTimeLine['clockout'].append([it.split('-')[-1] for it in list(clockoutlist.keys())])
    clockTimeLine['clockout'].append(list(clockoutlist.values()))
    clockTimeLine['front'] = dateIn
    clockTimeLine['end'] = dateOut
    res['zhexiantu'] = clockTimeLine
    tmp = {}
    tmp["daka"] = allin
    tmp["weidaka"] = allout
    tmp["chidao"] = late
    tmp["zaotui"] = advance
    tmp['xinzi'] = wages
    tmp['jiaban'] = len(makeUp)
    tmp['qingjia'] = len(workOver)
    res['bing'] = tmp


    return res