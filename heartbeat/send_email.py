#!/usr/bin/python

import smtplib


sender = 'nagios2'
receivers = ['radision@126.com']


message = """From: Nagios <nagios@localhost>
To: Systems <radision@126.com>
Subject: Alert from nagios2

Heartbeat Timeout
"""

try:
  smtpObj = smtplib.SMTP('localhost', 25)
  smtpObj.sendmail(sender, receivers, message)
  print "Successfully sent email"
except smtplib.SMTPException:
  print "Error: unable to send email"


