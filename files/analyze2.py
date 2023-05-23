import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取csv文件
df_csv = pd.read_csv('result.csv')

# 需要提取的列名
col_names = ['q5', 'q6', 'q7','q8']
# 提取需要的列并将每列拆成4个子列
aspect=['m','r','c','i']
new_cols = [f"{col}_{i}" for col in col_names for i in aspect]
df_extracted = df_csv[col_names].apply(lambda x: x.apply(lambda y: str(y)).explode()).reset_index(drop=True)
# print(df_extracted)
# 将每列再次拆分成4个子列，并重新排列结果以便放入新DataFrame中
list_of_series = []
for col in col_names:
    for i in range(4):
        list_of_series.append(df_extracted[f"{col}"].str[i])
    # print(list_of_series)
df_split = pd.concat(list_of_series, axis=1)
df_split.columns = new_cols
print(df_split)

# 宽数据转长数据，区分列来源
names = ['q5','q6','q7','q8']
# for i in range(4):# 对于4个问题
#     l=4*i+1
#     r=4*i+4
#     print("l:",l,",r:",r)
#     new_col = pd.concat([df_result.iloc[:, [4*i, 4*i+1, 4*i+2, 4*i+3] ].unstack()], ignore_index=True)
#     new_col.name=names[i]
#     df_result = pd.concat([df_result, new_col], axis=1)
df_result=pd.DataFrame()
for i in range(4):
    df_q=pd.DataFrame(df_split.iloc[:,4*i:4*i+4])
    df_q = pd.DataFrame(df_q.to_numpy().reshape(-1, 1, order='F'), columns=[names[i]])
    df_result=pd.concat( [df_result,df_q],axis=1,ignore_index=False)
# 增加维度区分、音乐水平列
df_result['aspect']=range(1,len(df_q)+1)
df_result['aspect'][0:20]='m'
df_result['aspect'][20:40]='r'
df_result['aspect'][40:60]='c'
df_result['aspect'][60:80]='i'
df_result['musiclevel']=range(1,len(df_q)+1)
for i in range(4):
    df_result['musiclevel'][20*i:20*i+10]='amateur'
    df_result['musiclevel'][20*i+10:20*(i+1)]='newhand'

# print(df_result)
# 将结果写入新的csv文件中
df_result.to_csv('new_csv_file.csv', index=False)
print("ok")
# 横：四个维度，纵：分数，左右区分:音乐水平
for n in names:
    df_result = df_result.explode(n)
    df_result[n] = df_result[n].astype('float')
    sns.violinplot(x="aspect",y=n,data=df_result,hue="musiclevel",palette="Set2",split=True)
    plt.show()
