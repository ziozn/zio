#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-27 17:02
# @Author  : Aries
# @Site    : 
# @File    : send_email.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText


class SendEmail:
	send_user = "1060793070@qq.com"
	email_host = 'smtp.qq.com'
	password = 'nvnlhekkamugbfji'

	def send_mail(self, user_list, sub, content):
		user = "zio" + '<' + self.send_user + '>'
		message = MIMEText(content, _subtype='plain', _charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ';'.join(user_list)
		server = smtplib.SMTP()
		server.connect(self.email_host)
		server.login(self.send_user, self.password)
		server.sendmail(user, user_list, message.as_string())
		server.close()


if __name__ == '__main__':
	sen = SendEmail()
	user_list = ['1223339885@qq.com']
	sub = '这个是测试邮件'
	content = '这个是我们第一封测试邮件'
	sen.send_mail(user_list, sub, content)
	












