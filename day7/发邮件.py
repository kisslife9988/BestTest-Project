# import yagmail  #导入第三方模块
# user = '582238977@qq.com'  #邮箱的用户名
# password = 'ahzzysbqaqurbfea'  #邮箱的密码
# #登录邮箱
# m = yagmail.SMTP(host='smtp.qq.com',user=user,password=password,smtp_ssl=True) #如果是QQ邮箱需要加入参数smtp_ssl=True，如果是其它邮箱则不用加入该参数
# #发送邮件内容
# m.send(to='836480052@qq.com',cc='1159814932@qq.com',subject='明天不上课',contents='这是一个测试邮件信息！',attachments='发邮件.py')
# '''
# to:目标人 ，如果想发送多个，那么直接写一个list列表即可实现
# cc：抄送人
# subject：主题
# contents：内容
# attachments：附件
# '''
#使用Python源安装的yagmail文件附件如果是中文的话则会显示乱码；

# 使用Python自带的模块发送邮件

import email.mime.multipart
import email.mime.text
import smtplib
#
msg = email.mime.multipart.MIMEMultipart()  #创建消息对象
msg['from'] = '582238977@qq.com'  #指定发件人，即邮件头展示的内容
msg['to'] =  '836480052@qq.com'    #指定收件人，即邮件尾展示的内容
msg['subject'] = '这是一个测试邮件！'  #写明邮件主题

context = '''        
    <h1>老师好</h1>
    你好，
     这是一封自动发送的邮件。
      www.ustchacker.com hello
    '''          #定义邮件内容

text = email.mime.text.MIMEText(_text=context, _subtype="html") #_text代表邮件内容，_subtype代表邮件内容的发送形式
msg.attach(text)

em = smtplib.SMTP_SSL()
em.connect("smtp.qq.com", 465)
em.login("582238977@qq.com", 'ahzzysbqaqurbfea')
em.sendmail(from_addr='582238977@qq.com', to_addrs='836480052@qq.com', msg=msg.as_string())
em.quit()