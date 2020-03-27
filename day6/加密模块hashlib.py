#hashlib加密模块
import hashlib
# import md5 #在Python2中引用MD5模块，Python3中都在hashlib中
#MD5字符串的加密；MD5方式加密后是不可逆的无法解密（简单的可以解密比如123123，abcded）
#MD5解密的方式是撞库：把一些常用的密码生成后加密放入数据库，然后解密的时候去库里面匹配
# password = '123456'
# print(password.encode()) #字符串不能直接加密，必须把自己串转成二进制类型
# m = hashlib.md5(password.encode())
# print(dir(m)) #查看变量M可以使用的方法
# print(m)
# print(m.hexdigest())
# #补充知识点：加盐
#加盐的意思就是在本该加密的数据上边在新添加点其他的数据生成新的MD5加密秘钥，增加密码安全度

#加密函数方法
def my_md5(s:str,salt = None):
    '''
    :param s: 需要传入的加密数据
    :param salt: 加密数据+额外的补充数据（加盐）
    :return: 返回计算结果
    '''
    s = str(s)
    if salt:
        s = s + salt
    m = hashlib.md5(s.encode())
    # print(m)
    return m.hexdigest()
print(my_md5('123456test')) #不加盐使用
print(my_md5('123456test','666')) #加盐使用

#sha1\sha224\sha256加密
# m = my_md5('123456')
# print(m)
# print(m)
# print(m)
# print( hashlib.sha1(m.encode()))
# print(hashlib.sha224(m.encode()))
# print(hashlib.sha256(m.encode()))

# import hashlib
# md5 = hashlib.md5()
# md5.update('123456test'.encode())
# print(md5.hexdigest())  #输出16进制格式的hash值
# print(md5.digest())  #输出2进制格式的hash值
#
# #上面也可以写成
# import  hashlib
# res = hashlib.md5('123456'.encode())
# res.update('test'.encode()) #如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
# print(res.hexdigest())
# print(res.digest())
#
# #最简便的写法是：
# import hashlib
# res = hashlib.md5('123456test'.encode())
# print(res.hexdigest())
# print(res.digest())
#
#
# import hashlib
# res = hashlib.sha1('123456test'.encode())
# print(res.hexdigest())
# print(res.digest())
#
# #也可以分开多次追加
# import hashlib
# sha_1 = hashlib.sha1()
# sha_1.update('123456'.encode())
# sha_1.update('test'.encode())
# print(sha_1.hexdigest())
# print(sha_1.digest())