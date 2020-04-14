from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from db_module import neo4j

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
neo4j.init_connection(app)

# index page
@app.route('/')
@cross_origin()
def index():
    return 'Simple REST API for Foodies Neo4J data using Flask.'


# Endpoint: get all users
@app.route('/api/users', methods=['GET'])
@cross_origin()
def get_all_users():
    return jsonify(neo4j.get_users_json())


# Endpoint: get user by id
@app.route('/api/users/<int:user_id>')
@cross_origin()
def get_user_by_id(user_id):
    return jsonify(neo4j.get_users_json(user_id))


# Endpoint --> recommendation by users w/ similar tastes, same restaurant
@app.route('/api/users/<int:user_id>/recommendation_1')
@cross_origin()
def get_recommendation_by_similar_tastes(user_id):
    return jsonify(neo4j.get_recommendation(user_id, 1))


# Endpoint --> recommendation by same subcategory dish, same restaurant
@app.route('/api/users/<int:user_id>/recommendation_2')
@cross_origin()
def get_recommendation_by_simiar_category(user_id):
    return jsonify(neo4j.get_recommendation(user_id, 2))


# Endpoint --> recommendation by friends, same restaurant
@app.route('/api/users/<int:user_id>/recommendation_3')
@cross_origin()
def get_recommendation_by_friends(user_id):
    return jsonify(neo4j.get_recommendation(user_id, 3))


if __name__ == '__main__':
    app.run(debug=True)
