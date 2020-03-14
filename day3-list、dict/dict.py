dict1 = {
    'test1':'123',
    'test2':'345',
    'test3':567
}
#字典的查找
print(dict1['test1'])  #如果key不存在，那么字典会报错
print(dict1.get('test11')) #如果字段没有key的值则返回为none，也可以指定返回的默认值
print(dict1.get('test11','没有此值'))
print(dict1.values()) #打印所有的值
print(dict1.keys())
#字典的添加
dict1['test4'] = 'wyh' #如果key的不存在则直接添加，如过key的值有值则会修改原来的数据
print(dict1)
dict1.setdefault('age',19)  #如果key已经存在，则不在重新赋值

#字典的修改
dict1['test4'] = 'wyh1'
#字典的删除
dict1.pop('test4')  #直接打印返回，删除的值
print(dict1)
del dict1['test1']
print(dict1)
dict1.popitem()  #随机删除
print(dict1)
dict1.clear()  #清空字典
print(dict1)
#字典的合并
dict2 = {'name':'wyh','age':30}
dict1.update(dict2) #字典的合并
print(dict1)
print('******字典的循环******')
#字典的循环
dict1 = {
    'test1':'123',
    'test2':'345',
    'test3':567
}
for i in dict1:
    print(i)
    if i == 'test1':
        print(dict1['test1'])

for k,v in dict1.items():
    print(k,v)
#字典的嵌套
all_stus = {
    'wyh':{
        'test':123,
        'test1':[1,2,3]
    },
    'age':{
        'test': 1234,
        'age': 18
    }
}

all_stus['wyh']['test1'].append(8888)
print(all_stus)
print(len(all_stus['wyh']['test1']))
all_stus['wyh']['test'] = 9898
print(all_stus)
