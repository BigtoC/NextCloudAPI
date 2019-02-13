import get_zip
import share
import send_email
import upload

'''
    This program must run in python 3.7 or above!!!
'''


def run(upload_path, local_path, mail_receiver):
    upload.upload(upload_path, local_path)  # run upload
    share_path = get_zip.get_zip(upload_path)  # get the zip
    share_info = share.share(share_path)  # get share url and password
    print(share_info)
    send_email.send_email(mail_receiver, share_info)  # send share_info via email


if __name__ == '__main__':
    u_path = 'testdir/vendor3'
    # l_path = ['pdf/2.pdf']  # local file path, single file
    l_path = ['pdf/2.pdf', 'pdf/1.pdf']  # local file path, multi files
    receiver = 'bigtochan@hkcec.com'  # Receiver email address
    run(u_path, l_path, receiver)




