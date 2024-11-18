from flask import Blueprint, jsonify, request

coffee_bp = Blueprint('coffee', __name__)

# Route to get all coffees
@coffee_bp.route('/coffees', methods=['GET'])
def get_coffees():
    coffees = [
        {"id": 1, "name": "Espresso", "price": 3.0},
        {"id": 2, "name": "Latte", "price": 4.5}
    ]
    return jsonify(coffees)

# Route to add a new coffee
@coffee_bp.route('/coffees', methods=['POST'])
def add_coffee():
    data = request.json
    return jsonify({"message": f"Added coffee {data['name']}"}), 201
