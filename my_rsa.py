from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import base64

message = 'To be signed'
key = RSA.importKey(open('fuyou_pri.pem').read())
import pdb
# pdb.set_trace()
en_message = message.encode("utf-8")
h = SHA.new(en_message)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(h)
my_si = base64.b64encode(signature).decode("ascii")
print(my_si)
# print(signature.decode("utf-8"))

