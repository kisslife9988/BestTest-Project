#内置函数--Python自带的函数
#input()\type()\print()\len()\enumerate()\list()\dict()\tuple()\set()\str()\int()\float()\bool()
# num = [1,2,3,4,5,7]
# print(max(num))
# print(min(num))
# num = round(6.2392,3) #取几位小数
# print(num)
#sorted（）方法
#list可以排序，方法是sort方法；字符串排序使用sorted方法
# s = '12345567'
# print(sorted(s))
# print(list(reversed(sorted(s)))) #倒叙排序方式一
# print(sorted(s,reverse=True)) #倒叙排序方式二
# list1 = [1,4,5,2,7,0,9]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

#ord（）、cha（）方法
# import string
# list = list(string.ascii_uppercase)
# print(list)
# for i in list:
#     # print('%s 的对应的数字值：%s'%(i,ord(i)))  #把字母转成阿斯科表里面的数值
#     print("%s 对应的字母是：%s"%(ord(i),chr(ord(i)))) #把数字转成阿斯科表里面的字母
#     # print('================================')
#any（）方法
# res = any([0,1,2]) #如果这个list里面有一个为真，就放true 否则就返回false
# print(res)
# res = any((0,0,0))
# print(res)
#all（）方法
# res = all([0,2,3,4]) #如果list中全部为真返回true，否则返回false
# print(res)
# res = all([1,2,3,4])
# print(res)

#dir（）方法
# import hashlib
# m = hashlib.md5('adb3'.encode())
# print(dir(hashlib))
# print(dir(m))  #获取帮助信息
# list = [1,2,3,3]
# print(dir(list))
#eval()方法
# res = eval('12+1')  #执行简单的Python代码
# print(res)
# res = eval('{"a":1321}')
# print(res)
#
# f = open('a.txt').read()
# print(type(f))
# res = eval(f)
# print(res)
# print(type(res))

# exec()执行Python代码
# res = '''
# def my():
#     print("123")
# my()
# '''
# res1 =exec(res)

#map()方法  循环帮你调用函数，然后保存函数的返回值的，放到一个生成器中，需要使用list强制类型转换成list列表；map后边传入的值只有可以循环都可以
# l = [1,2,3,4,5,6]
# l2 = []
# def bl(i):
#     return str(i).zfill(2)
# # for i in l:
# #     l2.append(bl(i))
# # print(l2)
# #如果使用map方法那就简单了
# res = list(map(bl,l))
# print(res)

#filter()方法，过滤传入的数据，也是循环过滤调用函数的，如果函数返回的值是真的，那么就保存这个值（不是返回值哦）

# l = [0,1,2,3,4,5,6]
# l2 = []
# def bl(i):
#     return str(i).zfill(2)
# def b2(i):
#     if i > 3:
#         return True
# res = set(filter(bl,l))
# res1 = list(filter(b2,l))
# print(res)
# print(res1)
# print(frozenset({1, 2, 3, 3}))  # 定义一个不可修改的集合
# print(globals())  # 返回程序内所有的变量，返回的是一个字典

dic = {2: 2, 1: 4, 5: 6, 7: 8}
print(sorted(dic.items()))  # 按照字典的key排序
print(sorted(dic.items(), key=lambda x: x[1]))  # 按照字典的value排序