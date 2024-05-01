import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    # Create a test user
    with app.app_context():
        db.create_all()
        user = User(username='testuser1421', email='test12423@example.com', password="admin1")
        db.session.add(user)
        db.session.commit()

    yield client

def test_login_success(client):
    response = client.post('/api/login', json={'username': 'testuser1421', 'password': 'admin1'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_invalid_credentials(client):
    response = client.post('/api/login', json={'username': 'testuser14', 'password': 'a11dmin1'})
    assert response.status_code == 401
    assert 'message' in response.json
    assert response.json['message'] == 'Invalid username or password'

def test_login_missing_fields(client):
    response = client.post('/api/login', json={'username': 'testuser15', 'password': 'password'})
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Missing required fields'

def test_login_empty_fields(client):
    response = client.post('/api/login', json={'username': 'testuser16', 'password': 'password'})
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Username and password cannot be empty'

def test_login_long_username(client):
    response = client.post('/api/login', json={'username': 'a'*257, 'password': 'password'})
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Username is too long'

def test_login_long_password(client):
    response = client.post('/api/login', json={'username': 'testuser17', 'password': 'a'*257})
    assert response.status_code == 400
    assert 'message' in response.json
    assert response.json['message'] == 'Password is too long'

def test_login_special_characters(client):
    response = client.post('/api/login', json={'username': '!@#$%', 'password': 'password'})
    assert response.status_code == 401
    assert 'message' in response.json
    assert response.json['message'] == 'Invalid username or password'

if __name__ == '__main__':
    pytest.main()
