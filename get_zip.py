from config import oc
from upload import upload


#####
# Unable to zip file on NextCloud
# So download zip first,
# then upload zip to original dir on NextCloud
#####
def get_zip(dir_path):
    file_name = dir_path.split('/')[1] + '.zip'
    local_path = 'pdf/' + file_name
    oc.get_directory_as_zip(remote_path=dir_path, local_file=local_path)  # Download zip
    file_path = upload(dir_path, local_path)  # Upload zip
    return file_path


if __name__ == '__main__':
    d_path = 'testdir/vendor1/vendor1'
    get_zip(d_path)
