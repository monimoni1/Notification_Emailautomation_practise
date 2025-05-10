import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = MIMEMultipart('alternative')
email['from'] = 'Study girl'
email['to'] = 'mishitanath@gmail.com, mishitanath1998@gmail.com'
email['subject'] = 'this is a test'

# This is for the body of the email.
html_content = html.substitute(name='TinTin')  # Substitute variables into the template
part2 = MIMEText(html_content, 'html')

email.attach(part2)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    smtp.ehlo()
    smtp.login('codingtest227@gmail.com', 'zuefwskvjswyxtec')
    smtp.send_message(email)
    print('all done')
