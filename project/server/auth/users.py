from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
import json

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__, url_prefix='/users')


@users_blueprint.route('/index', methods=['GET'])
def get():
    
    user_list = User.query.all()
    data_list = []

    for row in user_list:
        userObject = {
            "admin": row.admin,
            "email": row.email,
            "id": row.id,
            "registered_on": row.registered_on
        }

        data_list.append(userObject)

    print(data_list)

    responseObject = {
        'status': 'success',
        'message': 'Get all users success',
        'users': data_list
    }
        
    return make_response(jsonify(responseObject)), 201


# # define the API resources
# users_view = UsersAPI.as_view('register_api')

# # add Rules for API Endpoints
# users_blueprint.add_url_rule(
#     '/users/index',
#     view_func=users_view,
#     methods=['GET']
# )