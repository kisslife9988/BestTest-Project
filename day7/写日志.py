'''
日志的级别常见的：
    error
    waning
    info
    debug
'''
import logging
import nnlog
log = nnlog.Logger('my.log',level='info',backCount=3,when='S')
#参数说明：
#指定生成的文件名称 必传
#level：默认debug级别，也可以指定其它级别
#backCount：保留日志的数量，backCountry=5 则日志最多保存3个文件，默认5
#when：按每小时、每分钟、每周产生日志，默认是D（天）
#
log.info('test 登录……')
log.error('登录失败！')
log.surprise()
print(dir(log))