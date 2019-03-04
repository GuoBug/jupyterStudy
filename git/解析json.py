#encoding=utf-8

#从指定的文件中取出json内容，并重组出有用信息
import json
import pandas as pd

#建立字典,并按照字典建立Dataframe
cols = ['name','org','empno','post','phone']
df0 = pd.DataFrame(columns=cols)
#print(df0)

#取内容
for line in open("info.txt"):
  json0 = json.loads(line)
  
  for meneber in json0["rows"]:
    df0 = df0.append({'name':meneber['TITLE'],'org':meneber['ORGID'],'empno':meneber['EMPNO'],'post':meneber['POSTID'],'phone':meneber['MOBILENO']},ignore_index=True)
  
#End
#print(df0)
#输出文件
df0.to_csv('./output.csv',index=False,encoding='utf_8_sig')
