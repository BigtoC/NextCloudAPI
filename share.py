import string
import random
from config import nxc, pwd_len
import time


def share(share_path):
    pwd = ''.join(random.choices(string.digits + string.ascii_letters, k=pwd_len))  # auto gen password
    nxc_share_info = nxc.createShare(path=share_path,  # create share and return share info
                                     shareType=3,    # type of nxc_share_info is dictionary
                                     password=pwd)

    # print(nxc_share_info)  # run this line to see return info after create share

    share_url = nxc_share_info.get('ocs').get('data').get('url')  # extract url from nxc_share_info

    vendor_share_info = {'share_url': share_url, 'password': pwd}  # put share_url and pwd into a dictionary

    #####
    # write log after share a url,
    # you can find logs in records.txt
    #####
    write_log = {
        'share_url': share_url,
        'password': pwd,
        'file_owner': nxc_share_info.get('ocs').get('data').get('uid_file_owner'),
        'file_path': nxc_share_info.get('ocs').get('data').get('path'),
        'create_time': time.asctime(time.localtime(time.time())),
    }
    with open('record.txt', 'a') as record:
        record.write(str(write_log))
        record.write('\n\n')
        record.close()

    # print(write_log)

    return vendor_share_info  # return the dictionary for sending email


if __name__ == '__main__':
    s_path = 'testdir/vendor1/vendor1.zip'
    share(s_path)
