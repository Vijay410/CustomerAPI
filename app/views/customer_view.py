from flask import Blueprint, request, jsonify
from app.controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required, get_jwt_identity

customer_view = Blueprint('customer_view', __name__)

@customer_view.route('/api/customers', methods=['GET'])
@jwt_required()
def get_all_customer():
    return CustomerController.get_all()


@customer_view.route('/api/customers/<int:id>', methods=['GET'])
@jwt_required()
def get_customer(id):
    return CustomerController.get_by_id(id)

@customer_view.route('/api/customers', methods=['POST'])
@jwt_required()
def create_customer():
    data = request.json
    if 'name' not in data or 'email' not in data or 'address' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    return CustomerController.create(data)
    
@customer_view.route('/api/customers/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer(id):
    data = request.json
    return CustomerController.update(id,data)

@customer_view.route('/api/customers/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer(id):
    return CustomerController.delete(id)
