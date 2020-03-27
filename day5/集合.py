'''
    集合
        1、使用set进行定义,使用大括号进行表示
        2、天生可以去重
        3、集合是无序的，不能根据下标取值并且不能进行排序
'''
# l = [1,1,2,3,2,4,3,6]
# r =[]
# for i in l:
#     if i in r:
#         continue
#     else:
#         r.append(i)
# print(r)
# res = set(l)
# l = list(res)
# print(l)
# JH = set()  #定义一个空的集合
xingneng = ['wyh','gaobo','test']
zdh = ['wyh','test1','test2','gaobo']
xingneng = set(xingneng)
zdh = set(zdh)
res = xingneng.intersection(zdh) #取两个结合的交集
res1 = xingneng & zdh  #取交集
print(res,res1)

#取并集
res = xingneng.union(zdh)
res1 = xingneng | zdh
print(res,res1)
#差集,
res = xingneng.difference(zdh)  #在xingnengl里有在zdh中没有的
res1 = xingneng - zdh
print(res,res1)
#对称差集，即除去交集元素后的所有元素
a = ['1','2','3','4']
b = ['3','4','5','6']
a = set(a)
b = set(b)
res =a.symmetric_difference(b)
res1 = a^b
print(res,res1)

a = {1,2,3,4,5}
b = {1,2,4}
print(a.issubset(b)) #判断a是否是b的子集
print(b.issubset(a))
print(a.issuperset(b)) #判断a是否是b的父集
print(b.issuperset(a))
print(a.isdisjoint(b)) #判断a、b是否有交集，有交集返回false  没有交集返回true

#添加元素
a = {1,2,3}
a.add(4)
a.remove(3)#删除指定的元素
a.pop()  #随机删除一个
print(a)
