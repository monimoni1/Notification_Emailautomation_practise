import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = MIMEMultipart('alternative')
email['from'] = 'Study girl'
email['to'] ='mishitanath@gmail.com, mishitanath1998@gmail.com'
email['subject'] = 'this is a test'

#This is for the body of the email.
html = '<html><body><p>Hi, This is a test message!</p></body></html>'
part2 = MIMEText(html, 'html')

email.attach(part2)

#email.set_content('i am learnign !')

#with smtplib.SMTP(host='smtp.gmail.com', port=465) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    smtp.ehlo()
    #smtp.starttls()
    smtp.login('codingtest227@gmail.com', 'zuefwskvjswyxtec')
    smtp.send_message(email)
    print('all done')

          #fhxwftaqsxxsduia