from flask import Flask
from app.routes import main
from app.auth import auth

app = Flask(__name__)
app.secret_key = "secret"

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)