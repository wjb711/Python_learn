'''
pyftpdlib内部使用utf8，而windows使用gbk，可以将pyftpdlib进行修改：

1、filesystems.py

AbstractedFS.format_list与AbstractedFS.format_list最后一行

yield line.encode('utf8', self.cmd_channel.unicode_errors)

utf8改为gbk

 

2、handlers.py

FTPHandler.decode

return bytes.decode('utf8', self.unicode_errors)

utf8改为gbk

'''
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "./ftp", perm="elradfmwMT")
authorizer.add_anonymous("./anonymous",perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
