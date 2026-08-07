from machineid import id
from hashlib import sha256
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet


def get_machineid():
    return id()

def get_key(skey):
    return urlsafe_b64encode(sha256(skey.encode()).digest())

def encrypt(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt(key, data):
    f = Fernet(key)
    return f.decrypt(data).decode()



