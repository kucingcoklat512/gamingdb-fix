from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

# Initialize app and database connection
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}}, supports_credentials=True)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://gamelistapi_herselfhis:f012f55225cd6fba2d296586b857fc038d6d57f5@qbxab.h.filess.io:3305/gamelistapi_herselfhis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test123'
db = SQLAlchemy(app)

app.app_context().push()
