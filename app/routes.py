import flask
from app import app, opengate, auth
import json


@app.route("/open")
@auth.requires_auth
def open_gate(claims, *args, **kwargs):
    if auth.is_theif(claims['sub']):
        opengate.openGate()
        return "Opening Gate!"
    else:
        flask.abort(403)


@app.route("/close")
@auth.requires_auth
def close_gate(claims, *args, **kwargs):
    if auth.is_theif(claims['sub']):
        opengate.closeGate()
        return "Closing Gate!"
    else:
        flask.abort(403)
