from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["http://localhost:3000"],
        }
    },
)

from flask_app import routes
