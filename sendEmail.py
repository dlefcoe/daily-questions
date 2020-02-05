


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


textfile = 'emailbodymessage.txt'

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
me = 'dlefcoe@gmail.com'
# you == the recipient's email address
you = 'jjc3po@gmail.com'

msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = you

serverName = 'smtp.gmail.com'
port = 465


# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()


