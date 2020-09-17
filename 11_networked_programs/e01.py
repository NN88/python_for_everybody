# Exercise 1:
# Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split('/') to break the URL into
# its component parts so you can extract the host name for the socket connect
# call. Add error checking using try and except to handle the condition where
# the user enters an improperly formatted or non-existent URL.

import socket

try:
    source = input("URL:") or 'http://data.pr4e.org/romeo.txt'
    port = input("PORT:") or 80

    # vars
    url = source.split('/')
    protocal = url[0] + '//'
    host = url[2]
    file = url[3]
    port = int(port)

    # connection
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(source).encode() # string interpolation with format()
    mysock.send(cmd)

    # stream
    while True:
        data = mysock.recv(20)
        if (len(data) < 1):
          break
        print(data.decode(),end='')

except (TypeError, IndexError, ConnectionRefusedError):
    print("Invalid URL or PORT")
    exit()

finally:
    mysock.close()
