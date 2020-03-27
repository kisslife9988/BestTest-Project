'''
第三方模块的使用需要自己手动安装
xpinyin模块，把汉字转换成拼音
第三方模块的安装
    1、傻瓜式安装，使用Python自带的pip命令进行安装
    2、手动安装
        .tar结尾的安装：
            1、先解压文件，解压后进入到这个目录下
            2、执行：Python setup.py install方式安装
        .whl结尾的安装：
            直接使用pip install C:\XX\XXX\XXX.whl 文件（文件绝对路径/相对路径）
    注意当电脑中存在多个版本时，当安装模块时，可以使用PythonX.X -m -pip install XXX 的方式来安装文件到指定的Python中
'''

import xpinyin
r = (xpinyin.Pinyin()) #实例化
# print(r.get_pinyin('测试','')) #第二个参数指定汉字连接的格式，默认使用“-”进行连接；


'''
操作数据库：
    1、需要知道IP、账号、密码、端口号
    2、第一步连接数据库
    3、第二步创建游标（）
    4、
'''

host = '118.24.3.40'
user = 'jxz'
password = '123456'
db = 'jxz'
port = 3306   #端口号只能写int类型

import pymysql
# connect = pymysql.connect(host = host,password = password,user = user,db =db,port=port,charset = "utf8") #charset只能写utf8不能写utf-8
# cur = connect.cursor() #建立游标
# cur.execute('show tables;')  #执行sql语句，只是执行SQL并不会返回数据值
# cur.execute('select * from app_myuser limit 5;')
    # print(cur.) #获取数据库里面的所有结果,返回一个二维数组
# print('fetchone:',cur.fetchone()) #获取数据库里面的一条结果，返回一个一维数组；当查询的数据条数很多的时候使用fetchall最合适，如果查询结果只有一条则用fetchone比较合适
#插入语句
# SQL = "insert into app_myuser(id,username,passwd,is_admin,error_count,balance)VALUE (19,'test11','123456',8887,0,None);"
# cur.execute(sql)
# connect.commit() #提交sql，如果在连接数据库时定义了autocommit = True那么在插入数据库的时候就不用在执行commit了

# sql = 'select * from app_myuser limit 5;'
# cur.execute(sql)
# print(cur.description) #获取这个表里面的所有字段（表结构）
# #数据库操作后都要进行关闭避免超过最大连接数
# cur.close()
# connect.close()

#定义连接数据库的函数
# def my_db(ip,user,password,db,sql,port = 3306,charset = 'utf8'):
#     conn = pymysql.connect(host = ip,user = user,password = password,db = db,port = port,charset=charset,autocommit = True)
#     cur = conn.cursor()
#     cur.execute(sql)
#     res = cur.fetchall()
#     cur.close()
#     conn.close()
#     return res
def my_db2(sql):
    conn = pymysql.connect(host = '192.168.0.105',user = 'root',password = '123456',db = 'szz',port = 3306,charset='utf8',autocommit = True)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res
# my_db2("insert into stu(id,name)value(3,'test1');")
# my_db2('select * from stu;')

def select_db(sql):
    '''查询模块'''
    #建立数据库的连接
    db = pymysql.connect(host = '192.168.0.105',user = 'root',password = '123456',db = 'szz',port = 3306,charset='utf8')
    # cur = db.cursor()  #通过 cursor() 创建游标对象
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql) #使用 execute() 执行sql
    data1 = cur.fetchone() #获取返回结果的第一个值
    data2 = cur.fetchmany(2) #获取返回结果的前两个值
    data = cur.fetchall() #获取数据库里面的所有结果,返回一个二维数组
    cur.close() # 关闭游标
    db.close() # 关闭数据库连接
    return data,data1,data2
select_sql = select_db("select * from stu;")
print(select_sql)

# def select_db(sql):
#     '''查询模块'''
#     #建立数据库的连接
#     db = pymysql.connect(host = '192.168.0.105',user = 'root',password = '123456',db = 'szz',port = 3306,charset='utf8')
#     # cur = db.cursor()  #通过 cursor() 创建游标对象
#     cur = db.cursor(cursor=pymysql.cursors.DictCursor)
#     cur.execute(sql) #使用 execute() 执行sql
#     db.commit()
#     cur.close() # 关闭游标
#     db.close() # 关闭数据库连接

# select_sql = select_db("update stu set name='test001' where name ='test00';")

# def select_db1(sql):
#     '''查询模块'''
#     #建立数据库的连接
#     db = pymysql.connect(host = '192.168.0.105',user = 'root',password = '123456',db = 'szz',port = 3306,charset='utf8',autocommit=True)
#     # cur = db.cursor()  #通过 cursor() 创建游标对象
#     cur = db.cursor(cursor=pymysql.cursors.DictCursor)
#     cur.execute(sql) #使用 execute() 执行sql
#     cur.close() # 关闭游标
#     db.close() # 关闭数据库连接
# select_sql = select_db1("update stu set name='test00' where name ='test001';")

# def select_db1(sql):
#     '''查询模块'''
#     #建立数据库的连接
#     db = pymysql.connect(host = '192.168.0.105',user = 'root',password = '123456',db = 'szz',port = 3306,charset='utf8',autocommit=True)
#     # cur = db.cursor()  #通过 cursor() 创建游标对象
#     cur = db.cursor(cursor=pymysql.cursors.DictCursor)
#     cur.execute(sql) #使用 execute() 执行sql
#     cur.close() # 关闭游标
#     db.close() # 关闭数据库连接
# select_sql = select_db1("delete from stu where name='test00';")