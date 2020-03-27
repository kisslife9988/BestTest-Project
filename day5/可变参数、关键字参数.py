#位置参数
# def fun(x,y=6):  #x,y就是位置参数
#     print(x+y)
# fun(3)  #调用这个函数
# fun(y=0,x=6)


def my(name,sex='女'):
    '''

    :param name: 必填参数、位置参数
    :param sex: 默认值参数
    可变参数：
    关键字参数：
    :return:
    '''
    pass
#可变参数，在变量名前边加入*号（变量名可以随便起，一般都叫args），其特点
#1、不限制传参的个数
#2、元素都放入一个元组中
#3、不是必传的
#4、它用在传参比较多的情况下

def send_sms(*phone_num):
    # for p in phone_num:
        print(phone_num)
        # print('发报警短信',p)
send_sms()
send_sms(13199998888)
send_sms(13899992222,13499989234)

'========================================'
#关键字参数，在变量前边加入两个*号（变量名可以随便起，一般都叫kwargs），其特点：
# 1、不限制传参的个数
# 2、不是必传的
# 3、元素都放在一个字典中
# 4、它用在传参比较多的情况下
def send_sms(**phone_num):
    print('详细信息：',phone_num)
send_sms()
send_sms(name='test',sex='20')
send_sms(addr = '北京市',country = '中国',c = 'abc',f = 'kkk')

'========================================='
def my(name,county='china',*args,**kwargs):
    '''
    如果定义的函数如上边这样那么：
        1、先写位置参数，其次是默认值参数，然后是可变参数，最后是关键字参数，的顺序来写；
    '''
    print(name)
    print(county)
    print(args)
    print(kwargs)
# my('gaobo','japan','beijing','天通苑',color = '红色',age = 19)
my('gyb','beijing','天通苑',color = '红色',age = 19)

# def my(name,county='china',*args):   #可变参数、默认值参数、位置参数同时使用，可变参数必须在位置参数的后边，否则会报错
#     print(name)
#     print(county)
#     print(args)
# my('gyb','beijing','天通苑','海淀区')


