# 字符串常见操作
#3.1查找
# find检测某个子字符串是否包含在字符串中，如果在就返回到这个子字符串开始位置的下标，否则就返回负一。
# find(子字符串，开始位置下标，结束位置下标。)
# 开始位置下标和结束位置下标可以省略表示在整个字符串中查找
# from curses.ascii import isupper
# from itertools import count
# from operator import index
from dataclasses import replace
from os.path import split

# neam = "bingbing"
# print(neam.find("i"))   #第一个i的下标为1
# print(neam.find("bing"))
# print(neam.find("b",2))   #超出范围，不包含返回-1
# print(neam.find("b",5))
# print(neam.find("b",2,5))
# print(neam.find("b",3,4))    # -1 包前不包后

# 2. index()检测某个子字符串是否包含在字符串中，如果在就返回到这个子字符串的下标，否则就会报错。
# index(子字符串，开始位置下标，结束位置下标。)
# 开始位置下标和结束位置下标可以省略表示在整个字符串中查找

# neam = "红黄蓝绿青橙紫"
# print(neam.index("黄"))
# # print(neam.index("黄",2))   #报错 从下标2开始找，没有找到
# print(neam.index("黄",1,3))   # 1 包前不包后
# #同样遵循包前不包后 和 find 的区别 find 没找到输出 -1，index 没找的 会报错。

# 3. count(): 返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标。)
# 开始位置下标和结束位置下标可以省略表示在整个字符串中查找

# neam = "bingbing"
# print(neam.count("b"))  # 2
# print(neam.count("a"))  # 0
# print(neam.count("b",1))
# print(neam.count("b",1,3))
# print(neam.count("b",1,4))   #同样遵循包前不包后

# 4. 判断
# startswith():是否以某个字符串开头，是的话返回True,不是的话返回False,如果设置开始和结束位置下标则在指定范围内检查
# startswith（子字符串，开始位置下标，结束位置下标）

# st = "sixstar"
# print(st.startswith("s"))
# print(st.startswith("sixs"))
# print(st.startswith("i"))
# print(st.startswith("isf"))
# print(st.startswith("s",0,1))

# 5. endswith():是否以某个字符串结尾，是的话返回True,不是的话返回False,如果设置开始和结束位置下标则在指定范围内检查
# endswith(子字符串，开始位置下标，结束位置下标)

# st = "sixstar"
# print(st.endswith("ar"))
# print(st.endswith("er"))

# 6.isupper():检测字符串中所以的字母是否都为大写，是的话返回True,不是的话返回False
# st = "sixstar"
# print(st.isupper())
# print("SIX".isupper())

# 3.1 修改元素
# 1. replace():替换
# replace(旧内容，新内容，替换次数)
# 注意替换次数可以省略，默认全部替换
# naem = "好好学习，天天向上。"
# print(naem.replace("天","时"))    #好好学习，时时向上。
# print(naem.replace("天","时",1))    #好好学习，时天向上。

# 2. split():指定分隔符来切字符串
#如果字符串中不包括分割内容，就不进行分割，会作为一个整体
# st = "hello python"
# # print(st.split(","))
# print(st.split("o",1))
# # print(st.split("l"))

# 3. capitalize 第一个大写其他都是小写
# st = "bingbing"
# print(st.capitalize())

# 4. lower():大写字母转换成小写字母
# st = "BinGbInG"
# print(st.lower())

# 5. uppre()：小写字母转换成大写字母
# st = "BinGbInG"
# print(st.upper())

# 6.列表 基本格式
# 列表名=[元素1，元素2，元素3，....]
# 注意： 所以元素反在[]里面，元素与元素之间用逗号隔开，元素之间的数据类型可以个不相等
# li = [1,2,"a",4]
# print(li,type(li))
# print(li[2])
# 列表也可以进行切片操作
# print(li[0:3])
# 列表是可迭代对象，可以for循环便利取值
# for i in li:
#     print(i)

# 6.1 列表的常见操作 添加元素
# append()  extend()  insert()
# li = ["one", "two", "three"]
# li.append("four")    #append 整体添加
# li.extend("four")    #extend 分散添加，将另外一个类型中的元素逐一添加
# li.insert(3, "four")    #在指定位置插入元素
# li.insert(0, "four")    #指定位置如果有元素，那就会原有元素就会后移
# li.insert("four")     #报错没有指定下标
# print(li)
# li = [1,2,3]
# li.append(4)
# li.extend(4)    #extend 里面一定要是可迭代对象 比如 li.extend([5,6]) 不然会报错
# print(li)

# 5.2 修改元素
# 直接通过下标进行修改
# li = [1,2,3]
# print(li[1])   #查看
# li[2]="a"   #修改
# print(li)

#5.3 查找元素
# in: 判断指定元素是否存在列表中，如果存在就返回True,不存在返回False。
# no in: 判断指定元素是否存在列表中，如果不存在就返回True,存在返回False。
# li = ["a","b","c",]
# print("e"in li)

# 用户输入昵称，昵称重复则不能使用
# 定义一个列表，保存已经存在的昵称
# name_list = ["bingbing","yaya","susu"]
# while True:
#     name = input(f"请输入昵称:")
#     if name in name_list:
#         print(f"{name}重复出现请重新输入")
#     else:
#             print(f"{name}取名成功")
#             name_list.append(name)
#             print(f"{name_list}")
#             break

#5.4 删除元素
#del
# li = [1,2,3]    #删除列表
# # del li
# del li[1]
# print(li,)

#pop:删除指定下标的数据，python3版本默认删除最后一个元素。
# li = ["a","b","c"]
# # li.pop()    #默认删除最后一个元素
# li.pop(0)   #不能指定元素删除，只能根据下标进行删除
# print(li)

#remove 根据元素的值进行删除
# li = ["a","b","c","d","b"]
# li.remove("c")
# li.remove("t")  #报错，列表中不存在这个元素
# li.remove("b")  #默认删除最开始出现的指定元素
# print(li)

# 5.5 排序
# sort: 将列表按特定顺序重新排列，默认从小到大。
# reverse: 倒序，将列表倒置过来（反过来）
# li = [1,5,4,3,2]
# li.sort()   #按照从小到大的顺利重新排列，默认从小到大
# li.reverse()
# print(li)

# 5.6 列表推导式
# 格式一：{表达式 for 变更 in 列表}
# 注意：in后面可以放列表也可以放range()、可迭代对象
# li = [1,2,3,4,5]
# [print(i) for i in li]  #前面的i是表达式

# 方法二
# li = []
# for i in range(1,6):
#     # print(i)
#     li.append(i)
# print(li)

#方法三
li = []
# [li.append(i) for i in range(1,6)]
# print(li)

# 格式二[表达式 for 变更 in 列表 if 条件]
# 把奇数放进列表里面
# li = []
# for i in range(1,10):
#     if i % 2 == 1:
#         li.append(i)
# print(li)
# [li.append(i) for i in range(10)]
# print(li)

# 5.7列表嵌套
# 含义：一个列表里面又有一个列表
# li = [1,2,3,[4,5,6]]
# print(li[3][0])