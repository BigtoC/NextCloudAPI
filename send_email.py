from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email(mail_receiver, mail_content):
    subject = 'Vendor PDF'
    from_address = 'bigtochan@hkcec.com'
    login_pwd = '612700'
    share_link = mail_content['share_url']
    pwd = mail_content['password']
    mail_body = f'Click this link to download your pdf files: {share_link} \nYour password is: {pwd}'
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = mail_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(mail_body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP('mail06.hkcec.nws', 25)
        # server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(from_address, login_pwd)
        server.sendmail(from_address, mail_receiver, msg.as_string())
        server.close()
        print(f'Success send email to {mail_receiver}')
    except smtplib.SMTPException as se:
        print(f'Fail to send email, smtplib.SMTPException: {se}')


if __name__ == '__main__':
    content = {'share_url': 'http://10.0.1.26/s/HNDSBBEPCBfZGZL', 'password': 'KoQrOB3BpE'}
    receiver = 'bigtochan@hkcec.com'
    send_email(receiver, content)
