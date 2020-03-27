name = 'model1'
def f1():
    print('我是model1文件里面的f1')
print('我是model1文件里面的print')

#创建一个文件，并写入内容
f = open('test.txt','w')
f.write('我是model1模块文件里面写入的内容')
f.close()
print('脚本执行完毕!')