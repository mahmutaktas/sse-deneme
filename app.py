from flask import Flask
from flask_cors import CORS

from controllers.DenemeController import deneme_page

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'


cors = CORS(app)




app.register_blueprint(deneme_page)

@app.route('/')
def hello_world():
    return 'Hello World!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
