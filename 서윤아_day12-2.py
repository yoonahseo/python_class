import pandas as pd
# df = pd.read_csv("data.csv")
# print(df)
# print(df.describe())#데이트 요약 분석
# import matplotlib.pyplot as plt
# import numpy as np
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
#
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

#0으로 채운 다차원 배열
#zeros = np.zeros((3,4))
#print(zeros)

#특정한 값으로 채운 다차원 배열
# filled =np. full((3,4),5)
# print(filled)

#연속된  값으로 채운 일차원 배열
#arr = np.arange(1,10,2)
#print(arr)

# random_arr = np.random.randint(1,100,(3,4))
# print(random_arr)

# arr1 = np.array([1,3,5])
# arr2 = np.array([2,5,8])

# print(arr1 + arr2 )
# print(arr1 - arr2 )
# print(arr1 * arr2 )
# print(arr1 / arr2 )

import seaborn as sns
from matplotlib import pyplot as plt

from 서윤아_미니프로젝트2 import choice

df = pd.read_csv("tips.csv")
plt.figure(figsize=(8,5))
sns.scatterplot(x="total_bill",y="tip",hue="sex",data=df,palette="Set2")
plt.xlabel("total Bill ($)")
plt.xlabel("tip($)")
plt.show()




