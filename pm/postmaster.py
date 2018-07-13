import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class PostMaster:
    from_address = ''
    to_address = ''
    subject = ''
    text = ''

    def __init__(self, subject, text, fromaddr, toaddr):
        self.subject = subject
        self.text = text
        self.from_address = fromaddr
        self.to_address = toaddr

    def set_from_address(self, address):
        self.from_address = address

    def set_to_address(self, address):
        self.to_address = address

    def send(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.from_address
        msg['To'] = self.to_address
        msg.attach(MIMEText(self.text, 'plain'))

        # Send the email out
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("dateng.cognex@gmail.com", "Shadow@900702")
        s.sendmail(self.from_address, [self.to_address], msg.as_string())
        s.quit()
