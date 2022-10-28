import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

HOST = 'HOST'
USERNAME = 'USERNAME'
PRIVATE_KEY = 'file.ppk'
PORT = 1111

srv = pysftp.Connection(host = HOST, 
                        username = USERNAME, 
                        private_key = PRIVATE_KEY, 
                        port = PORT
                        cnopts = cnopts)

data = srv.listdir()
srv.close()

for i in data:
    print(i)
#https://jtuto.com/upload-files-to-sftp-server-using-python/
