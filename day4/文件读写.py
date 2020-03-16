'''
1、找到操作的文件；
2、打开文件
3、操作文件进行读写
4、关闭
文件操作的模式：读、写、追加三种模式，默认为只读模式
     r:只能读，不能写；打开文件不存在，则报错
     rb：读取二进制文件的内容
     w:只能写，不能读；写入会清空原来的文件内容，
     wb：写入二进制文件
     a:追加写，不能读；如果打开的文件不存在会新建一个文件；在文件的末尾进行追加
     r+: 读写模式;打开不存在的文件，报错；可以写入但是写入的文件会从文件的顶部开始覆盖原文件
     w+: 写读模式，能读文件，但是由于会清空文件内容，所以读到的内容都是空
     a+：追加读模式，文件不存在创建一个新的文件；既能读文件也能写入文件
     ab:追加模式的二进制写
读文件方法：
    read（）方法：读取文件中的素有内容，以字符串的方式进行展示
    readlines方法：获取文件中所有内容，把每一个行内容存入一个list表中，且没一行内容代表一个元素
    readline方法：获取文件中的每一行的内容，以字符串形式展示
写文件方法：
    write（）方法：只能写字符串
    writelines（）方法：将list中的元素写入文件中
修改文件内容：

其它方法：
    seek（）方法：确定文件指针的位置
    flush（）方法：刷新缓冲区，即立即把缓冲区里面的内容写入磁盘
    tell()方法：记录文件指针的当前位置
    truncate()方法：清空文件的内容，需要配置指针使用
    注意：如果写入文件报错的话需要制定字符编码
'''
# a = ['wyh123231661,1243\n','test1玩儿玩儿玩儿11,1234\n']
# f = open('users.txt','r+',encoding='UTF-8')
# print(f.read())
# print('二次读取',f.read())
# print(f.readlines())
# f.flush()
# f.seek(0)
# print(type(f.readline()))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.writelines(a)
# f.close()

#打开二进制文件的时候（比如图片、或者其它）
#链接的URL地址：
import requests   #导入requests模块
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1584945092&di=ba5f1891ad196f22cb25394d459780d5&imgtype=jpg&er=1&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2F40bbc6dc7f5691d5ee1e4f1aeaa307f4f745ee41.jpg'
res = requests.get(url).content  #打开URL地址并以二进制形式进行读取
f = open('changba.jpg','wb') #以读模式打开文件
f.write(res)
f.close()
# print('============文件的高效处理===========')
#如何高效的处理文件
#读文件的时候一次只取一行去读取文件
#使用while循环方式，读取文件
# f = open('users.txt',encoding='utf-8')
# while True:
#     line = f.readline()
#     if line != '':
#         print('line:',line)
#     else:
#         print('end')
#         break
# f.close()
# print('====for 循环读取====')
#使用for循环方式，读取文件
f = open('users.txt',encoding='utf-8')
f.seek(0)
for line in f:
    print(line)
f.close()
# print('===文件读取的练习===')
'''
    例子6：监控日志
        1、从日志里面找到，1分钟之内超过20次访问的IP
        2、脚本没分钟运行一次
    思路：
        1、读取文件内容，获取IP地址
        2、把每个IP地址存起来,使用字典存储（避免重复）
        3、判断IP访问的次数是否超过20次
        4、加入黑名单

'''
import time
point = 0
while True:
    ips = {}
    f = open(r'C:\Users\Administrator\Desktop\access.log', encoding='utf-8')  #文件前边加入r代表路径中的特殊字符不会被转义
    f.seek(point)
    for line in f:
        ip = line.split()[0]
        if ip in ips:
            ips[ip] += 1
        else:
            ips[ip] = 1
    point = f.tell()  # 记录文件指针的位置
    for ip, count in ips.items():
        if count >= 20:
            print('%s  加入黑名单！' % ip)
    f.close()
    time.sleep(60)

# print('=================修改文件内容================')
#把users文件中的test修改为wyh
#方式一：
# f = open('users.txt')
# res = f.read().replace('test','wyh')
# f.close()
# f = open('users.txt','w')
# f.write(res)
# f.close()
#方式二:如果文件过大会导致内存不够的问题
# f = open('users.txt','a+')
# f.seek(0)
# res = f.read().replace('gaobo','521')
# f.seek(0)
# f.truncate()   #清空文件里面的内容
# f.write(res)
# f.close()
#方式三：
import os  #导入os模块
# f = open('users.txt')
# f2 = open('users.txt.bat','w')
# for line in f:
#     new_line  = line.replace('list','test')  #将文件内容中的list修改为test
#     f2.write(new_line)  #将修改的内容，添加到文件2中
# f.close()
# f2.close()
# os.remove('users.txt')  #删除原文件
# os.rename('users.txt.bat','users.txt')   #将修改后的问题重命名

#打开文件时，使用with方式打开会自动关闭文件;如果同时打开多个文件，使用逗号进行分割：
# import os
# with open('users.txt') as f:
#     for line in f:
#         print(line)
# with open('users.txt') as f ,open('users.txt.bat','w') as f2:
#     for line in f:
#         new_line = line.replace('521','gaobo')
#         f2.write(new_line)
# os.remove('users.txt')
# os.rename('users.txt.bat','users.txt')

# with open('test.txt','a') as f: #以最近方式对文件进行操作
#     f.write('test11') #往文件中写入数据

a = ['list1\n','list2\n','list3\n']
f = open('test.txt','w')
f.writelines(a)
f.close()
f = open('test.txt')
print(f.read())
f.close()