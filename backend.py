from werkzeug.serving import run_simple

import app

run_simple('localhost', 8080, application=app, use_reloader=True)