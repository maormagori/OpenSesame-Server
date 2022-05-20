from app import app


@app.route("/open")
def open_gate():
    return "<p>Opening Gate!</p>"


@app.route("/close")
def close_gate():
    return "<p>Closing Gate!</p>"
