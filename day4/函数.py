#函数也叫方法。实现特定功能的代码，可以提高代码的复用性
#一个函数只做一件事情
#函数的定义
def my():
    print('函数!')
#函数必须得调用才能使用
my()  #函数的调用
print(my) #打印出函数的内存地址
import json
# def get_file_name(file_name): #file_name 形参，形式参数
#     #入参：传入一个文件名
#     #返回值：文件内容转成字典，返回
#     with open(file_name,encoding='utf-8') as f:
#         res = json.load(f)   #局部变量，在函数中定义的变量只能在干函数中使用，称为局部变量
#         print(res)
#         return res
# res = get_file_name('stus.json') #stus.json实参，实际参数
# # print(res)

def write_file(filename,content):
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(content,f,ensure_ascii=False,indent=4)
        # f.write(json.dumps(content))
d = {'name':'wyh','name2':'gaobo'}
write_file('test.json',d)









