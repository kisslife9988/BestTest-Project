import xlwt   #写Excel
import xlrd  # 读Excel
import xlutils  #修改Excel

# #写Excel
# book = xlwt.Workbook()
# sheet = book.add_sheet('sheet_test')
# sheet.write(0,0,'id') #指定行和列的内容
# sheet.write(0,1,'username')
# sheet.write(0,2,'passwd')
#
# sheet.write(1,0,'1')
# sheet.write(1,1,'test')
# sheet.write(1,2,'123456')
# stus = [[1,'test2','123456'],[2,'test2','123456'],[3,'test3','123456']]
# line = 0 #控制行数
# for stu in stus:
#     col = 0
#     for s in stu:
#         sheet.write(line,col,s)
#         col += 1
#     line += 1
# book.save('stu.xls') #结尾只能用xls，因为如果用.xlsx的话用微软的软件打不开，WPS才能打开
#方法二：
# stus = [[1,'test2','123456'],[2,'test2','123456'],[3,'test3','123456']]
# for line,stu in enumerate(stus):
#     for col,s in enumerate(stu):
#         sheet.write(line,col,s)
# book.save('stu.xls') #结尾只能用xls，因为如果用.xlsx的话用微软的软件打不开，WPS才能打开
print('=========读Excel=========')
# book = xlrd.open_workbook('stu.xls')
# sheet = book.sheet_by_index(0)
# # sheet = book.sheet_by_name('sheet_test')
# print(sheet.nrows)#获取Excel中的行数
# print(sheet.ncols)#获取Excel中的列数
# print(sheet.cell(0,0).value) #获取指定单元格的内容
# print(sheet.cell(0,1).value) #获取指定单元格的内容
# print(sheet.row_values(0)) #获取整行的内容
# print(sheet.col_values(0)) #获取整列的内容
#
# #循环获取每行的内容
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

print('========修改Excel========')
# 修改模块得和xlrd模块一起配合使用
#修改文件，先用用xlrd打开一个Excel，然后用xlutils模块中的copy功能，复制一个Excel  这样才能修改
from xlutils import copy
book = xlrd.open_workbook('stu.xls')
new_book = copy.copy(book)
sheet = new_book.get_sheet(1) #通过下标获取要操作的sheet页
sheet.write(0,1,'wyh')
sheet.write(1,2,'wyh1')
new_book.save('stu.xls')

# # 方法二
# #enumerate 方法自动计算循环的下标，循环使用的时候，先取下标在取值
# import string
# case = list(string.ascii_uppercase)
# for index,c in enumerate(case,1): #()中的1代表下标的步长
#     print("%s =》%s"%(c,index))



import xlwt #导入操作Excel的写模块
# 基本的写入操作
# book = xlwt.Workbook() #创建一个Excel表格
# sheet = book.add_sheet('test_sheet1',cell_overwrite_ok=True) #给Excel表中添加一个sheet页
# sheet.write(0,0,'id')  #向sheet表中写入数据，第一个参数代表的行数，第二个参数代表的列数，第三个参数代表写入的内容
# sheet.write(0,1,'name')
# sheet.write(1,0,1)
# sheet.write(1,1,'哈哈')
# sheet.write(1,1,'测试哈哈')
# book.save('test.xls') #报存文件，结尾只能用xls，因为如果用.xlsx的话用微软的软件打不开，WPS才能打开
#如果存在很多数据的时候，用基本写入是不现实的，这个时候我们可以使用循环进行操作

# #循环方式一：
# stus = [[1,'test2','123456'],[2,'test2','123456'],[3,'test3','123456']]
# book = xlwt.Workbook() #创建一个Excel表格
# sheet = book.add_sheet('test_sheet1') #给Excel表中添加一个sheet页
# line = 0 #控制写入的行数
# for stu in stus:
#     col = 0  #控制写入的列数
#     for s in stu:
#         sheet.write(line,col,s)
#         col += 1
#     line += 1
# book.save('stu.xls')
#
# # 循环方式二：
# # enumerate 方法自动计算循环的下标，循环使用的时候，先取下标在取值
# stus = [[1,'test2','123456'],[2,'test2','123456'],[3,'test3','123456']]
# book = xlwt.Workbook() #创建一个Excel表格
# sheet = book.add_sheet('test_sheet1') #给Excel表中添加一个sheet页
# for line,stu in enumerate(stus):
#     for col,s in enumerate(stu):
#         sheet.write(line,col,s)
# book.save('stu.xls')

# import xlrd
# book = xlrd.open_workbook('stu.xls')  #打开Excel文件，可以制定绝对路径的文件
# # sheet = book.sheet_by_name('Sheet1')  #通过sheet表的名称来读取要操作的表
# sheet = book.sheet_by_index(1)  #通过Excel表中sheet也得下标确定要读取的表，下标从左往右依次为：0,1,2……
# rows = sheet.nrows  #获取表中所有的行数
# cols = sheet.ncols  #获取表中所有的列数
# print('表中的总行数是：%s'%(rows))
# print('表中的总列数是：%s'%(cols))
# print(sheet.cell(0,0).value) #获取指定单元格的内容
# print(sheet.cell_value(0,0)) #获取指定单元格的内容
#
# print(sheet.cell(0,1).value) #获取指定单元格的内容
# print(sheet.cell_value(0,1)) #获取指定单元格的内容
#
# print(sheet.row_values(0)) #获取整行的内容,以列表格式显示
# print(sheet.col_values(0)) #获取整列的内容，以列表格式显示
# #循环打印每一行的数据
# for i in range(rows):
#     print(sheet.row_values(i))
# #循环打印每一列的值：
# for i in range(cols):
#     print(sheet.col_values(i))
# #循环读取每一个元素的值
# for i in range(rows):
#     for j in range(cols):
#         print('第%s行第%s列的值是：%s'%(i,j,sheet.cell_value(i,j)))
# #其它方法：
# import xlrd
# book = xlrd.open_workbook('stu.xls')  #打开Excel文件，可以制定绝对路径的文件
# sheet = book.sheet_names()[1] #该函数是用来获取sheet页的表名称的，这个代表获取Excel表中下标是1的表名称值
# print(sheet)
# sheet = book.sheet_loaded('Sheet1')  #判断表是否存在，存在返回true 不存在报错
# print(sheet)













