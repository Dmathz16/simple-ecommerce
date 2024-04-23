from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for

authentication = Blueprint('authentication', __name__)

# list
@authentication.route('/authentication/', methods=['GET'])
def index():
    return "LIST"

# post
@authentication.route('/authentication/api/', methods=['POST'])
def post():
    return "post"

# get
@authentication.route('/authentication/api/', methods=['GET'])
def get():
    return "get"

# put
@authentication.route('/authentication/api/', methods=['PUT'])
def put():
    return "put"

# delete
@authentication.route('/authentication/api/', methods=['DELETE'])
def delete():
    return "delete"