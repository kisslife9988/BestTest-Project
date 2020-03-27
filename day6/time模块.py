#time模块，进行和时间相关的操作
import time
# time.sleep(1) #设置休眠时间
#时间的表示方式
#1、格式化好的时间；2、时间戳显示（时间戳，从计算机诞生到现在过了多少秒的时间）
#时间戳计算时间比较好计算，将其转换成秒来计算
# print(time.strftime('%Y%m%d'))
# print(time.strftime('%Y-%m-%d'))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))  #取当前格式化时间
# print(time.time()) #获取当前的时间戳，精确到毫秒，有小数点，如果不想要 转换成int类型即可
# print(int(time.time()))

# 如果想把时间戳转换成格式化好的时间，或者反过来；则必须将其先转换成时间元祖
# 把格式化时间修改
# 1、先把格式化好的时间转成时间元祖
# 2、然后时间元祖在转成时间戳
# 1992-01-03
# res = time.strptime('1992-01-03 19:23:59','%Y-%m-%d %H:%M:%S')
# print(res) #把格式化好的时间转换成时间元祖
# print(time.mktime(res))

#转换成时间戳的方法.
def str_to_timestamp(time_str=None,format='%Y%m%d%H%M%S'):
    '''格式化好的时间转时间戳，如果不传参数返回当前时间'''
    if time_str:
        time_tuple = time.strptime(time_str,format) #把格式化好的时间转成时间元组
        timestamp = time.mktime(time_tuple)
    else:
        timestamp = time.time()
    return int(timestamp)
# print(str_to_timestamp())
# print(str_to_timestamp('20391123175123'))
# print(str_to_timestamp('2013-08-09','%Y-%m-%d'))

#时间戳转格式化好的时间
#1、先把时间戳转成时间元祖

# res = time.gmtime(time.time())  #gmtime把时间戳转成时间元组，但是会将时间转换成标准时区的时间
# print(res)
# res = time.localtime(time.time())  #把时间戳转成时间元组，将时间转换成当前时区的时间
# test = time.strftime('%Y-%m-%d %H:%M:%S',res)
# print(test)

def timestamp_to_strtime(timestamp = None,format = '%Y-%m-%d %H:%M:%S'):
    '''1、把时间戳转成格式化好的时间；2、如果不传入时间戳，那么就返回当前的时间'''
    if timestamp:
        time_tuple = time.localtime(timestamp)  # 把时间戳转成时间元组，将时间转换成当前时区的时间
        str_time  = time.strftime(format,time_tuple) #格式化输出时间元组
    else:
        str_time = time.strftime(format)
    return str_time

# 例子：取50年后的时间
# 分析用当前的时间戳+50年的秒数，然后把时间戳转成格式化好的时间
time_str = str_to_timestamp() + (3*30*24*60*60)
res = timestamp_to_strtime(time_str)
print('50年后的时间：',res)


