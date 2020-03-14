'''
例子1：
  输入一个分数  大于等于90  优秀
  小于90 大于等于80 良好
  大于等于60 小于 80  及格
  小于60，不及格
'''
# score = int(input('Please input you score:'))
# if score >= 90:
#     print('优秀')
# elif score >= 80 and score < 90:
#     print('良好')
# elif score >=60 and score < 80:
#     print('及格')
# else:
#     print('不及格')
'''
例子2：
    猜数字游戏：数字为100，1、总共有7次机会；2、输入小了 ，提升用户输入小了；3、输入大了，提示用户输入大了
'''
# import random
# num = random.randint(1,100)
# count = 0
# while count < 7:
#     count += 1
#     guess = int(input('Please input you guess res:'))
#     if guess == num:
#         print('恭喜你猜对了！')
#         break
#     elif guess < num:
#         print('猜小了！再试试！')
#         continue
#     else:
#         print('猜大了，在试试！')
#         continue
# else:
#     print('输入错误次数过多，game over！')
# # 使用for循环来实现
# import random
# num = random.randint(1,100)
# print(num)
# for i in range(7):
#     guess = int(input('Please input you guess res:'))
#     if guess == num:
#         print('恭喜你猜对了！')
#         break
#     elif guess < num:
#         print('猜小了！再试试！')
#         continue
#     else:
#         print('猜大了，在试试！')
#         continue
# else:
#     print('输入错误次数过多，game over！')
'''
例子3：
    登录程序
        username = wyh
        passwd = 123456
    要求：
        1、输入账号密码，输入正确就登录成功
            提示“欢迎XXX登录，今天的日期是：XX”
        2、最多输入三次密码
            提示“账号/密码错误，请重新登录！”
        3、校验超过3次，提示“失败次数过多，退出！”
        4、校验输入是否为空，如果输入为空，提示“账号/密码不能为空！”
            什么都不输入/输入一个或多个空格都算为空
            输入为空也计入验证次数
'''
# import datetime
# today = datetime.date.today()
# username = 'wyh'
# passwd = '123456'
# for i in range(3):
#     username_new = input('请输入您的账号：')
#     password = input('请输入您的密码：')
#     if username_new.strip() == '' or password.strip() == '':
#         print('账号/密码不能为空，请重新输入！')
#     elif username_new == username and password == passwd:
#         print('欢迎%s登录，今天的日期是：%s'%(username_new,today))
#         break
#     else:
#         print('输入的账号/密码错误，请重新输入！')
# else:
#     print('失败次数过多，退出！')

# #使用while循环实现
# count = 0
# while count < 3:
#     username_new = input('请输入您的账号：')
#     password = input('请输入您的密码：')
#     count += 1
#     if username_new.strip() == '' or password.strip() == '':
#         print('账号/密码不能为空，请重新输入！')
#     elif username_new == username and password == passwd:
#         print('欢迎%s登录，今天的日期是：%s' % (username_new, today))
#         break
#     else:
#         print('输入的账号/密码错误，请重新输入！')
# else:
#     print('失败次数过多，退出！')

'''
    例子4：校验手机号的小程序
'''
# user = ['test01','test02']
# for i in range(3):
#     username = input('请输入用户名：')
#     # if user.count(username) >0 :
#     if username in user:  #in就是判断在不在里面，not in 就是判断不包含在里面
#         print("用户已注册")
#     else:
#         print("用户未注册")
#         user.append(username)
# print(user)
'''
    例子5：
    一：实现注册功能
        1、输入username、passwork、cpassword
        2、3个值都不能为空，且错误次数为3次
        3、用户名长度最少6位，最长20位，用户名不能重复
        4、密码长度最少8位，最长15位；密码输入要一致
        5、注册成功后，要写到文件中，格式：用户名，密码
    二：登录功能实现
        1、用户名和密码去文件里面读取登录
        2、3次登录
'''
# f = open('test.txt','a+')
# f.seek(0)
# res = f.read()
# all_user_name = []
# for r in res.split('\n'):
#     username = r.split(',')[0]
#     all_user_name.append(username)
# print(all_user_name)
# print(len(all_user_name))
# for i in range(3):
#     username = input('username:').strip()
#     pwd = input('pwd:').strip()
#     cpwd = input('cpwd:').strip()
#     if len(username) < 6 or len(username) > 20:
#         print('用户名不合法！')
#     elif len(pwd) < 8 or len(pwd) > 20:
#         print('密码不合法')
#     elif pwd != cpwd:
#         print('两次密码不一致！')
#     elif username in all_user_name:
#         print("用户名已经被注册！")
#     else:
#         user_info = '%s,%s\n'%(username,pwd)
#         f.write(user_info)
#         print('注册成功！')
#         break
# else:
#     print('错误次数过程。')
# f.close()
#登录
all_user = {}
res = open('test.txt').read()
# username = input('username:')
# pwd = input('pwd:')
# user_info = username + ',' + pwd
# if user_info in res:
#     print('登录成功')
# else:
#     print('登录失败！')

for r in res.split('\n'):
    if r.strip() != '':
        username = r.split(',')[0]
        pwd = r.split(',')[1]
        all_user[username] = pwd
for i in range(3):
    username = input('username:')
    pwd = input("pwd:")
    if username in all_user:
        if pwd == all_user.get(username):
            print('欢迎登录')
            break
        else:
            print('账号、密码错误！')
    else:
        print('该用户未注册！')