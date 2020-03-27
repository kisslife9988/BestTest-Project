'''
数据库：
    关系型数据；
        数据库、表
        通过SQL来操作
    非关系型数据库：Redis、mongodb、memcache
        没有数据表、没有SQL语句
        数据的存储是以k-v形式的
        redis--读取数据非常快，每秒支持30万次的读写；它的数据全部都是放在内存中的
    使用工具修改数据库：
        select  数据库名称
        set  K  v  添加数据
        get  k   取值
        在添加key的时候如果：session：test  /  12323，那么会在库里面创建一个session的文件夹，文件夹下边有数据test：12323
    如果使用Python操作需要安装Redis模块
'''
import redis
ip = '118.24.3.40'
password = 'HK139bc&*'

r = redis.Redis(host=ip,password=password,port=6379,db=1,decode_responses=True) #port有默认值6379,加入decode_responses=True 就不需要将二进制数据转换成字符串了，不加需要转换
#针对的都是string类型的数据
# res = r.get('name')
# print(res)
# s = '123'
# print(s.encode()) #字符串变成bytes类型，二进制类型
# print(res.decode()) #decode是bytes类型，转成字符串
# r.flushdb() #删除这个数据库里所有的key
# r.set('name','这是一个测试！',60) #新增和修改数据k-v-失效时间，默认-1,永远生效；60代表一分钟内生效；setex查询？
# r.delete('name') #删除指定的key
# r.set('python:os','listdir,path')
# res = r.get('python:os')
# print(res)
# print(r.keys()) #获取所有的key
# print(r.keys('na*')) #括号可以写入模糊匹配



#Redis哈希类型，hash类型：二层字典如下：
# session = {
#     "name":{'sex':18,'age':19},
#     "add":{'sex':20,'age':21}
# }

# r.hset('syz_stus','test','21345')  #存储hash类型的数据的是格式：K-k-v,如上面的格式 ，添加hash类型数据
# res = r.hget('syz_stus','test') #指定获取小k的值
# print(res)
# r.delete('syz_stus') #删除大K，即删除整个数据
# r.hdel('syz_stus','test') #删除指定的小K，删除大K里面的小K的值
# res = r.hgetall('jnz_stus')  #以字典的格式获取到大K里面所有的数据，格式是二进制类型
# print(res)
# new = {}
# for k,v in res.items():
#     new[k.decode()] = v.decode()
# print('============')
# print(new)



# import redis  #导入模块
# ip = '118.24.3.40'
# password = 'HK139bc&*'
# r = redis.Redis(host=ip,password=password,db=1,decode_responses=True) #连接redis，,默认值port=6379
# r.set('sex','女')
# res = r.get('sex').decode()  #获取key=sex的value值；且获取的结果是一个二进制类型的数据,所以需要decode转成字符串类型的数据
# r.delete('sex1') #删除key=sex1的value值
# res = r.get('sex')
# print(res)
# r.set('java:test','JAVA-language') #在数据库中添加了一个名词为JAVA的文件夹，文件夹下有数据key:java:test,value:JAVA-language
# print(r.keys())  #获取所有key
# print(r.keys('*a*'))  #获取所有key中包括a字母的key

#读取所有数据库中key的值
# key_list = []
# for i in r.keys():
#     key_list.append(r.get(i))
#     print('key:%s,value:%s'%(i,r.get(i)))
# print(key_list)

#哈希类型练习
import redis  #导入模块
ip = '118.24.3.40'
password = 'HK139bc&*'
r = redis.Redis(host=ip,password=password,db=1,decode_responses=True) #连接redis，,默认值port=6379
r.hset('syz_stus','test1','21345')  #存储hash类型的数据的是格式：K-k-v,如上面的格式 ，添加hash类型数据
r.hset('syz_stus','test','哈哈哈')  #数据hash类型数据值
# res = r.hget('syz_stus','test')  #获取某一个小key的值
# res1 = r.hgetall('syz_stus') #以字典的格式获取到大K里面所有的数据，格式是二进制类型
# print(res,res1)
# r.hdel('syz_stus','test') #删除指定的小K的数据
# r.delete('syz_stus') #删除整个大K的所有数据

#循环的使用
res = r.hgetall('syz_stus')  #以字典的格式获取到大K里面所有的数据，格式是二进制类型
print(res)
new = {}
for k,v in res.items():
    new[k] = v
print('============')
print(new)