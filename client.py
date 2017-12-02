#!/usr/bin/env python
# Author : Ramin Farajpour Cami (https://github.com/raminfp)

from rsa_encrypt import RSAEnrcyption
import pickle
import socket


class ClientRSA(object):

    def __init__(self):
    	self.host = 'localhost'
    	self.port = 4444

    def public(self, pub_key, msg):
        return RSAEnrcyption().encrypt_RSA(pub_key, str(msg))

    def create_socket(self):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.connection(s)

    def connection(self, s):
	try:
		s.connect((self.host, self.port))
		self.reciv_data(s)
	except :
	    raise

    def reciv_data(self, s):

	rcstring = s.recv(2048)
	publickey = pickle.loads(rcstring)
	secretText = ClientRSA().public(publickey, "hello! my friends")
	self.send_data(s,secretText)

    def send_data(self, s,secretText):
	print secretText
	s.sendall(pickle.dumps(secretText))
	s.close()


def main():

    get_obj = ClientRSA().create_socket()

if __name__ == "__main__":
    main()
