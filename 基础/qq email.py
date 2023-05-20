import smtplib
from email.mime.text import MIMEText
from_addr="1793420386@qq.com"
password=input()
to_addrs=['1793420386@qq.com','2483935422@qq.com','1239161461@qq.com']
smtp_server='smtp.qq.com'
from email.header import Header
msg=MIMEText("print(b'\xc4\xe3\xca\xc7\xd2\xbb\xd6\xbb\xd6\xed'.decode('gbk'))",'plain','utf-8')
msg['From']=Header('密集')
msg['To']=Header(','.join(to_addrs))
msg['subject']=Header('python text')
server=smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr,password)
server.sendmail(from_addr,to_addrs,msg.as_string())
server.quit()


import csv
data = [['wufeng ', 'wufeng@qq.com'],['kaxi', 'kaxi@qq.com']]
with open ('to_addrs.csv','w',newline='') as f:
    writer=csv.writer(f)
    for i in data:
        writer.writerow(i)
with open ('to_addrs.csv','r')as f:
    reader=csv.reader(f)
    for i in reader:
        to_addrs=i[1]
        print(to_addrs)