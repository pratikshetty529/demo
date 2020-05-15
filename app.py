from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/')
@app.route('/index')
def index():
    return "Paper Analysis"


if __name__ == "__main__":
    app.run(debug=True, port=5003)
