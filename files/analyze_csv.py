import csv
from matplotlib import figure
from matplotlib.ticker import PercentFormatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读csv文件，存入pd.dataframe
filename='result.csv'
data=pd.read_csv(filename)
count=len(data.index)
print("count:",count)
# =====统计不同音乐水平=====
count_amateur=(data["musiclevel"]=="amateur").sum()
count_profession=(data["musiclevel"]=="profession").sum()
count_newhand=(data["musiclevel"]=="newhand").sum()
print("count_profession:",count_profession,
      ",count_amateur:",count_amateur,
      ",count_newhand:",count_newhand)
# =====图灵测试=====
count_human=(data["q2"]=="human").sum()+(data["q4"]=="human").sum() # AI生成,被认为是human创作的
count_ai=(data["q1"]=="ai").sum()+(data["q3"]=="ai").sum() # human创作,被认为是AI生成的
print("count_human_but_ai:",count_human,",count_ai_but_human:",count_ai)


# =====对比生成的和训练样本=====
count_real_better=(data["q9"]=="first").sum()
count_fake_better=(data["q9"]=="second").sum()
print("count_real_better:",count_real_better,",count_fake_better:",count_fake_better)
# =====对比不同配器=====
count_instA_better=(data["q10"]=="first").sum()
count_instB_better=(data["q10"]=="second").sum()
print("count_instA_better:",count_instA_better,",count_instB_better:",count_instB_better)
# =====对比不同轨道数量=====
count_original_tracks=(data["q11"]=="first").sum()
count_less_tracks=(data["q11"]=="second").sum()
print("count_original_tracks:",count_original_tracks,",count_less_tracks:",count_less_tracks)


# =====旋律、节奏、和声、创新平均分=====
q5_scores=data.iloc[:,8].values   # 返回该列数值的list
num=len(q5_scores)
mean_m=0
mean_r=0
mean_c=0
mean_i=0
total=0
for score in q5_scores:
    digits = [int(d) for d in str(score)]
    mean_m+=digits[0]
    mean_r+=digits[1]
    mean_c+=digits[2]
    mean_i+=digits[3]
    total=mean_m+mean_r+mean_c+mean_i
print("【q5】mean_m:",mean_m/num,",mean_r:",mean_r/num,
      ",mean_c:",mean_c/num,",mean_i:",mean_i/num,",mean_total:",total/num)

q6_scores=data.iloc[:,9].values
mean_m=0
mean_r=0
mean_c=0
mean_i=0
total=0
for score in q6_scores:
    digits = [int(d) for d in str(score)]
    mean_m+=digits[0]
    mean_r+=digits[1]
    mean_c+=digits[2]
    mean_i+=digits[3]
    total=mean_m+mean_r+mean_c+mean_i
print("【q6】mean_m:",mean_m/num,",mean_r:",mean_r/num,
      ",mean_c:",mean_c/num,",mean_i:",mean_i/num,",mean_total:",total/num)

q7_scores=data.iloc[:,10].values
mean_m=0
mean_r=0
mean_c=0
mean_i=0
total=0
for score in q7_scores:
    digits = [int(d) for d in str(score)]
    mean_m+=digits[0]
    mean_r+=digits[1]
    mean_c+=digits[2]
    mean_i+=digits[3]
    total=mean_m+mean_r+mean_c+mean_i
print("【q7】mean_m:",mean_m/num,",mean_r:",mean_r/num,
      ",mean_c:",mean_c/num,",mean_i:",mean_i/num,",mean_total:",total/num)

q8_scores=data.iloc[:,11].values
mean_m=0
mean_r=0
mean_c=0
mean_i=0
total=0
for score in q8_scores:
    digits = [int(d) for d in str(score)]
    mean_m+=digits[0]
    mean_r+=digits[1]
    mean_c+=digits[2]
    mean_i+=digits[3]
    total=mean_m+mean_r+mean_c+mean_i
print("【q8】mean_m:",mean_m/num,",mean_r:",mean_r/num,
      ",mean_c:",mean_c/num,",mean_i:",mean_i/num,",mean_total:",total/num)

# 平均分：不同step数的4个维度的小提琴图
# 横：四个维度，纵：分数，左右区分:音乐水平
# sns.violinplot(x=["m","r","c","i"],y=q8_scores,data=data,hue="musiclevel",palette="set2",split=True)
               


