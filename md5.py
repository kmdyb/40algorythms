from passlib.hash import md5_crypt


myHash = md5_crypt.hash("myPassword")

print(myHash)

print(md5_crypt.verify("myPassword", myHash))
print(md5_crypt.verify("myPassword2", myHash))
