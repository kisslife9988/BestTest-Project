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
# all_user = {}
# res = open('test.txt').read()
# username = input('username:')
# pwd = input('pwd:')
# user_info = username + ',' + pwd
# if user_info in res:
#     print('登录成功')
# else:
#     print('登录失败！')

# for r in res.split('\n'):
#     if r.strip() != '':
#         username = r.split(',')[0]
#         pwd = r.split(',')[1]
#         all_user[username] = pwd
# for i in range(3):
#     username = input('username:')
#     pwd = input("pwd:")
#     if username in all_user:
#         if pwd == all_user.get(username):
#             print('欢迎登录')
#             break
#         else:
#             print('账号、密码错误！')
#     else:
#         print('该用户未注册！')
'''
    例子6：监控日志
        1、从日志里面找到，1分钟之内超过20次访问的IP
        2、脚本没分钟运行一次
    思路：
        1、读取文件内容，获取IP地址
        2、把每个IP地址存起来,使用字典存储（避免重复）
        3、判断IP访问的次数是否超过20次
        4、加入黑名单
        
'''
# import time
# point = 0
# while True:
#     ips = {}
#     f = open(r'C:\Users\Administrator\Desktop\access.log',encoding='utf-8')
#     f.seek(point)
#     for line in f :
#         ip = line.split()[0]
#         if ip in ips:
#             ips[ip] += 1
#         else:
#             ips[ip] = 1
#     point = f.tell()   #记录文件指针的位置
#     for ip,count in ips.items():
#         if count >=20:
#             print('%s  加入黑名单！'%ip)
#     f.close()
#     time.sleep(60)

'''
    例子7：购买程序
    1、实现一个商品管理的程序
        #输入1，添加商品；2、删除商品；3、查看所有商品
        添加商品：
            输入商品的名称：XX  商品存在提升已经存在
            商品的价格：XXX  数量只能大于0的整数
            商品的数量：XXX  数量只能为大于0的整数
        删除商品：
            输入商品名称：
                iPhone  删除商品；如果输入的商品名称不存在，要提升不存在
        查询商品：
            输入商品名称：
                iPhone  把对应的信息打印出出来；如果输入的商品名称不存在，要提升不存在
                all：打印出所有的商品信息
'''
# FILENAME = 'products.json' #如果变量名全是大写字母表示该变量是一个常量
# import json
# def get_file_content():
#     with open(FILENAME,encoding='utf-8') as f:
#         content = f.read()
#         if len(content) > 0:
#             res = json.loads(content)
#         else:
#             res = {}
#     return res
# def write_fiel_content(dic):
#     with open(FILENAME,'w',encoding='utf-8') as fw:
#         json.dump(dic,fw,indent=4,ensure_ascii=False)
# def check_digit(cs:str):
#     if cs.isdigit():
#         cs = int(cs)
#         if cs > 0:
#             return cs
#         else:
#             return 0
#     else:
#         print('商品数量必须是整数!')
#         return 0
# def add_product():
#     product_name = input('请输入商品名称：').strip()
#     count = input('请输入商品数量：').strip()
#     price = input('请输入商品价格：').strip()
#     all_products = get_file_content()
#     if check_digit(count) == 0:
#         print('数量输入不合法！')
#     elif check_digit(price) == 0:
#         print('价格输入不合法')
#     elif product_name in all_products:
#         print('商品已存在！')
#     else:
#         all_products[product_name] = {"count":int(count),"price":int(price)}
#         write_fiel_content(all_products)
#         print('添加成功！')
# def show_product():
#     product_name = input('请输入查询商品名称：').strip()
#     all_products = get_file_content()
#     if product_name == 'all':
#         print(all_products)
#     elif product_name not in all_products:
#         print('商品不存在！')
#     else:
#         print(all_products.get(product_name))
# def del_product():
#     product_name = input('请输入商品名称：').strip()
#     all_products = get_file_content()
#     if product_name in all_products:
#         all_products.pop(product_name)
#         print('删除成功！')
#         write_fiel_content(all_products)
#     else:
#         print('商品不存在！')
#
# choice = input('操纵权限：\n 1、添加商品 2、删除商品 3、查看商品信息\n 您的选择是：')
# if choice == '1':
#     add_product()
# elif choice == '2':
#     del_product()
# elif choice == '3':
#     show_product()
# else:
#     print('输入错误，请重新输入！')

