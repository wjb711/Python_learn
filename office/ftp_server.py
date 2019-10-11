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
