import os
import math
import random
import smtplib

nums = '0123456789'
OTP = ''
for i in range(6):
    OTP += nums[math.floor(random.random()*10)]          # Genrates the random num
a = OTP + ' is your unique code'
token = a

smtp = smtplib.SMTP('smtp.gmail.com', 587)              # Gmail smpt sever for sending mails
smtp.starttls()
smtp.login('Enter your gmail', 'Enter your google app password')        # Here enter your gmail account, and google app password 
users_id = input('Enter your email: ')
smtp.sendmail('&&&&&&&&&&', users_id, token)
x = input('Enter your OTP code >> ')
if x == OTP:
    print('Access Granted!')
else:
    print('Invalid OTP code, please check and try again.')
