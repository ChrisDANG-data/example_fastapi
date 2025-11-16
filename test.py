
import bcrypt


def hash(password: str)-> bytes:
 
    if isinstance(password,bytes):
        password = password.decode('utf-8',errors='ignore')
    password_bytes = password.encode('utf-8', errors='ignore')[:72]
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())


def verify(plain_password: str, hashed_password: str):

    if isinstance(plain_password, bytes):
        plain_password = plain_password.decode('utf-8', errors='ignore')
    password_bytes = plain_password.encode('utf-8', errors='ignore')[:72]
    return bcrypt.checkpw(password_bytes, hashed_password)

hashed_pwd = hash("mypassword")         
hashed_str = hashed_pwd.decode("utf-8") 
print(hashed_pwd)
print(hashed_str)


verify("mypassword", hashed_str.encode("utf-8"))
