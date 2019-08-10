#数据预处理：
#①处理缺失值
#②将非数值型特征转化为数值型特征
#③特征归一化，连续特征离散化
import pandas as pd
import  numpy as np
from datetime import  date
#禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)


offlinedata = pd.read_csv("..\\Data\\sourceData\\ccf_offline_stage1_train.csv")

#①处理优惠券的Discount_rate
def calc_discount_rate(s):
    s =str(s)
    s =s.split(":")
    if(len(s) == 1):
        return s[0]
    else:
        return 1-float(s[1])/float(s[0])
def get_discount_price(s):
    s =str(s)
    s =s.split(":")
    if(len(s) == 1):
        return
    else:
        return int(s[0])
def get_discount_dicount(s):
    s = str(s)
    s = s.split(":")
    if (len(s) == 1):
        return
    else:
        return int(s[1])
def is_ManJian(s):
    s =str(s)
    s =s.split(":")
    if(len(s) == 1):
        return 0
    else:
        return 1

offlinedata['discount_price'] = offlinedata.Discount_rate.astype('str').apply(get_discount_price)
offlinedata['discount_discount'] = offlinedata.Discount_rate.astype('str').apply(get_discount_dicount)
offlinedata['is_man_jian'] = offlinedata.Discount_rate.astype('str').apply(is_ManJian)
offlinedata['discount_rate'] = offlinedata.Discount_rate.astype('str').apply(calc_discount_rate)
print(offlinedata.head(10))

#②处理用户相关特征

#a.使用户使用优惠券日趋与领取优惠券日期的间隔天数
def get_user_date_datereceived_gap(s):
    s =s.split(":")
    return (date(s[0][0:4],s[0][4:6],s[0][6:8])-date(s[1][0:4],s[1][4:6],s[1][6:8]))
#b.统计用户消费的商户数量(t1)
user = offlinedata['User_id']
user.drop_duplicates(inplace=True)
t1 = offlinedata[offlinedata['Date'].notnull()][['User_id','Merchant_id']]
t1.drop_duplicates(inplace=True)
t1['Merchant_id'] = 1
t1 = t1.groupby('User_id').agg('sum').reset_index()
t1.rename(columns = {'Merchant_id':'count_merchant'},inplace=True)
print(t1.head(5))



