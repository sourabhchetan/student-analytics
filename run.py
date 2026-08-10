from flask import Flask
from app.config import Config
from app.routes import main
from app.auth import auth

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
