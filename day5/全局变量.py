import datetime
def get_today():
    print(datetime.datetime.today())\
#全局变量；如果全局变量是一个字典或者list则不需要声明可以直接进行修改；只有str、int、和元组才需要声明（即不可变的类型都需要进行声明）
name = 'wyh'  #全局变量
def get_name():
    # name = 'gaobo'  #函数内部的局部变量
    global name  #声明要修改的变量，为全局变量name；
    name = 'gaobo'
    print(name)
def get_name2():
    print('get_name2',name)
get_name2()
get_name()
print('外面的name：',name)


total = [1,2,3,4,5]  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total.append(6)  #修改全局变量
    print("函数内是全部变量 : ", total)
    return total
# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)
