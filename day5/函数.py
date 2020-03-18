#函数的定义
'''
def 函数名（参数列表）:
    函数体
1、函数体重定义的变量都是局部变量
2、return函数返回调用函数后的结果
3、位置参数：参数列表中的必填参数叫做位置参数
4、默认值参数：即参数列表中定义的变量有值
'''
#例：默认值参数
def db_connect(ip,port=3306):
    print(ip,port)
db_connect('1.1.1.1')
db_connect('1.1.1.1',3307)

#既能写文件，又能读文件
import json
def op_file(file_name,dic=None):
    if dic:
        with open(file_name,'w',encoding='utf-8') as fw:
            json.dump(dic,fw,indent=4,ensure_ascii=False)
    else:
        with open(file_name,encoding='utf-8') as f:
            content = f.read()
            if content:
                res = json.loads(content)
            else:
                res = {}
        return res