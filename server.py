#!/usr/bin/env python
# Author : Ramin Farajpour Cami (https://github.com/raminfp)
from rsa_encrypt import RSAEnrcyption
import pickle
import socket
import sys


class ServerRSA(object):

    def __init__(self):
        self.prv_key = None
        self.pup_key = None
        self.host = ''
	self.port = 4444

    def key_genrate(self):
        KEYS = RSAEnrcyption().generate_RSA()
        self.prv_key = KEYS[0]
        self.pub_key = KEYS[1]
        return (self.pub_key, self.prv_key)


    def private(self, prv_key, rsa_enc):
        return RSAEnrcyption().decrypt_RSA(prv_key,rsa_enc)

    def create_socket(self):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	self.bind_socket(s)

    def bind_socket(self, s):
	s.bind((self.host, self.port))
	s.listen(1)
	print "Server is running on port %d; \npress Ctrl-C to terminate." % self.port
        self.ifinity_loop_sock(s)

    def ifinity_loop_sock(self, s):

	while 1:
            try:
 	        clientsock, clientaddr = s.accept()
  	        print "Connection from ", clientsock.getpeername()
  	        key_gen = ServerRSA().key_genrate()
  	        clientsock.send(pickle.dumps(key_gen[0]))
  	        rcstring = ''
  	        while 1:
    	            buf = clientsock.recv(1024)
    	            rcstring += buf
    	            if not len(buf):
      		        break
  	        clientsock.close()
  	        encmessage = pickle.loads(rcstring)
  	        print ServerRSA().private(key_gen[1], encmessage)

            except:
                print "CTRL + C to exit program"
                break
def main():

    get_obj_serv = ServerRSA().create_socket()


if __name__ == "__main__":
     main()
