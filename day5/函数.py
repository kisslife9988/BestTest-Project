#函数的定义
'''
def 函数名（参数列表）:
    函数体
1、函数体重定义的变量都是局部变量
2、return函数返回调用函数后的结果
3、位置参数：参数列表中的必填参数叫做位置参数
4、默认值参数：即参数列表中定义的变量有值
'''
def my():
    res = '这是一个测试函数！'
    a = 123
    return res,a
res1= my()
print(res1)
#函数返回一个值
def my():
    res = '这是一个测试函数！'
    return res
res1= my()
print(res1)

#函数返回默认值
def my():
    res = '这是一个测试函数！'
res1 = my()
print(res1)



def calc(x, y):  # 这个就是定义了一个有返回值的函数
    c = x * y
    return c, x, y
res = calc(5, 6)  # 把函数的返回结果赋值给res
print(res)



def fun():  #定义一个名称是fun的函数
    print('hello world!')  #函数体：函数要实现的功能
fun()  #调用这个函数

def print_str(str):
    '打印输出传入的字符串'
    print('要打印的字符串是：',str)
test = 'Hello world!'
print(test)

#传不可变对象实例
# def ChangeInt(a):
#     print('修改前a的值：',a)
#     a = 10
#     print('函数内部的a:',a)
# b = 2
# ChangeInt(b)
# print(b)

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)







#例：默认值参数
def db_connect(ip,port=3306):
    print(ip,port)
db_connect('1.1.1.1')
db_connect('1.1.1.1',3307)
res = db_connect('1.1.1.1')
print(res)
#return 有两个作用：1、结束函数，只要函数里面遇到return结束函数的运行；2、返回函数处理结果
def my2():
    for i in range(50):
        return i
print(my2()) #返回NOne

def my3():
    # a = 1
    # b = 2
    # c = 3
    a,b,c =1,2,3
    return a,b,c
b,c,d = my3()
s = my3() #结果是一个元组
print(b,c,d)
print(s)

def my4(s:str,d:dict):  #s,传值类型为str；D为字典，目的是为了调用字符串、字典的方法；当然这里也可以传其它类型的数据，就和参数有默认值的使用方式是一致的
    print(s,d)
my4(123,"324")
#练习
def check_float(s):
    '''
    这个函数的作用就是判断传入的字符串是否是合法的小数
    :param s: 传入一个字符串
    :return: True/False
    '''
    s = str(s)
    print(s)
    if s.count('.') == 1:
        s_split = s.split('.')
        # left = s_split[0]
        # right = s_split[1]
        left,right = s_split
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left[1:].isdigit() and right.isdigit():
            print(left[1:])
            return  True
    return False
print(check_float(---2.3))
print(check_float(2.3))
print(check_float(-3.45))
print(check_float('a.2'))
print(check_float('1.22'))
print(check_float('---2.3'))

#既能写文件，又能读文件
# import json
# def op_file(file_name,dic=None):
#     if dic:
#         with open(file_name,'w',encoding='utf-8') as fw:
#             json.dump(dic,fw,indent=4,ensure_ascii=False)
#     else:
#         with open(file_name,encoding='utf-8') as f:
#             content = f.read()
#             if content:
#                 res = json.loads(content)
#             else:
#                 res = {}
#         return res