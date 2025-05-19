# 4. 三目运算
# 基本格式：为真结果 if 判断条件 else 为假结果
# a = 10
# b = 5
# if a <= b:
#     print("a小于等于b") #为真结果
# else:
#     print("a大于b") #为假结果
# print("a小于等于b") if a <= b else  print("a大于b") #第二种写法

# 6. if elif 结构
# if else 二选一 if elif 多选一
# if 条件：
#     满足条件1要做的事情
# elif 条件2：
#     满足条件2要做的事情
# elif 条件3：
#     满足条件3要做的事情
# score = 35
# if 80<=score<=100:
#     print("优秀")
# elif 60<=score<80:
#     print("及格")
# elif 0<=score<60:
#     print("不及格")
# else: # else 可以表示所以条件不符合这样一种情况
#     print("成绩无效")
"""
a = input("请输入一个数字a：")
b = input("请输入另一个数字b：")
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
elif a == b:
    print("a = b")  #自写 if elif 多选一判断
"""

"""                 多看
# if嵌套
ticket = False   # true 代表有车票 False代表没有车票
temp =39 # 定义一个浮点型变量保存温度
if ticket == True:
    print("可以回家了-->", end="")
    if 36.3 <= temp <= 37.2:
        print("体温正常 顺利上车" )
    else:
        print("体温异常被隔离")
else:
    print("没有票了-->", end="")
if 36.3 <= temp <= 37.2:
    print("体温正常可以侯票")
else:
    print("还被隔离了")
"""