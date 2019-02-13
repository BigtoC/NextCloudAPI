import owncloud
import NextCloud

url = 'http://10.0.1.26/'  # NextCloud server
user = 'my_name'  # Login name
pwd = 'my_pwd'  # login password
tojs = True  # if True, output format is json. if False, output format is xml

pwd_len = 10  # share url password length

# Two libraries
oc = owncloud.Client(url)
oc.login(user, pwd)
nxc = NextCloud.NextCloud(url, user, pwd, tojs)


