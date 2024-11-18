from flask import Blueprint, jsonify, request

new_user_bp = Blueprint("New User", __name__)

@new_user_bp.route("/signup", methods=["POST"])
def newUser(request):
    data = request.body
    fname = data.fname
    lname = data.lname
    email = data.email
    password = data.password

    return jsonify({newUser: data})
