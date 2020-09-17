# Exercise 2:
# Change your socket program so that it counts the number of characters it has
# received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number
# of characters and display the count of the number of characters at the end
# of the document.

import socket

try:
    # inputs
    source = input("URL:") or 'http://data.pr4e.org/mbox-short.txt'
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
    count = 0
    while True:
        data = mysock.recv(20)
        count = count + len(data)

        # stops displaying any text after it has shown 3000 characters.
        if (count < 3000):
            print(data.decode(),end='')

        # retrieve the entire document and count the total number
        # of characters and display the count of the number of characters at the end
        # of the document.
        if (len(data) < 1):
            print("count", count)
            break

except (TypeError, IndexError, ConnectionRefusedError):
    print("Invalid URL or PORT")
    exit()

finally:
    mysock.close()
