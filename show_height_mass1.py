import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 读取数据 name height mass gender homeworld
df = pd.read_csv('stat_character.csv')
fig, ax = plt.subplots(1, 1)

## 散点图
# sns.jointplot(x="height", y="mass", data=df, color="b", s=50, kind='scatter',
#              space = 0.1, size = 8, ratio = 5)

## 回归图
# sns.jointplot(x="height", y="mass", data=df, color="b", kind='reg')

## 六角形
# sns.jointplot(x="height", y="mass", data=df, color="b", kind='hex')

## KDE 图
# sns.jointplot(x="height", y="mass", data=df, kind="kde", space=0, color="#6AB27B")

## 散点图+KDE 图
# g = (sns.jointplot(x="height", y="mass", data=df, color="k")
#      .plot_joint(sns.kdeplot, zorder=0, n_levels=6))

# pairplot图
sns.pairplot(df)

plt.show()
