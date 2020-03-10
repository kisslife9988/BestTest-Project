# # 打印语句print
# print("hello world!")
# #一、定义变量，变量用来存储东西的。格式：变量名 = 变量值
# #   变量名的命名规则：
# #       1、系统保留的关键字不可以用
# #       2、变量必须由字母或者下划线开头，不能以数字开头
# #       3、变量是由字母、数字、下划线构成的字符序列
# # 变量定义中，不管是单引号还是双引号都是成双成对使用的。
# IP = "118.24.3.40"
# name = 'xiao jun'
# print(IP,name)
#
# #输入语句input
# name = input("please input Your name:")
# print(name)

# #二、条件判断语句
# if name == 'wyh':
#     print('答对了')
# elif name == 'test':
#     print('真不错！')
# else:
#     print('答错了！')
# print(type(name)) #查看变量所属的类型

# #三、循环语句，while循环
# #   循环就是重复做同一件事情（循环=遍历=迭代）
# #   用while循环必须得有一个计数器；用来记录循环的次数，从而达到控制循环退出
# #   while + else else的执行是在循环正常结束之后才开始执行的
#
# count = 0 #计数器，控制循环次数
# while count < 10:
#     count += 1
#     print('count 小于 10',count)
#     if count == 6:
#         # break   #退出循环体
#         continue    #结束本次循环，继续执行下一次循环
#     print(count)
# else:
#     print('终于执行我了！')

# #for 循环，不需要去定义计数器来控制循环
# for count in range(4):
#     print('haha')
# var = 'abcd12345'
#
# for i in var:
#     print(i)
# else:
#     print('ok')
#
# for i in range(len(var)):
#     print(i)

# 四、字符串格式化
# 第一种方式，s%  通过格式；d%只能是整数；f%为小数，想保留几位小数就写 .2f  以此类推
import datetime
print(datetime.datetime.today())
name = 'wyh'
date = datetime.date.today()
welcome = '%s,您好！今天的日期是%s'%(name,date)
print(welcome)
#第二种方式，通过+ 号连接
print(name + 'hahah' + 'ads')
#第三种方式，参数较多的时候，可以使用format的方式
sql = 'insert into student (id,name,sex) values'\
'("%s","%s","%s")'
sql2 = 'insert into student(id,name,sex) values'\
    '({id},{name},{sex})'
sql3 = sql2.format(id = 2 , name = 'wyh' , sex = 'boy')
word = '你的名字{name}  你的年龄{age}'.format(name='wyh',age = 10)
print(sql3,word)
