# import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import random

with open('data.csv',  newline='') as csvfile:
    rows = csv.reader(csvfile)
    listData = list(rows)

with open('result.csv',  newline='') as csvfile:
    rows = csv.reader(csvfile)
    listResult = list(rows)

#設定加工時間
costTime = {
    'OP110':22,
    'OP120':36,
    'OP130':6,
    'OP140':27,
    'OP150':57,
    'OP160':30,
}

#設定不同工作的顏色
jobColor = {}
keys = []
values = []
num = 0
#設定seed，固定隨機數值
random.seed(10)
#設定 key 和 value，並製作成dictionary
for i in range(len(listData)):
    keys.append(listData[i][0] + str(num))
    num+=1
    values.append("#"+''.join(random.choice('0123456789ABCDEF')for j in range(6)))
for key, value in zip(keys, values):
    jobColor[key] = value

print(jobColor)

#subplots(顯示位置, 圖片大小比例)
fix, ax = plt.subplots(1, figsize = (16,6))

#繪製甘特圖，barch(標籤名稱, 長度, 開始位置, 顏色)
for i in range(2,22):
    n = len(listResult[i])
    for j in range(1,n-1):
        ax.barh(listResult[i][0], costTime[listResult[i][j][10:15]], left = int(listResult[i][j][-3:]),color=jobColor[listResult[i][j][4:6]])

#讀取字典的 key 和 value
patchesColor = [i for i in jobColor.values()]
patchesName = [i for i in jobColor.keys()]

#設定圖例，mpatches.Patch(顏色, 名稱)
patches = [mpatches.Patch(color=patchesColor[i], label="{:s}".format(patchesName[i]))for i in range(len(jobColor.keys()))]

#添加圖例
plt.legend(handles = patches, loc=4)

#設定XY軸標籤
plt.xlabel("Processing Time/Hr", fontsize=15)
plt.ylabel("Processing Machine", fontsize=15)

# plt.savefig("result.jpg")
plt.show()