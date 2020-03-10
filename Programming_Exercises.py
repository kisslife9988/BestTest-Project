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
import datetime
today = datetime.date.today()
username = 'wyh'
passwd = '123456'
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

#使用while循环实现
count = 0
while count < 3:
    username_new = input('请输入您的账号：')
    password = input('请输入您的密码：')
    count += 1
    if username_new.strip() == '' or password.strip() == '':
        print('账号/密码不能为空，请重新输入！')
    elif username_new == username and password == passwd:
        print('欢迎%s登录，今天的日期是：%s' % (username_new, today))
        break
    else:
        print('输入的账号/密码错误，请重新输入！')
else:
    print('失败次数过多，退出！')