import smtplib

server = smtplib.SMTP()
server.connect(host, port)
server.login(username, password) 
server.sendmail(from_addr, to_addr, msg.as_string()) 
server.quit() 


qq邮箱
# smtplib 用于邮件的发信动作
import smtplib

# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = 'xxx@qq.com'
password = '你的授权码数字'

# 收信方邮箱
to_addr = 'xxx@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.starttls()
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()


email

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