'''
    校验小数类型
    正小数：
    1、小数点个数为1
    2、小数点左边和右边都是整数
    负小数：
    1、小数点个数为1
    2、小数点左边和右边都是整数
    3、负号开头，并且只有一个负号
'''
# def check_float(s):
#     '''
#     这个函数的作用就是判断传入的字符串是否是合法的小数
#     :param s: 传入一个字符串
#     :return: True/False
#     '''
#     s = str(s)
#     print(s)
#     if s.count('.') == 1:
#         s_split = s.split('.')
#         # left = s_split[0]
#         # right = s_split[1]
#         left,right = s_split
#         if left.isdigit() and right.isdigit():
#             return True
#         elif left.startswith('-') and left[1:].isdigit() and right.isdigit():
#             print(left[1:])
#             return  True
#     return False
# print(check_float(---2.3))
# print(check_float(2.3))
# print(check_float(-3.45))
# print(check_float('a.2'))
# print(check_float('1.22'))
# print(check_float('---2.3'))

'''
    随机生成密码并写入文件
        def gen_password(num):
            #num 代表生成密码的条数
            pass
        2、密码复杂度
            长度在8-16之间
            密码必须包括大写字母、小写字母、数字、特殊字符
                思路1：
                1、分别从大写字母、小写字母、数字、特殊字符各取一个
                2、在从所以的字符里面取8-4个，和第一步获取到的结果拼接起来
                思路2：
                1、将所有的大写字母、小写字母、数字、特殊字符拼接起来
                2、随机取8位，判断里面是否都包括大写字母、小写字母、数字、特殊字符
                3、如果包含的话，存起来，不符合的话重新在活区一个
            密码不能重复
        3、生成的密码保存到文件中
    生成一批双色球号码
        def gen_seq(num):
            pass
        1、中奖号码由6个红色球号码和1个蓝色球号码组成
        2、红球范围：1-33
        3、篮球范围：1-16
        4、产生的不能重复
'''
# import random,string
# def get_passwords1():
#         pwd_len = random.randint(8,16)
#         upper = random.sample(string.ascii_uppercase,1)
#         lower = random.sample(string.ascii_lowercase,1)
#         digit = random.sample(string.digits,1)
#         punctuation = random.sample(string.punctuation,1)
#         other = random.sample(string.ascii_letters+string.digits+string.punctuation,pwd_len-4)
#         res = upper + lower + digit + punctuation + other
#         random.shuffle(res)
#         res = ''.join(res)
#         return ''.join(res)
# def get_password2():
#     pwd_len = random.randint(8, 16)
#     all_str = string.ascii_letters + string.digits + string.punctuation
#     res = set(random.sample(all_str,pwd_len))
#     if res & set(string.ascii_uppercase) and res & set(string.ascii_lowercase) and res & set(string.digits)\
#         and set(string.punctuation):
#         return ''.join(res)
#     return get_password2()
# def write_file(pw):
#     with open('password.txt','w',encoding='utf-8') as fw:
#         fw.writelines(pw)
# # all_passwords = set()
# all_passwords = []
# num = int(input('请输入要产生密码的条数：').strip())
# while len(all_passwords) != num:
#     res = get_password2() + '\n'
#     all_passwords.append(res)
#     write_file(all_passwords)

#作业2
# import random
# def gen_seq():
#     all_red_ball = [str(i).zfill(2) for i in range(1,34)]
#     all_blue_ball =  [str(i).zfill(2) for i in range(1,17)]
#     blue = random.choice(all_blue_ball)
#     red = random.sample(all_red_ball,6)
#     red = ' '.join(red)
#     return '红球：%s  篮球:%s'%(red,blue)
# def write_file(pw):
#     with open('shuangseqiu.txt','w',encoding='utf-8') as fw:
#         fw.writelines(pw)
# all_seq = set()
# num = int(input('请输入次数：').strip())
# while len(all_seq) != num:
#     res = gen_seq() + '\n'
#     all_seq.add(res)
#     write_file(all_seq)


'''
    查看文件路径
'''
# def find_file(path,keyword):
#     '''查找文件路径'''
#     res = os.walk(path)
#     for cur_path,dirs,files in res:
#         for file_name in files:
#             if keyword in file_name:
#                 print('该文件在%s目录下'%cur_path)
# find_file('G:\\','fullstack')

'''
 
'''



