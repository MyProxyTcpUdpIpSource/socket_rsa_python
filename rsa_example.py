#Author : Ramin Farajpour Cami (https://github.com/raminfp)
from rsa_encrypt import RSAEnrcyption


## Generator KEYS (publick_KEY, Private_KEY)

class PublicKEY(object):

    def __init__(self):
	self.prv_key = None
	self.pup_key = None

    def key_genrate(self):

	KEYS = RSAEnrcyption().generate_RSA()
        self.prv_key = KEYS[0]
        self.pub_key = KEYS[1]
	return (self.pub_key, self.prv_key)

    def public(self, pub_key, msg):

        MessgeEncrypt = RSAEnrcyption().encrypt_RSA(pub_key, str(msg))
        return MessgeEncrypt

    def private(self, prv_key, rsa_enc):

            MessageDecryptRSA = RSAEnrcyption().decrypt_RSA(prv_key,rsa_enc)
            return MessageDecryptRSA

key_gen = PublicKEY().key_genrate()
objencrypt = PublicKEY().public(key_gen[0], "malware")
print objencrypt


print  "#############################################DeCrypt###########################################"

objdecrypt = PublicKEY().private(key_gen[1], objencrypt)
print objdecrypt







