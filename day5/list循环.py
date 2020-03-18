#循环尽量不要删除list中的元素，因为会导致下标错位，结果显示的不正确；如果非要删除list中元素则配置两个想听的list 删除第二个list即可
#知识点1:深拷贝和浅拷贝
# l = [1,2,3,1,4,5,2]
# import copy
# # l2 = l.copy()
# l2 = copy.copy(l)
# print(id(l))
# print(id(l2))
# # # l2 = [1,2,3,1,4,5,2]
# # print(id(l))
# # # l2 = l #浅拷贝，新的数据的内存地址是一样的
# # l2 = l.copy()  #浅拷贝，复制一份list
# # print(id(l2))
# # print(id(l))
# for i in l:
#     print(i)
#     if i % 2 != 0:
#         l2.remove(i)
# print(l,l2)
# print(l.index(1))
# print(len(l))

#深拷贝的定义方式；会重新定义变量，变量的内存地址是不同的
import copy
# l = [1,2,3,1,4,5,2]
# l2 = copy.deepcopy(l)
# print(id(l))
# print(id(l2))
#深拷贝和浅拷贝的区别是深拷贝会改变变量的内存地址
'''================================================='''
#直接赋值：
# a = [1,2,['test1','test2']]
# b = a
# print(id(a))  #查看存储空间的id
# print(id(b)) #查看存储空间的id
# print('第一次的值：',a)
# print('第一次的值：',b)
# a.append('4')
# print('第二次的值：',a)
# print('第二次的值：',b)

#浅拷贝
# a = [1,2,['test1','test2']]
# b = a.copy()
# b = copy.copy(a)
#
# print('a的ID值：',id(a))
# print('b的ID值：',id(b))
# print('第一次的值a：',a)
# print('第一次的值b：',b)
# print('a所有元素的下标值：',[id(ele) for ele in a])
# print('b所有元素的下标值：',[id(ele) for ele in b])
# a[0]=3
# a[2].append('test3')
# print('第二次的值a：',a)
# print('第二次的值b：',b)
# print('a所有元素的下标值：',[id(ele) for ele in a])
# print('b所有元素的下标值：',[id(ele) for ele in b])

#深拷贝
a = [1,2,['test1','test2']]
b = copy.deepcopy(a)

print('a的ID值：',id(a))
print('b的ID值：',id(b))
print('第一次的值a：',a)
print('第一次的值b：',b)
print('a所有元素的下标值：',[id(ele) for ele in a])
print('b所有元素的下标值：',[id(ele) for ele in b])
a[2].append('test3')
print('第二次的值a：',a)
print('第二次的值b：',b)
print('a所有元素的下标值：',[id(ele) for ele in a])
print('b所有元素的下标值：',[id(ele) for ele in b])