from app import app, opengate, auth


@app.route("/open")
@auth.requires_auth
def open_gate(claims, *args, **kwargs):
    return "<p>Opening Gate!</p>"


@app.route("/close")
@auth.requires_auth
def close_gate(claims, *args, **kwargs):
    return "<p>Closing Gate!</p>"
