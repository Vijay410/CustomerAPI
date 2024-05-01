from app.models.customer import Customer
from app import db
from flask import jsonify,request

class CustomerController:
    @staticmethod
    def get_all():
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=1, type=int)
            customers = Customer.query.paginate(page=page, per_page=per_page, error_out=False)
            result = []
            for customer in customers:
                result.append({
                    'id': customer.id,
                    'name': customer.name,
                    'email': customer.email
                })
            response_data = {
                'customers': result,
                'total_customers': customers.total,
                'current_page': customers.page,
                'per_page': customers.per_page
        }
            return jsonify(response_data),200
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'error': str(e), 'status': 'FAILED'}), 500

    @staticmethod
    def get_by_id(id):
        try:
            customer = Customer.query.get(id)
            if customer:
                return jsonify(customer.serialize())
            else:
                return jsonify({'message': 'Customer not found'}), 404
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
        
    @staticmethod
    def create(data):
        try:
            customer = Customer(**data)
            db.session.add(customer)
            db.session.commit()
            return jsonify({'message': 'Customer created successfully'}), 201
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
    
    @staticmethod
    def update(id, data):
        try:
            customer = Customer.query.get(id)
            if customer:
                for key, value in data.items():
                    print(key,value)
                    setattr(customer, key, value)
                db.session.commit()
                return jsonify({'message': 'Customer updated successfully'}),201
            else:
                return jsonify({'message': 'Customer not found'}), 404
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

    @staticmethod
    def delete(id):
        try:
            customer = Customer.query.get(id)
            if customer:
                db.session.delete(customer)
                db.session.commit()
                return jsonify({'message': 'Customer deleted successfully'}),201
            else:
                return jsonify({'message': 'Customer not found'}), 404
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500