from flask import Blueprint, jsonify, request

orders_bp = Blueprint('orders', __name__)

# Route to get all orders
@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 1, "customer": "John", "coffee": "Espresso", "quantity": 2}
    ]
    return jsonify(orders)

# Route to create a new order
@orders_bp.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    return jsonify({"message": f"Order for {data['customer']} created!"}), 201
