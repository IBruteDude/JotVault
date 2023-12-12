from hashlib import sha512

def hash_password(password: str) -> bytes:
    ''' Hash a string using the sha512 algorithm '''
    password_bytes = password.encode('utf-8')

    hash = sha512()

    hash.update(password_bytes)

    hashed_password_bytes = hash.digest()

    return hashed_password_bytes
