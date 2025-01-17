from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api/v1/users")
def list_users():
    result = {
        'data': 'User example'
    }
    return result


if __name__ == '__main__':
    app.run(debug=True)
