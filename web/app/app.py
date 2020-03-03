

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
app.config['FLASK_APP']="app/app.py"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:#########@localhost:5432/postgres"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.route('/')
def hello():
    return "<h1>Hello Container World! Postgres works</h1>"

#if __name__ == "__main__":
   # app.run()