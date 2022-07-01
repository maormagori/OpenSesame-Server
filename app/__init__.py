from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from app import routes  # noqa

app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
