# symmetric encryption
from cryptography.fernet import Fernet


key = Fernet.generate_key()
print("key: %s" % key)

"""file = open("mykey.key", "wb")
file.write(key)
file.close()

file = open("mykey.key", "wb")
file.read()
file.close()"""


message_raw = "W Ottawie jest bardzo zimno"
message = message_raw.encode()
f = Fernet(key)
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)

print("message_raw: %s" % message_raw)
print("message: %s" % message)
print("encrypted: %s" % encrypted)
print("decrypted: %s" % decrypted)