# 人群分布
plt.pie([count_profession,count_amateur,count_newhand],
        labels=['profession','amateur','newhand'],
        colors=['#3682be','#5b9bd5','#ed7d31'],
        autopct='%.1f%%')
plt.title("Music Level")
plt.show()
plt.close()

# 图灵测试
y1 = count_human/(count*2.0)
y2 = 1-count_human/(count*2.0)
plt.bar(0,y1,width=0.2,label='human',color='#f59311',edgecolor='grey',zorder=1)
plt.bar(0,y2,width=0.2,bottom=y1,label='AI',color='#16afcc',edgecolor='grey',zorder=1)

plt.axes().get_xaxis().set_visible(False) 
plt.xlabel('question',fontsize=12)
plt.ylabel('result',fontsize=12)
plt.ylim(0,1.01)
plt.yticks(np.arange(0,1.2,0.2),[f'{i}%' for i in range(0,120,20)])
for i in range(10):
    plt.axhline(y=i/10,color='grey',ls='--', linewidth=0.5)
# 添加图例，将图例移至图外
plt.legend(frameon=False,bbox_to_anchor=(1.01,1))
plt.tight_layout()
plt.subplots_adjust(left=0.4,right=0.5,top=0.9)
plt.title("Human or AI?")
plt.show()
plt.close()


# 对比：百分比堆积柱状图,q9
y1 = count_real_better/count
y2 = count_fake_better/count
plt.bar(0,y1,width=0.2,label='real',color='#ed7d31',edgecolor='grey',zorder=1)
plt.bar(0,y2,width=0.2,bottom=y1,label='fake',color='#5b9bd5',edgecolor='grey',zorder=1)
plt.axes().get_xaxis().set_visible(False) 
plt.xlabel('question 9',fontsize=12)
plt.ylabel('result',fontsize=12)
plt.ylim(0,1.01)
plt.yticks(np.arange(0,1.2,0.2),[f'{i}%' for i in range(0,120,20)])
for i in range(10):
    plt.axhline(y=i/10,color='grey',ls='--', linewidth=0.5)
plt.legend(frameon=False,bbox_to_anchor=(1.01,1))# 添加图例，将图例移至图外
plt.tight_layout()
plt.subplots_adjust(left=0.4,right=0.5,top=0.9)
plt.title("Q9:Real or Fake?")
plt.show()
plt.close()
# q10
y1 = count_instA_better/count
y2 = count_instB_better/count
plt.bar(0,y1,width=0.2,label='instA',color='#ed7d31',edgecolor='grey',zorder=1)
plt.bar(0,y2,width=0.2,bottom=y1,label='instB',color='#5b9bd5',edgecolor='grey',zorder=1)
plt.axes().get_xaxis().set_visible(False) 
plt.xlabel('question 10',fontsize=12)
plt.ylabel('result',fontsize=12)
plt.ylim(0,1.01)
plt.yticks(np.arange(0,1.2,0.2),[f'{i}%' for i in range(0,120,20)])
for i in range(10):
    plt.axhline(y=i/10,color='grey',ls='--', linewidth=0.5)
plt.legend(frameon=False,bbox_to_anchor=(1.01,1))# 添加图例，将图例移至图外
plt.tight_layout()
plt.subplots_adjust(left=0.4,right=0.5,top=0.9)
plt.title("Q10:InstA or InstB?")
plt.show()
plt.close()

# q11
y1 = count_original_tracks/count
y2 = count_less_tracks/count
plt.bar(0,y1,width=0.2,label='more',color='#ed7d31',edgecolor='grey',zorder=1)
plt.bar(0,y2,width=0.2,bottom=y1,label='less',color='#5b9bd5',edgecolor='grey',zorder=1)
plt.axes().get_xaxis().set_visible(False) 
plt.xlabel('question 11',fontsize=12)
plt.ylabel('result',fontsize=12)
plt.ylim(0,1.01)
plt.yticks(np.arange(0,1.2,0.2),[f'{i}%' for i in range(0,120,20)])
for i in range(10):
    plt.axhline(y=i/10,color='grey',ls='--', linewidth=0.5)
plt.legend(frameon=False,bbox_to_anchor=(1.01,1))# 添加图例，将图例移至图外
plt.tight_layout()
plt.subplots_adjust(left=0.4,right=0.5,top=0.9)
plt.title("Q11:More tracks or Less?")
plt.show()
plt.close()

