from sklearn.linear_model import LogisticRegression
from cryptography.fernet import Fernet
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from pickle import dump, load

iris = load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LogisticRegression()
model.fit(X_train, y_train)

filename_source = 'myModel_source.sav'
filename_destination = "myModel_destination.sav"
filename_sec = "myModel_sec.sav"

dump(model, open(filename_source, 'wb'))


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename_sec, "wb") as file:
        file.write(encrypted_data)


write_key()
encrypt(filename_source, load_key())


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename_destination, "wb") as file:
        file.write(decrypted_data)


decrypt(filename_sec, load_key())

loaded_model = load(open(filename_destination, "rb"))
result = loaded_model.score(X_test, y_test)
print(result)
