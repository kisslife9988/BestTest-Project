'''
导入模块
1、导入模块的顺序
    1、先从当前目录下找这个模块寻找
    2、再去环境变量里找
2、导入模块的实质
    就是把这个Python文件运行一次

'''

# import m1
# m1.f1()
# print(m1.name)

# import random
# print(random.randint(1,9)) #由于在本目录下定义了random模块，所以在掉用该方法的时候去当前目录查找的时候没有randinit方法，所以报错
# 临时加入环境变量，调用模块
import sys
# print(sys.path) #打印python的环境变量目录
sys.path.insert(0,r'G:\besttest-jyz-code\BestTest-Project\day6') #将变量加入环境变量的开头，避免查询所有 的环境变量
# sys.path.append(r'G:\besttest-jyz-code\BestTest-Project\day6') #临时生效，将路径加入都Python环境变量的末尾
# print(sys.path)
import 加密模块hashlib as m
res1 = m.my_md5('123')
print(res1)

#pycharm下导入环境变量
# 选择文件右击>选择Mark Direc as>Sources Root  即可将文件加入Python的环境变量中
#   如果取消的话，同样选择文件右击>选择Mark Direc as>unmark as Sources root

from day4 import json处理  #从day4模块中导入部分功能
from day2.Python_JiChu import *

