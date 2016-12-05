#! /usr/bin/env python
#coding=utf-8
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import poplib
import smtplib
#邮件发送函数
#limeng@space-time.site


#email.txt
#email.png

def send_mail():
      sender = 'limeng@space-time.site'
      receivers = ['supermans1201@163.com','2247674792@qq.com']
      emailsmtp='smtp.mxhichina.com'
      emailport=25
      password=*
      subjectstring='邮件发送'

      mail_msg = """<p>李盟向你发来了一封邮件</p>
     <p><a href="http://www.space-time.site">www.space-time.site</a></p>
     <p>图片演示：</p>
     <p><img src="cid:image1"></p>
        """
      #设置from to subject 和 date
      message = MIMEMultipart()
      message['From'] = Header(sender)
      message['To'] = ",".join(receivers )
      thetime= time.strftime( '%Y%m%d%H%M%S', time.localtime() )
      subject =subjectstring+thetime
      message['Subject'] = Header(subject, 'utf-8')
      message['date']=thetime
      #设置邮件信息（html），内含图片
      messageText= MIMEText(mail_msg, 'html', 'utf-8')
      message.attach(messageText)
      # 指定当前目录email.png图片为附件
      fp = open('email.png', 'rb')
      msgImage = MIMEImage(fp.read())
      fp.close()
      # 定义图片 ID，在 HTML 文本中
      msgImage.add_header('Content-ID', '<image1>')
      message.attach(msgImage)
      # 构造附件，为当前目录下的 email.txt 文件
      attachment = MIMEText(open('email.txt', 'rb').read(), 'base64', 'utf-8')
      attachment["Content-Type"] = 'application/octet-stream'
      # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
      attachment["Content-Disposition"] = 'attachment; filename="email.txt"'
      message.attach(attachment)
      try:
        handle = smtplib.SMTP(emailsmtp,emailport)
        handle.login(sender,password)
        handle.sendmail(sender,receivers,message.as_string())
        handle.close()
        print "Success send Email!"
      except smtplib.SMTPException:
        print "Error: 无法发送邮件"
        return 0
#运行当前文件时，执行sendmaill函数
if __name__ == "__main__":
     send_mail()
     # accpet_mail()
