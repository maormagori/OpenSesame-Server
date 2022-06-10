import flask
from app import app, opengate, auth


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


@app.route("roles/add/<UUID:user_id>")
def add_role(user_id):
    ali_baba_id, roles = flask.request.args.get(
        "uid", ""), flask.request.args.get("roles")

    if not auth.is_ali_baba(ali_baba_id):
        flask.abort(403)

    if not auth.get_user_roles(user_id):
        flask.abort(flask.Response("UID missing from database", 404))

    auth.set_user_roles(user_id, roles, ali_baba_id)
