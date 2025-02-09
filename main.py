from flask import Flask,blueprints
from flask_cors import CORS
from meth import meth


app = Flask(__name__)
CORS(app)

app.register_blueprint(meth)

if __name__ == '__main__':
    app.run(debug=True)

