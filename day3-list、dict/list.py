#list的定义使用中括号来定义，每个元素使用逗号隔开；list中取值都是从0开始的。每个元素对应有唯一的下标值或者叫索引、角标
# 为什么重复添加相同的值不会写入list？
# 答：程序都是和内存打交道的，每次运行程序都会把内存中的缓存清理后重新加入
stu_name = ['test1','test2','test3']
print(stu_name[1])
#增加元素
stu_name.append('test4')   #append方法，将元素添加到list中末尾
stu_name.insert(0,'test00')    #在指定的下标位置添加元素，每次只能增加一个元素，如果需要添加多个则需要多个insert语句
stu_name.insert(0,'test00')
stu_name.insert(0,'test01')
# print(stu_name)
#修改元素
stu_name[1] = 'test01'   #找到要修改的元素下标，直接重新复制即可
print(stu_name)
#删除元素
stu_name.pop() #不写删除的下标则删除list中末尾的元素
print(stu_name)
stu_name.pop(4) #删除指定下标的元素
print(stu_name)
# stu_name.pop(9) #删除下标不存在的元素则会报错：IndexError: pop index out of range
# print(stu_name)

stu_name.remove('test01') #删除指定的元素，直接传入元素的值；如果有相同的元素值，只删除第一个匹配的值
print(stu_name)

del stu_name[-1]  #删除最后一个值，如果下标值是整数从list前边开始取值（0-N），如果是下标是负数则从后边开始取值，下标值从-1开始（-1到N）
print(stu_name)
# del stu_name  #删除stu_name变量
# print(stu_name)

#查询
#1、指定下标取值
list1 = ['test1','test2','test3','test4','test1','test5']
print(list1[-1])
print(list1[0])
print(list1.count('test1')) #查询某个元素在list中出现的个数
print(list1.index('test4')) #查询元素的下标值
# print(list1.index('wyh')) #不存在的元素则会报错，ValueError: 'wyh' is not in list
print(list1.reverse()) #将list中的元素进行翻转，它是没有返回值的，直接打印为：none
print(list1)
list1.sort() #对list中的元素进行正序排序，如果想降序排序可以先进行正序排序然后在翻转即可
print(list1)
list1.sort(reverse=True) #如果指定了reverse=True，则就是降序排序
print(list1)
list1.extend(stu_name) #把一个list中的元素值加入到另外一个list中，两个list合并也可以使用+号，来正常进行合并
print(list1)
list2 = [2,3,5]
list3 = ['wyh','set']
print(list2+list3) #合并两个list
print(list2*3) #复制list2的值三次然后生成一个新的list
list1.clear() #清空list中的所有元素值
print(list1)

#list的嵌套使用
#多维数组，多维数组的取值，按照list的下标逐层去取值，取到二维list的时候在按照list正常取值就可以了
num1 = [1,2,3] #一维数组
num2 = [1,2,3,[2,3,4]] #二维数组
print(num2[3][2])
num3 = [1,2,[3,4,[5,6]]]#三维数组
print(num3[2][2][1])

#list的循环
list_num = [1,2,3,4,5]
# count = 0
# while count < len(list_num):
#     print(list_num[count])
#     count += 1
for i in range(len(list_num)):
    print(list_num[i])
for i in list_num:
    print(i)
print('#########################')
for index,ip in enumerate(list_num):  #使用枚举函数，它会帮你计算下标和元素
    print(index,ip)
    list_num[index] = 'wyh'+str(ip)
print(list_num)
print('**********切片操作*************')
#list切片操作
#格式：list[首数值:尾数值]
#切片取值，是顾头不顾尾的；即取值最后一个值是不会取的
L = list(range(1,10))
print(L)
#取出1-4的值
print(L[0:4]) #去小标为0-3的值
print(L[:4]) #从首个下标开始取值，取到下标为3的位置
print(L[2:]) #取从下标为2开始往后的所有值
print(L[:]) #取list中的所有的值
print(L[::2]) #根据步长每隔2个值取一次值
print(L[1::2]) #取偶数
print(L[::2]) #取奇数，如果步长是整数，那么从左往右开始取值
print(L[::-2]) #取奇数，如果后边的步长是负数，那么从右往左开始取值
print(L[-3:-1])
words = '字符串切片操作！'
print(words[1:3])
print(words[::-1])
for index,w in enumerate(words):
    print(index,w)
for w in range(len(words)):
    print(words[w])
s = '上海自来水来自海上'  #回文算法，即正读和反读都是一样的语句
for i in range(3):
    s = input('请输入一个字符串：')
    if s == s[::-1]:
        print('是回文语句')
    else:
        print('不是回文语句')
