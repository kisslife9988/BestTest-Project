#递归调用，即函数自己调用自己；递归可以实现循环但是效率没有循环效率高；可以实现循环的效果
#递归最多999次
# count = 0
# def say():
#     global count
#     count += 1
#     print(count)
#     print('say')
#     say()
# say()

def test():
    num = int(input('please input number:'))
    if num %2 != 0: #判断输入的数字是不是奇数
        return True  #如果是奇数的话，退出程序返回True
    print('不是偶数')
    return test() #如果不是奇数，继续调用自己，输入值
print(test())
#
'==========================================================='
#函数之间的调用，参数的传参
#1、参数调用方式
def db_connect (ip,user,password,db,port):
    print(ip)
    print(user)
    print(password)
    print(db)
    print(port)
db_connect(user='wyh',port=3306,db=1,ip='1.2.2.2',password='wyh')
db_connect('1.1.1.1','root',db=2,password='wyh',port=3306)
#关键字调用的时候不能写在最开始位置，除非所有调用都有对应的关键字；
