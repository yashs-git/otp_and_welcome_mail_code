#for sending email otp verification
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#global variable 

#Here the code of OTP verification starts
# function to generate OTP
def generateOTP() :
    OTP = ''.join([str(random.randint(0,9)) for i in range(4)])
 
    return OTP

def get_mail_content(otp:str):
    mail_content = ""
    with open('otp_verification_mail_template.html', 'r') as f:
        mail_content = f.read()
    mail_content = mail_content.replace('<h1 id="otp">23815</h1>',f'<h1 id="otp">{otp}</h1>')
    return mail_content

#function to generate email to send at any mail
def email_send(otp, email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "OTP"
    msg['From'] = 'no-reply@celetel.com'
    msg['To'] = email
    text = f"Your OTP is {otp}"
    html = get_mail_content(otp)
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("no-reply@celetel.com", "pfjdomiugpyknhux")
    s.sendmail('no-reply@celetel.com',email,msg.as_string())
    s.close()

if __name__ == "__main__":
    otp = generateOTP()
    print(otp)
    email_send(otp, email)
#here the code of otp verification ends


#Here the code of verified otp Welcome mail starts
#function to read welcome mail html template
def welcome_mail_read():
    mail_content = ""
    with open('welcome_mail_template.html', 'r') as f:
        mail_content = f.read()
    return mail_content

#function to create a welcome mail
def welcome_email_send(email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Welcome to Celetel Technologies"
    msg['From'] = 'no-reply@celetel.com'
    msg['To'] = email
    html = welcome_mail_read()
    part = MIMEText(html, 'html')
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("no-reply@celetel.com", "pfjdomiugpyknhux")
    s.sendmail('no-reply@celetel.com',email,msg.as_string())
    s.close()

    
 #ere the code of welcome mail is finished