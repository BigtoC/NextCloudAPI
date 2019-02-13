from config import oc

'''
    Remark:
    The upload procedure as follow ↓↓↓
    1) Create a file on NextCloud, file name is as same as the file we want to upload
    2) Upload the file in local path
    3) Replace the file on NextCloud with the file I upload
'''


def upload(upload_path, local_file):
    for file in local_file:
        upload_handler(upload_path, file)


def upload_handler(upload_path, local_file):
    upload_path += '/' + local_file.split('/')[-1]  # Step 1 in the remark
    oc.put_file(upload_path, local_file)  # Step 2 && 3 in the remark
    return upload_path


if __name__ == '__main__':
    u_path = 'testdir'  # upload path
    # l_path = ['pdf/2.pdf']  # local file path, single file
    l_path = ['pdf/2.pdf', 'pdf/1.pdf']  # local file path, multi files
    upload(u_path, l_path)

