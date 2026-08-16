from machineid import id
from hashlib import sha256
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet


def _get_machineid() -> str:
    return id()


def _get_key(skey: str) -> bytes:
    return urlsafe_b64encode(sha256(skey.encode()).digest())


def encrypt(data: str) -> str:
    f = Fernet(_get_key(_get_machineid()))
    return f.encrypt(data.encode()).decode()


def decrypt(data: str) -> str:
    f = Fernet(_get_key(_get_machineid()))
    return f.decrypt(data).decode()
