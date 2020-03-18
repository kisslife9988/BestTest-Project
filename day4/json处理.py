#常用方法：
    # loads():json串(字符串)，转成字典；json的定义只能用双引号不能用单引号
    # dumps():将字典，转换成json串；indent方法是用来进行缩进的可以以json格式进行显示;ensure_ascii=false中文可以正常显示
    # load():json转成字典，直接传递文件对象，不用传递文件内容
    # dump():

    # load()和loads()的区别，load传递的是文件对象，loads传递的文件中的内容
# json 通用的数据类型，所有的语言都认识；格式为：K-V格式；
# json不能直接通过字典的方式取值，实际上它是字符串格式，需要转成字典格式才行
s = '''{
    "test":1,
    "test2":23,
    "test3":{
        "wyh":521
    }
}'''
import json
res = json.loads(s)  #json串(字符串)，转成字典；json的定义只能用双引号不能用单引号
print('原始数据：',s)
print('JSON对象：',res)
print(res.keys())
print(type(res))

stus = {'test':123456,'test2':780,'test3':0000,'高博':'我爱你'}
print(type(stus))
res2 = json.dumps(stus,indent=4,ensure_ascii=False) #将字典，转换成json串；indent方法是用来进行缩进的可以以json格式进行显示;ensure_ascii=false中文可以正常显示
print(res2)
print(type(res2))
with open('stus.json','w',encoding='utf-8') as f:
    f.write(res2)
print('===================load和loads的区别======================')
f = open('stus.json',encoding='utf-8')
content = f.read()
user_dic = json.loads(content) #传递文件内容
print(user_dic)

f = open('stus.json',encoding='utf-8')
user_dic = json.load(f) #创建文件对象
print(user_dic)
f.close()
print('====================dump和dumps的区别=====================================')
f = open('stus2.json','w',encoding='utf-8')
json.dump(stus,f,indent=4,ensure_ascii=False)
f.close()
print('=====================with方式打开文件=====================')
with open('stus3.json','w',encoding='utf-8') as f:
    json.dump(stus,f,indent=4,ensure_ascii=False)

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", data)
print("JSON 对象：", json_str)