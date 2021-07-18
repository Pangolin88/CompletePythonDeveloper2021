import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./Section17/email_playground/index.html').read_text())
email = EmailMessage()
email['from'] = <Name>
email['to'] = <email>
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(<your_email>, <your_password>)
  smtp.send_message(email)
  print('Done!')
