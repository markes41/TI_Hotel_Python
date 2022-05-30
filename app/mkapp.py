from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@api-postgres:5432/postgres"
app.config['JWT_SECRET'] = 'a5b31BC19peQf25mCsaq'
db = SQLAlchemy(app)