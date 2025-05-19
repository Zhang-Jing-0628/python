# print("123")
# print("哈哈哈","嘿嘿嘿","嘻嘻嘻")
# print("哈哈哈""嘿嘿嘿""嘻嘻嘻")

# print("哈哈哈","嘿嘿嘿","嘻嘻嘻",sep=",")
# sep用来间隔多个值

# print("hello world","哈哈哈哈",end="____")
# print("pipi")
# print（字符串,end="后面拼接的值")最后输出结果:第一个print中的字符串+后面拼接的值+第二个print中的字符串

# num1=3
# num2=10
# total=num1+num2
# print(num1,end=",")
# print(num2,end=",")
# print(total)
# print(num1,num2,total)

# 标识符——————定义的变量名函数名只能由数字、字母、下划线_来组成
# 价格=3
# print(价格)

# 3.1 int整数（常用）：任意大小的整数
# num=5
# 检测数据类型的方法 type（）
# print(type(num))

# 3.2float浮点型-小数
# num=0.1
# print (type(num))

# 3.3bool布尔型 通常用于判断
# 有固定写法，一个为True（真），一个为False（假）
# 注意：True和false必须严格区分大小写
# print(type(True))
# print(type(False))
# True相当于整数1，False相当于整数0
# print(True+False)

# 3.4compile（复数类型）
# 固定写法: z = a + bj---a 是实数部分 b是虚数部分 j是虚数单位
# ma1=1+2j
# ma2=2+3j
# print(ma1+ma2)

# 4z字符串str
# 特点：需要加上引号，单引号和双引号都可以使用，包含了多行内容的时候可以使用三引号
# name =sixstar #报错没有引号识别成变量名 sixstar并没有被赋值
# name="sixstar"
# name="""sixstar"""
# name='sixstar'
# print(type(name))
# print(name)

"""
注释 不会被执行
print(123)
"""
from tkinter.font import names

# 注意多行注释和用三引号的字符串类型的区别，多行注释是单独存在的前面不需要变量名 =

# 5格式化输出
# 5.1占位符
# 生成一定格式的字符串
# 5.2 %
# 1. %s 字符串（常用）
# name="bingbing"
# print("我的名字：%s" % name)
# 占位符只会占据位置，并不会被输出

# 2. %d 整数（常用）
# age=18
# print("我的年龄：%d" % age)
# 加在一起使用
# age=18
# name="bignbing"
# print("我的年龄%d,我的名字%s" % (age,name) )

# 3. 4d 整数
# 数字设置位数，不足前面补空白
# a=123
# print("%04d" % a) #表示输出的整数显示位数，不足的话用0补全，超出当前位则原样输出。

# 4. %f 浮点小数
# a=1.512342
# print("%f" % a)

# 5. %4f 浮点小数
# a=2.34567
# print("%.3f" % a) # 不加.e显示6位小数

# 6. %%
# print("我是%%的1%%" % ())

# 7. 3f格式化
#格式化：f"{表达式}"
# name ="bingbing"
# age =18
# print(f"我的名字{name}，我的年龄{age}。")

