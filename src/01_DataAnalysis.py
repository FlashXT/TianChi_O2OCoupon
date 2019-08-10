# @Author:FlashXT;
# @Date:2019/6/8 11:25;
# @Version 1.0
# CopyRight © 2018-2020,FlashXT & turboMan . All Right Reserved.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb
#禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)
#对数据进行统计分析，了解数据的正负样本分布，缺失值情况，以及初步特征构建
######################################################################
#数据文件说明：
# ccf_offline_stage1_train.csv              用户线下消费和优惠券领取行为
# ccf_online_stage1_train.csv               用户线上点击/消费和优惠券领取行为
# ccf_offline_stage1_test_revised.csv       用户O2O线下优惠券使用预测样本
#######################################################################
#正负样本定义：
#正样本：如果Date!=null & Coupon_id != null，则表示用优惠券消费，即正样本；
#负样本：如果Date=null & Coupon_id != null，该记录表示领取优惠券但没有使用，即负样本；
#中间样本：如果Date!=null & Coupon_id = null，则表示普通消费；
def DataAnalysis():

    # 1.ccf_offline_stage1_train.csv  用户线下消费和优惠券领取行为统计
    ccfoffline = pd.read_csv('..\\Data\\sourceData\\ccf_offline_stage1_train.csv')

    #①用户线下消费和优惠券领取行为统计
    print("用户线下消费和优惠券领取行为统计:\t")

    print("①抽样查看数据的特征以及数据规模：")
    print("a.数据的前10行：")
    print(ccfoffline.head(10))
    print("-" * 100)
    print("b.数据集特征：")
    print(ccfoffline.info())
    print("-"*100)

    # ②正负样本数量统计
    print("②正负样本数量统计：")
    # 负样本：
    offnegsample =ccfoffline[ccfoffline["Coupon_id"].notnull() & ccfoffline["Date"].isnull()]
    print("负样本数量：",offnegsample.shape[0])
    # 正样本：
    offpossample = ccfoffline[ccfoffline["Coupon_id"].notnull() & ccfoffline["Date"].notnull()]
    print("正样本数量：",offpossample.shape[0])
    # 中间样本：
    offmidsample = ccfoffline[ccfoffline["Coupon_id"].isnull() & ccfoffline["Date"].notnull()]
    print("中间样本数量:", offmidsample.shape[0])

    #seaborn绘制统计图
    # x = ["pos",'mid','neg']
    # y = [offpossample.shape[0],offmidsample.shape[0],offnegsample.shape[0]]
    # #条形统计图
    # g= snb.barplot(x,y)
    # for i in range(0,len(y)):
    #     g.text(i,y[i],y[i],color="black",ha="center")
    #
    # plt.xlabel("offline sample class")
    # plt.ylabel("offline sample num")
    # plt.title("Offline Sample Count")
    # plt.savefig("..\\Data\\StatisticalChart\\Offline_Sample_Count.jpg")
    # plt.show()
    print("结论：正负样本不均衡")
    print("-"*100)

    #③用户数量和商户数量统计
    print("③用户和商户数量统计：")
    offusers = set(ccfoffline['User_id'].values.tolist())
    offmerchants = set(ccfoffline['Merchant_id'].values.tolist())

    offpusers = set(offpossample['User_id'].values.tolist())
    offpmerchants = set(offpossample['Merchant_id'].values.tolist())

    offnusers = set(offnegsample['User_id'].values.tolist())
    offnmerchants = set(offnegsample['Merchant_id'].values.tolist())

    print("\t\t","用户数量","\t商户数量")
    print("Pos\t\t",len(offpusers), "\t\t",len(offpmerchants))
    print("Neg\t\t",len(offnusers), "\t",len(offnmerchants))
    print("P&N\t\t",len(offpusers & offnusers),"\t\t",len(offpmerchants & offnmerchants))
    print("Summary\t", len(offusers), "\t", len(offmerchants))
    print("结论：共有539438个用户，8415个商户，其中正样本中有46395个用户，4076个商家，"
          "有33517个用户和3959个商家，在正样本和负样本中均出现")
    print('-' * 100)

    # 2.ccf_online_stage1_train.csv  用户线下上消费和优惠券领取行为统计

    # ① 用户线上消费和优惠券领取行为统计
    print("用户线上消费和优惠券领取行为统计:\t")
    print("①抽样查看数据的特征以及数据规模：")

    ccfonline = pd.read_csv('..\\Data\\sourceData\\ccf_online_stage1_train.csv')

    print("a.线上数据示例：")
    print(ccfonline.head(5))
    print("b.线上数据统计信息：")
    print(ccfonline.info())


    #②正负样本数量统计
    print("正负样本数量统计：")
    # 负样本：
    onnegsample =ccfonline[ccfonline["Coupon_id"].notnull() & ccfonline["Date"].isnull()]
    print("正样本数量：",onnegsample.shape[0])
    #正样本：
    onpossample = ccfonline[ccfonline["Coupon_id"].notnull() & ccfonline["Date"].notnull()]
    print("负样本数量：",onpossample.shape[0])
    # 中间样本：
    onmidsample = ccfonline[ccfonline["Coupon_id"].isnull() & ccfonline["Date"].notnull()]
    print("中间样本数量:",onmidsample.shape[0])

    # seaborn绘制统计图
    # x = ["pos", 'mid', 'neg']
    #     # y = [onpossample.shape[0], onmidsample.shape[0], onnegsample.shape[0]]
    #     # # 条形统计图
    #     # g = snb.barplot(x, y)
    #     # for i in range(0, len(y)):
    #     #     g.text(i, y[i], y[i], color="black", ha="center")
    #     #
    #     # plt.xlabel("online sample class")
    #     # plt.ylabel("online sample num")
    #     # plt.title("Online Sample Count")
    #     # plt.savefig("..\\Data\\StatisticalChart\\Online_Sample_Count.jpg")
    #     # plt.show()
    print("线上数据的正负样本数量都很少，几乎全部是中间样本")

    #③线上用户数量和商户数量统计
    print("用户和商户数量统计:")
    onusers = set(ccfonline['User_id'].values.tolist())
    onmerchants = set(ccfonline['Merchant_id'].values.tolist())

    onpusers = set(onpossample['User_id'].values.tolist())
    onpmerchants = set(onpossample['Merchant_id'].values.tolist())

    onnusers = set(onnegsample['User_id'].values.tolist())
    onnmerchants = set(onnegsample['Merchant_id'].values.tolist())

    print("\t\t","用户数量","\t商户数量")
    print("Pos\t\t",len(onpusers), "\t\t",len(onpmerchants))
    print("Neg\t\t",len(onnusers), "\t",len(onnmerchants))
    print("P&N\t\t",len(onpusers & onnusers),"\t\t",len(onpmerchants & onnmerchants))
    print("Summary\t", len(onusers), "\t", len(onmerchants))

    print("结论：共有762858个用户，7999个商户，其中正样本中有95655个用户，2841个商家，"
          "有59472个用户和2526个商家，在正样本和负样本中均出现")
    print('-'*100)

    # 3.线上数据和线下数据的综合分析
    print("线上和线下用户和商户的重合数量：")
    print("\t\t\t","用户数量","商户数量")
    print("总数量：\t\t",len(offusers&onusers),"\t",len(offmerchants&onmerchants))
    print("正样本数量:\t", len(offpusers & onpusers),"\t\t",len(offpmerchants&onpmerchants))
    print("负样本数量：\t", len(offnusers & onnusers),"\t\t",len(offnmerchants&onnmerchants))
    print('-'*100)

if __name__ == "__main__":
    DataAnalysis()