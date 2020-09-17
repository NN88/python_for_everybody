# Exercise 5: (Advanced)
# Change the socket program so that it only shows data after the headers and a
# blank line have been received. Remember that recv is receiving characters
# (newlines and all), not lines.

import socket

try:
    source = input("URL: ") or 'http://data.pr4e.org/romeo.txt'
    port = input("PORT: ") or 80

    # vars
    url = source.split('/')
    protocal = url[0] + '//'
    host = url[2]
    file = url[3]
    port = int(port)
    count = 0
    # this b (binary mode) is very important to allow response = response + data
    # otherwise you get a "can only concatenate str (not "bytes") to str" exception.
    # response = "" is incorrect use this instead:
    response = b""

    # connection
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(source).encode() # string interpolation with format()
    mysock.send(cmd)

    # stream
    while True:
        data = mysock.recv(5120) # data stream by bytes
        if (len(data) < 1): break # break if you hit end of file
        response = response + data # make sure response is in b"" binary mode, and add data to it
    mysock.close() # close connection

    # Find the Header and its end point
    pos = response.find(b"\r\n\r\n")

    # Add 4 characters to the end of the header possition which are the
    # "\r\n\r\n" characters, and print out the rest which is the file we want.
    target = response[pos+4:]
    print(target.decode().rstrip())

except Exception as e:
    print('Error is: ', e)
    exit()

finally:
    exit();

