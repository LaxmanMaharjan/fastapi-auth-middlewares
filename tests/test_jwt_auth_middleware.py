from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_auth_middlewares import JwtAuthMiddleware

app = FastAPI()
app.add_middleware(JwtAuthMiddleware, secret_key="secret_key", public_paths=["/public"])


@app.get("/protected")
async def protected_route():
    return {"message": "This is a protected route"}


@app.get("/public")
async def public_route():
    return {"message": "This is a public route"}


def test_middleware_allows_access_to_public_paths():
    client = TestClient(app)

    response = client.get("/public", headers={"Authorization": "Bearer token"})

    assert response.status_code == 200
    assert response.json() == {"message": "This is a public route"}


def test_successful_verification(
    valid_jwt,
):
    client = TestClient(app)
    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "This is a protected route"}


def test_missing_header():
    client = TestClient(app)
    response = client.get("/protected")
    assert response.status_code == 401
    assert response.json() == {"message": "Invalid Credentials."}


def test_invalid_token(
    invalid_jwt,
):
    client = TestClient(app)
    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {invalid_jwt}"},
    )
    print(response.text)
    assert response.status_code == 401
    assert response.json() == {
        "message": "Invalid Token. Signature verification failed."
    }


def test_expired_token(
    expired_jwt,
):
    client = TestClient(app)
    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {expired_jwt}"},
    )
    print(response.text)
    assert response.status_code == 401
    assert response.json() == {"message": "Token has expired. Signature has expired."}
