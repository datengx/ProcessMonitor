import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class PostMaster:
    fromaddr = ''
    toaddr = ''
    text = ''

    def __init__(self, text, fromaddr, toaddr):
        self.text = text
        self.fromaddr = fromaddr
        self.toaddr = toaddr

    def send(self):
        msg = MIMEMultipart()
        msg['Subject'] = 'Test email'
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg.attach(MIMEText(self.text, 'plain'))

        # Send the email out
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # s.starttls()
        s.login("dateng.cognex@gmail.com", "Shadow@900702")
        s.sendmail(self.fromaddr, [self.toaddr], msg.as_string())
        s.quit()