import functools
import google.oauth2
import google.auth.transport.requests as requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import request, Response
from app import app
config = app.config

request = requests.Request()

cred = credentials.Certificate(config['SERVICE_ACCOUNT_KEY_FILE'])
firebase_admin.initialize_app(cred)
db = firestore.client()
users_collection = db.collection('users')


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


def is_theif(uid):
    roles = get_user_roles(uid)
    return roles.get('theif', False)


def is_ali_baba(uid):
    roles = get_user_roles(uid)
    return roles.get('aliBaba', False)


def get_user_roles(uid):
    u_doc = users_collection.document(f'{uid}').get()

    if u_doc.exists:
        return u_doc.to_dict().get('roles')
    else:
        return None
