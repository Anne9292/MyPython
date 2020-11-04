#! /usr/bin/env python
#-*- coding:utf-8 -*-

import socket

def test_webserver(HOST, PORT):

	# 新的socket
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# listen_socket绑定与监听
	listen_socket.bind((HOST, PORT))
	listen_socket.listen(100)


	print('The server is running on port %d' % PORT)
	print('The url is http://localhost:%d' % PORT)

	while True:
	    http_response = '''
		HTTP/1.1 200 OK
		Content-Type: text/html

		Hello, my first python server-8001
		'''
	    Client, Address = listen_socket.accept()
	    Request = Client.recv(1024)
	    Client.sendall(http_response.encode(encoding='utf-8'))
	    Client.close()

if __name__ == '__main__':
    test_webserver('localhost', 8001)
    # test_webserver('192.168.146.135', 8002)