from flask import Flask
from flask_cors import CORS

from controllers.DenemeController import deneme_page

app = Flask(__name__)

app.config['CORS_ALLOW_HEADERS'] = '*'
app.config['CORS_ORIGINS'] = '*'
app.config['CORS_SUPPORTS_CREDENTIALS'] = False
app.config['CORS_METHODS'] = ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH" "DELETE"]

cors = CORS(app)




app.register_blueprint(deneme_page)

@app.route('/')
def hello_world():
    return 'Hello World!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
