import smtplib
from smtplib import SMTP


my_email = "mplacehome@gmail.com"
password = 'zcgaykbejslxoznr#'
try:
    connect =  smtplib.SMTP("smtp.gmail.com")
    connect.close()
except:
    print('cant connect')
# connect.starttls()
# connect.login(user=my_email, password=password)
# connect.sendmail(from_addr=my_email, to_addrs='mpalcehome@yahoo.com', msg='Hello')



#connect_yahoo = smtplib.SMTP