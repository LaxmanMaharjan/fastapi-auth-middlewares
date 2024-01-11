from datetime import datetime, timedelta

import jwt
import pytest


@pytest.fixture
def secret_key():
    return "secret_key"


@pytest.fixture
def invalid_secret_key():
    return "invalid_secret_key"


@pytest.fixture
def valid_jwt(secret_key):
    issued_at = datetime.utcnow()
    expiration_time = issued_at + timedelta(days=1)
    payload = {
        "sub": "laxmanmaharjan@example.com",
        "name": "Laxman Maharjan",
        "iat": issued_at,
        "exp": expiration_time,
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")


@pytest.fixture
def invalid_jwt(invalid_secret_key):
    issued_at = datetime.utcnow()
    expiration_time = issued_at + timedelta(days=1)
    payload = {
        "sub": "laxmanmaharjan@example.com",
        "name": "Laxman Maharjan",
        "iat": issued_at,
        "exp": expiration_time,
    }
    return jwt.encode(payload, invalid_secret_key, algorithm="HS256")


@pytest.fixture
def expired_jwt(secret_key):
    issued_at = datetime.utcnow()
    expiration_time = issued_at - timedelta(days=1)
    payload = {
        "sub": "laxmanmaharjan@example.com",
        "name": "Laxman Maharjan",
        "iat": issued_at,
        "exp": expiration_time,
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")
