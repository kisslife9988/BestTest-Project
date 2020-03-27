s = 'abcdef'
users = ['username','username2','username3']
str_users = str(users)
print(str_users[1])
#join方法 用于将序列中的元素以指定的字符连接生成一个新的字符串
res = ','.join(users)  #以某种格式连接list、str、元组当中的元素值，生成一个字符串
print(users)
#zfill方法自动补0,返回指定长度的字符串，原字符串右对齐，前面填充0
list = list(range(1,10))
print(list)
list1 = []
for i in list:
    new_l = str(i)
    list1.append(new_l.zfill(4))
print(list1)
#find 方法,找寻下标的方法(检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。)
print(s.find('a'))
print(s.index('a'))
print(s.find('g')) #内容下标不存在展示为-1
# print(s.index('g')) #内容下标不存在则会报错
#isdigit  检测字符串是否只由数字组成。
print('123'.isdigit())
print('12.3'.isdigit())

#islower 检测字符串是否由小写字母组成；isupper  判断是否都是大写字母
print('abc'.islower())
print('AB'.upper())

#isalnum  检测字符串是否由字母和数字组成
print('abcd123'.isalnum())
#isalpha 检测字符串是否只由字母组成
print('abc123'.isalpha())
print('abddDC'.isalpha())
#isspace 检测字符串是否只由空格组成
print('   '.isspace())
print('  sd'.isspace())
#isidentifier  判断是否是一个合法的变量名
print('ab'.isidentifier())
#splitlines  按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
str1 = 'ab c\n\nde fg\rkl\r\n'
print (str1.splitlines())
str2 = 'ab c\n\nde fg\rkl\r\n'
print(str2.splitlines(True))
print('===========string===========')
import string
print(string.ascii_lowercase)  #所有的小写字母
print(string.ascii_uppercase)  #所有的大写字母
print(string.digits) #0-9整数
print(string.punctuation)  #特殊字符
print(string.ascii_letters) #所有的大小字母
