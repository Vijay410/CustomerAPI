from app import db #import db from app

class Customer(db.Model):
    """Adding a Customer in the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(255))
    state = db.Column(db.String(50))

    def serialize(self):
        """ Serialize the Customer object into a dictionary.
        
        Returns:
            dict: A dictionary containing the serialized attributes of the Customer object.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address
        }
    
