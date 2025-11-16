
import bcrypt

def _prepare_password(password: str | bytes) -> bytes:
    """
    Convert password to bytes, handle str/bytes input,
    and truncate to 72 bytes for bcrypt.
    """
    if isinstance(password, bytes):
        password = password.decode("utf-8", errors="ignore")
    return password.encode("utf-8", errors="ignore")[:72]

def hash_password(password: str | bytes) -> str:
    """
    Hash a password and return it as a UTF-8 string ready for DB storage.
    """
    password_bytes = _prepare_password(password)
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode("utf-8")

def verify_password(plain_password: str | bytes, hashed_password_str: str) -> bool:
    """
    Verify a plain password against a hashed password string from the database.
    """
    password_bytes = _prepare_password(plain_password)
    hashed_bytes = hashed_password_str.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

