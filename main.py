from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
from pathlib import Path

my_email = MIMEMultipart()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'text': 'Hello friend'})

html_part = MIMEText(html_content, 'html')
my_email.attach(html_part)

with open('images/email.png', 'rb') as img:
    image_data = img.read()
    # Attach image
    image_part = MIMEImage(image_data, name='email.png')
    my_email.attach(image_part)

my_email['from'] = '<your_name>'
my_email['to'] = "test@gmail.com"
my_email['subject'] = "<your_subject>"

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print("Email was sent...")