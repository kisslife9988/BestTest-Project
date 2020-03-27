#标准模块，OS模块介绍
import os
# os.remove() #删除文件
# os.rename() #文件重命名
#mkdir 只能创建单层次的文件夹；创建多层文件夹时会报错；makedirs不仅可以创建单层文件夹还能创建多层文件夹
# os.mkdir('python') #创建一个文件夹
# os.makedirs('python2')
# os.mkdir('china1/beijing')
# os.makedirs('china/beijing')

# os.removedirs('python')  #只能删除空文件夹，如果文件夹有内容是删除不了的
# print(os.listdir('D:\\'))  #显示该目录下的所有文件和文件夹，如果不传显示当前文件下面内容
# print(os.listdir())
# print(os.path.isdir('python21')) #判断是否是文件夹，可以写绝对路径；也可以判断文件是否存在，不存在返回false
# print(os.path.isfile('上周回顾1.txt')) #判断是否是文件可以写绝对路径；也可以判断文件是否存在，不存在返回false
# print(os.path.exists('china1')) #判断文件或者文件夹是否存在，存在返回true 不存在返回false

#统计E盘下面有多少个Python文件
#os.walk 方法，可以将指定文件路径下所有的文件及文件夹找出来；
    # 其有三个返回参数；
#       当前目录
#       目录下的文件
#       目录下的文件夹
res = os.walk('china')
for cur_path,dirs,files in res:
    print('当前目录：',cur_path)
    print('当前目录下所有文件',files)
    print('当前目录下所有文件夹：',dirs)
    print('==========================')
#
# res = os.walk('china')
# count = 0
# for cur_path,dirs,files in res:
#     for f in files:
#         if f.endswith('.py'):
#             count += 1
# print(count)
#查找文件路径
def find_file(path,keyword):
    '''查找文件路径'''
    res = os.walk(path)
    for cur_path,dirs,files in res:
        for file_name in files:
            if keyword in file_name:
                print('该文件在%s目录下'%cur_path)
find_file('G:\\','fullstack')
print('===============================')
# os.system('dir') #执行操作系统命令，无法返回执行的结果
# res = os.popen('ipconfig') #用来执行操作系统的命令，可以返回执行的结果
# print(res.read())
print('===============================')
#路径的拼接
# os.path.join()
# print(os.path.join('china','OS模块.py')) #拼接路径
#删除文件
# res = os.walk('china')
# count = 0
# for cur_path,dirs,files in res:
#     print(cur_path)
#     for f in files:
#         if f.endswith('.py'):
#             # os.remove(cur_path + '/' + f)
#             os.removedirs(os.path.join(cur_path,f))
#
print('===============================')
#路径的分割
# res = os.path.split(r'D:\besttest-学习资料\双鱼座-Python\自动化视频\day15\复习.exe')  #用例分割文件名和文件路径
# print(res)
print('===============================')
#取父目录
# res = os.path.dirname(r'D:\besttest-学习资料\双鱼座-Python\自动化视频\day15\复习.exe')
# print(res)
# #取文件大小
# # print(os.path.getsize('上周回顾.txt')) #单位是字节
# #取当前目录
# print(os.getcwd()) #取当前目录
# #进入到哪个目录下
# print(os.chdir(r'G:\besttest-jyz-code\BestTest-Project\day5'))
# print(os.getcwd())
# #获取文件的创建时间、修改时间、更新时间
import time
# print(time.ctime(os.path.getctime('OS模块.py'))) #获取文件修改时间
# print(os.path.getmtime('OS模块.py'))  #获取文件创建时间
# print(os.path.getatime('OS模块.py')) #文件最近访问时间
















#复习练习
os.mkdir('test') #在当前目录下创建一个test文件夹
os.makedirs(r'test\test1\test11') #在test目录下创建递归文件夹
os.rename('test','study') #将当前目录下的test文件夹修改名称为study
os.remove('aa.txt') #删除当前目录下的aa.txt文件（可以指定目录）
os.removedirs(r'study\test1') #会报错，因为test1下边有文件
print(os.getcwd())#获取当前目录的路径
print(os.chdir(r'G:\\')) #修改文件/文件夹路径
print(os.path.isdir('study')) #判断study是否是文件夹
print(os.path.isfile('OS模块.py')) #判断os模块是否是文件
print(os.path.exists('study')) #判断文件或者文件夹是否存在，存在返回true 不存在返回false
print(os.path.join(r'study\test1','OS模块.py')) #将path和文件组成一个新的路径
print(os.path.split(r'c:\test\test1\a.txt')) #把文件路径分割成文件和文件路径两部分并返回一个元组
print(os.path.dirname(r'c:\test\test1\a.txt')) #返回a.txt文件的父目录路径
print(os.path.getsize('OS模块.py')) #返回os文件的大小
print(os.path.getctime('study')) #显示创建时间
print(os.path.getatime('study')) #显示文件夹最近访问时间
print(os.path.getmtime('study')) #显示文件夹最近修改时间