import functools
import google.oauth2
import google.auth.transport.requests as requests
from flask import request, Response
from app import app
config = app.config

request = requests.Request()


def requires_auth(func):
    @functools.wraps(func)
    def auth_validate_wrapper(*args, **kwargs):
        id_token = request.headers['Authorization'].split(' ').pop()
        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, request, audience=config['GOOGLE_CLOUD_PROJECT'])
        if claims:
            return func(claims=claims, *args, **kwargs)
        else:
            return Response("User not authenticated!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return auth_validate_wrapper
