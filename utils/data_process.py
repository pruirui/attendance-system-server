
# 数据模型类===》普通字典
#    user/[user,user,user]    属性清单,

#                  数据源     数据模型类属性    0 obj / 1
import datetime
from db_config import db_init as db
def query2dict(model_list):
    
    if isinstance(model_list,list):  #如果传入的参数是一个list类型的，说明是使用的all()的方式查询的

        if(len(model_list) == 0):
            return None

        if isinstance(model_list[0],db.Model):   # 这种方式是获得的整个对象  相当于 select * from table
            lst = []
            for model in model_list:
                dic = {}
                for col in model.__table__.columns:
                    dic[col.name] = getattr(model,col.name)
                lst.append(dic)
            return lst
        else:                           #这种方式获得了数据库中的个别字段  相当于select id,name from table
            lst = []
            for result in model_list:   #当以这种方式返回的时候，result中会有一个keys()的属性
                # print(type(result))
                print(type(result))
                lst.append([dict(zip(result.keys(), r)) for r in result])
            return lst
    else:                   #不是list,说明是用的get() 或者 first()查询的，得到的结果是一个对象
        if isinstance(model_list,db.Model):   # 这种方式是获得的整个对象  相当于 select * from table limit=1
            dic = {}
            for col in model_list.__table__.columns:
                dic[col.name] = getattr(model_list,col.name)
            return dic
        else:    #这种方式获得了数据库中的个别字段  相当于select id,name from table limit = 1
            return dict(zip(model_list.keys(),model_list))
        

def Class_To_Data(data_list,fields,type=0):
    if not type:  #[obj,obj]
        user_list = []  
        for u in data_list:
            temp = {}
            for f in fields:
                if f in ['create_time','login_time']:
                    temp[f] = datetime.datetime.strftime(getattr(u,f), "%Y-%m-%d %H:%M:%S ")
                else:
                    temp[f] = getattr(u,f)
            user_list.append(temp)


            
    else:#   obj
        user_list = {}
        for f in fields:
            if f in ['create_time', 'login_time']:
                d = getattr(data_list, f)
                if d:
                    user_list[f] = datetime.datetime.strftime(d, "%Y-%m-%d %H:%M:%S ")
            else:
                user_list[f] = getattr(data_list, f)

    return user_list