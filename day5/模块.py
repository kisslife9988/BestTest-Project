'''
    模块：即一个Python文件
        1、标准模块
        2、第三方模块
        3、自己写的Python模块
'''
import time,os,datetime,json  #安装完Python直接可以用的都是标准模块
import random
# print(random.randint(1,100)) #随机在1-100之间产生一个整数
# print(random.uniform(1,1000)) #随机产生一个1-1000之间的小数
# stu = ['1','2','3','4','5','6']
# print(random.choice(stu)) #随机选择一个元素，choice只要是可以循环的都可以取值
# print(random.sample(stu,2)) #随机取N个值
# # res = random.sample(stu,2)
# print(res)
# res2 = ''.join(res)
# print(res2)
# print(random.shuffle(stu)) #洗牌，打乱顺序，无返回值；只能传入list
# print(stu)
#
# # a = ['test1\n','test2\n','test3\n']
# # with open('test.txt','a+',encoding='utf-8') as f:
# #     f.writelines(a)
# with open('test.txt') as f:
#     res = f.read()
# print(res)
# res = res.split()
# print(res)
# # for i in res:
# #     print(i)
#随机生成的一个实数，它在[0,1)范围内
# print(random.random())
# print(random.randrange(1,100))  #生成一个1到100的随机整数
# print( random.randrange(1,100,5) ) #生成一个1到100的间隔为5的随机整数
#
import time,datetime
# print(time.time()) #获取当前的时间戳
# time.sleep(1)  #休眠5秒，继续执行程序
# print(time.gmtime()) #把时间戳转换成时间元组，如果不传的话，默认取标准时区的时间戳
# print(time.strftime("%Y %m %d %H:%M:%S"))#将时间元组转换成格式化输出的字符串
# print(time.strptime("20160204 191919","%Y%m%d %H%M%S"))#将格式化的时间转换成时间元组
# print(time.mktime(time.gmtime())) # 把时间元组转换成时间戳
# print(time.localtime()) #把时间戳转换成时间元组，如果不传的话，默认取当前时区的时间戳
# print(time.asctime())#时间元组转换成格式化时间
# print(time.ctime())#时间戳转换成格式化时间
# print(time.timezone)#和标准时间相差的时间，单位是s

print(datetime.datetimw(e.no)) #获取当前时间并格式化输出
print(datetime.datetime.now() + datetime.timedelta(3)) #计算三天后的时间
print(datetime.datetime.now() + datetime.timedelta(-3)) #三天前的时间
print(datetime.datetime.today()) #获取当前的时间
print(datetime.date.today()) #获取当前的日期