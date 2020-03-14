'''
1、找到操作的文件；
2、打开文件
3、操作文件进行读写
4、关闭
文件操作的模式：读、写、追加三种模式，默认为只读模式
     r:
     w:会清空原来的文件
     a:在末尾追加写入
     r+:
     w+:
     a+：
'''
f = open('test.txt','a+')
# print(f.read())
# f.write('yangfan,123456\n')
f.seek(0) #移动文件指针
# print(f.read())
dict1 = {}
for i in f.readlines():
    print(i.strip().split(','))
    r = i.strip().split(',')
    dict1[r[0]] = r[1]
    print(dict1)
f.close()