#字符串常用的方法
password = ' 123456 \n 456789'
# print(password)
print(password.strip())#默认去掉字符串两边的空格和换行符,如过传入了值，则可以删除指定的内容；修改的内容不会直接修改这个变量值
print(password.lstrip()) #去掉左边的空格和换行符
print(password.rstrip()) #去掉有变动的
password =  'jpg 12323 .jpg ABD'
print(password.strip('.jpg'))
print(password.upper())  #将小写字母变为大写字母
print(password.lower())  #将大写字母变为小写字母
print(password.capitalize()) #将首字母大写
print(password.count('jpg')) #统计次数
print(password.replace('12323','wyh')) #字符串的替换，如果替换的值不存在则没有任何变化，也不会报错
print(password.replace('sdkf','9999'))
filename = 'a.mp3'
print(filename.endswith('.mp3')) #判断是否以.MP3结尾
print(filename.endswith('.jpg'))
print(filename.startswith('a')) #判断是以**开头
print('{name},{age}'.format(name='wyh',age = 19)) #字符串格式化方法
#split方法：1、把字符创变成了list；2、以某个字符串分割，分割之后的是list里面的每个元素，默认是以空格进行分割
names = 'wyh,test,gaobo'
print(names.split(',')) #以逗号分隔生成一个list