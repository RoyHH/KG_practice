# Knowledge-Graph-Movie
该资源为学习网易云张老师的总结，希望对您有所帮助，再次强烈推荐大家阅读张宏伦老师的网易云课程及Github源码，受益匪浅。 <br />
[https://github.com/Honlan/starwar-visualization/tree/master/star_war](https://github.com/Honlan/starwar-visualization/tree/master/star_war) <br />
[https://study.163.com/course/courseLearn.htm?courseId=1003528010](https://study.163.com/course/courseLearn.htm?courseId=1003528010) <br />
***
## Key Features
- [x] python 3.6 or 3.7
- [x] urllib + json
- [x] HTML + CSS + D3

## To-do List
- [x] 知识获取
- [x] 知识抽取
- [ ] 知识融合
- [x] 知识关联
- [ ] 知识挖掘
    - [ ] 特征工程
    - [ ] 先验知识
- [ ] 知识存储
- [x] 知识计算
    - [x] 知识搜索
    - [ ] 知识推理
- [ ] 知识应用
***
## 1. 知识获取
- 爬虫 :sunny:
```
# 生成films.csv文件存入csv文件夹
python get_films.py
```
## 2. 知识抽取
#### 2.1 抓取实体 ==> 生成一系列csv文件
- [x] 生成film_characters.csv存入csv文件夹
- [x] 生成film_planet.csv存入csv文件夹
- [x] 生成film_species.csv存入csv文件夹
- [x] 生成film_starships.csv存入csv文件夹
- [x] 生成film_vehicles.csv存入csv文件夹
```
python get_details.py
```
#### 2.2 这部分实体可以可视化，更加直观一些（选做）
- （选做）调用seaborn做可视化
```
# 生成stat_basic.csv文件
python get_jsonfilms.py

# 柱状图展示
python show_hist.py

# 生成stat_character.csv文件
python get_jsondetails.py

# 散点图、回归图、六角图、KDE图展示
python show_height_mass1.py
python show_height_mass2.py
```
- （选做）调用matplotlib做可视化
```
# 散点图展示
python show_scatter.py
```
## 3. 知识关联
#### 3.1 获取节点、边，建立关联 
```
# 生成starwar_alldata.json文件
python get_alldata.py
```
#### 3.2 HTML网页设计
- 为了展示全部信息
```
# 生成all_data.json文件
python get_json_info.py
```
- 为了展示全部信息的时间轴
```
# 生成all_timeline.json文件
python json_timeline.py
```
- 网页设计
```
main.html
```
***
建议读者结合博客进行实践，对应文章（感谢Eastmount博主）： <br />
[[知识图谱实战篇] 一.数据抓取之Python3抓取JSON格式的电影实体](https://blog.csdn.net/eastmount/article/details/86714051) <br />
[[知识图谱实战篇] 二.Json+Seaborn可视化展示电影实体](https://blog.csdn.net/Eastmount/article/details/86739154) <br />
[[知识图谱实战篇] 三.Python提取JSON数据、HTML+D3构建基本可视化布局](https://blog.csdn.net/Eastmount/article/details/86755610) <br />
[[知识图谱实战篇] 四.HTML+D3+CSS绘制关系图谱](https://blog.csdn.net/Eastmount/article/details/87090486) <br />
[[知识图谱实战篇] 五.HTML+D3添加鼠标响应事件显示相关节点及边](https://blog.csdn.net/Eastmount/article/details/87116136) <br />
[[知识图谱实战篇] 六.HTML+D3实现点击节点显示相关属性及属性值](https://blog.csdn.net/Eastmount/article/details/87193405) <br />
[[知识图谱实战篇] 七.HTML+D3实现关系图谱搜索功能](https://blog.csdn.net/Eastmount/article/details/87270150) <br />
[[知识图谱实战篇] 八.HTML+D3绘制时间轴线及显示实体](https://blog.csdn.net/Eastmount/article/details/87371200) <br />

 
 
