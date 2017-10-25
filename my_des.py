from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Util import Counter
import base64

key = b'-8B key-'
nonce = Random.new().read(DES.block_size//2)
ctr = Counter.new(DES.block_size*8//2, prefix=nonce)
cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
plaintext = b'we are no loger the knights who say hi'
msg = nonce+cipher.encrypt(plaintext)
final_msg = base64.b64encode(msg).decode("utf-8")
print(final_msg)