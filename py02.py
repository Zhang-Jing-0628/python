# 1.算数运算符
# 加减乘除
# print(1+1)
# print(1-1)
# print(1*2)
# print(6/3)
# a=1/1
# print(type(a))

#//取整除 取商的整数部分 向下取整
# 向下取整：不管四舍五入的规则，只要后面有小数就忽略小数
# a=5
# b=2
# print(a//b)

# %取余数 只取余数部分
# print(a%b)

# ** 幂  a**b,a的b次方。
# print(a**b)
# print(7.0//2)

# 赋值运算符  给变量赋值
# num1=5
# num2=10
# num3=num2
# print(num3)
# num4=num1
# print(num3+num4)

# n1 = 152 #成本价
# n2 = 200 #利润
# n3 = n1 + n2 #第一种
# print(n3)
# n1 +=n2 #第二种
# print(n1)

# n = 1
# n = n-1 #第一种
# n -= 1 #第二种
# print(n)
# 赋值运算符必须连着写，中间不能有空格，否则会报错

# n=2
# n *= 2
# n /= 2
# print( n )


# 3. input()输入函数
# name = input("请输入你的名字：")
# print(name)
# pwd = input("请输入你的密码：")
# print(pwd)

# 4.转义字符
# 4.1 \t 制表符 通常表示空四个字符，也称缩进符
# print("sixs\tar")
# print("姓名\t年龄\t性别\t")
# 4.2 \n 换行符 表示将当前位置移动到下一行开头
# print("hh\nxx\nheihei")
# 4.3 \r 回车 将当前位置移动到本行开头
# print("jingjing\rdingding")
# 4.4 \\ 放斜杠符
# print("sixs\\ar")

# if判断 运算符 if-else if嵌套
# 1. if判断
# if
# 满足条件做的事前
# age=17
# if age<18:
#     print("未成年禁止上网")
# score = input("请输入您的成绩:")
# if score=='100':
#     print("优秀")
# if score=='80':
#     print("良好")
# if score=='60':
#     print("继续努力")

# 2.比较运算符
# == 比较的是两个变量的值是否相等，相等的话就返回为True(真)，相等返回为False(假)
# != 比较的是两个变量的值是否相等，不相等的话就返回为True(真)，相等返回为False(假)
# a = 9
# b = 1
# # print(a <= b)
# if a < b:
#     print("a小于b")
# if a > b:
#     print("a大于b")

# a=10
# b=10
# if a!=b:
#     print("a不等于b")
# if a==b:
#     print("a等于b")

# 3.逻辑运算符
# and 左右俩边都符合才为真
# a = "哈"
# b = "嘿"
# if a =="哈" and b=="嘿":
#     print("a和b都在笑")

# or 左右俩边只要有一边符合就为真
# a="哈哈哈"
# if a == "哈哈哈" or b == "嘿嘿嘿":
#     print("他在哈哈大笑")

# fruit = "苹果"
# if fruit == "苹果" or fruit == "水蜜桃":
#     print("带回来了苹果")

# 4. not 表示相反的结果
# print( not 3>9)

# if else
# 基本格式:
# if 条件:
#     满足条件时要做的事
# else:
#     不满足条件是改做的事情

# a=666
# if a == 666:
#     print("你真棒")
# else:
#     print("继续努力")

