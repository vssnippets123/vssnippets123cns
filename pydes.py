# pip install pycrypto
# pip install base32hex

# Encryption
import base32hex
import hashlib
from Crypto.Cipher import DES
password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key)
key = m.digest()
(dk, iv) = (key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

plain_text = input("Enter text: ")

print("The plain text is : ", plain_text)
plain_text += '\x00' * (8 - len(plain_text) % 8)
ciphertext = crypter.encrypt(plain_text)
encode_string = base32hex.b32encode(ciphertext)
print("The encoded string is : ", encode_string)


# Decryption
password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key)
key = m.digest()
(dk, iv) = (key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

encrypted_string = input("Enter cipher text: ")

print("The ecrypted string is : ", encrypted_string)
encrypted_string = base32hex.b32decode(encrypted_string)
decrypted_string = crypter.decrypt(encrypted_string)
print("The decrypted string is : ", decrypted_string)
