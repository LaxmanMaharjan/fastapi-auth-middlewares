# FastAPI Auth Middleware

FastAPI Auth Middlewawre is a middleware for securing FastAPI application. It provides a convenient way to secure your FastAPI routes and endpoints using jwt tokens.

## Features

- Seamless integration with FastAPI applications.
- Easily protect routes and endpoints with JWT authentication.
- Lightweight and designed for simplicity.


## Requirements

Python 3.8


* [FastAPI](https://fastapi.tiangolo.com/) obvisouly 😁😁😁😊😊
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/)

## Installation

<div class="termy">

```console
$ pip install fastapi_auth_middlewares
```

</div>

## Example

### Create it

* Create a file `main.py` with:
```Python
from fastapi import FastAPI, Request

from fastapi_auth_middlewares import JwtAuthMiddleware

app = FastAPI(
    title="Secured Project",
    version="1.0",
)


app.add_middleware(
    JwtAuthMiddleware,
    secret_key="your_secret_key",
    algorithms=["HS256"],
    # Excluding Documentation (OpenAPI and favicon routes) and health check routes from authentication
    public_paths=["/docs", "/favicon.ico", "/openapi.json", "/api/health"],
)


@app.get("/api/health")
async def health():
    return {"message": "server is up and running."}, 200


@app.get("/protected")
async def protected_route(request: Request):
    # Access the decoded_token from the middleware
    decoded_token = request.state.user

    # Your logic using the decoded_token
    user_id = decoded_token.get("user_id")
    username = decoded_token.get("username")

    return {
        "message": "This is a protected route",
        "user_id": user_id,
        "username": username,
    }

```


<div class="termy">

### Run it

* Run the server with:
```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

## Contributing 
Feel free to contribute to this project.

## License

This project is licensed under the terms of the MIT license.