import socket

s = socket.socket()

host = 'www.zhihu.com'
port = 80

s.connect((host, port))

ip, port = s.getsockname()
print('log ip and port {} {}'.format(ip, port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\nConnection: close\r\n\r\n'.format(host)
request = http_request.encode('utf-8')
print('log request:\n', request)
s.send(request)

response = b''
while True:
    r = s.recv(1024)
    if len(r) == 0:
        break
    response += r
   
print('log response\n', response.decode('utf-8'))
