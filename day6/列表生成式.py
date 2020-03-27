#列表生成式
#先写一个循环，然后将循环体重要操作的内容放入循环前边，如下实例
res = []
for i in range(1,34):
    res.append(str(i).zfill(2))
print(res)
#上面的循环也可以按下面的方式写入
res =[str(i).zfill(2) for i in range(1,34)]
print(res)