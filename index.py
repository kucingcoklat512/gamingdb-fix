from flask import Flask, request, jsonify  # Add the request import
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, verify_jwt_in_request
from config import app, db
from routes.Game_bp import game_bp
from routes.Genre_bp import genre_bp
from routes.Developer_bp import developer_bp
from routes.Publisher_bp import publisher_bp
from routes.Platform_bp import platform_bp
from routes.User_bp import user_bp
from routes.Rating_bp import rating_bp
from flask_swagger_ui import get_swaggerui_blueprint

jwt = JWTManager(app)

@app.before_request
def before_request():
    excluded_routes = ['/api/login', '/api/users', '/swagger']
    if request.path in excluded_routes:
        return None
    try:
        verify_jwt_in_request()  # This validates the JWT in the request
    except Exception as e:
        return jsonify({"message": str(e)}), 401

@app.route("/api/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Register blueprints
app.register_blueprint(game_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(developer_bp)
app.register_blueprint(publisher_bp)
app.register_blueprint(platform_bp)
app.register_blueprint(user_bp)
app.register_blueprint(rating_bp)

# Swagger configuration
SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # Path to your Swagger JSON file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "GameList"}
)
# Register the blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
db.create_all()
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
