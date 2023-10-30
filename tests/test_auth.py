from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from database.base import SessionLocal

client = TestClient(app)

def setup_module():
    # criar um usuário teste
    db = SessionLocal()
    test_user = User(username="testuser", password_hash="hashedpassword")  # Lembre-se de hashear a senha!
    db.add(test_user)
    db.commit()
    db.close()

def test_get_token():
    response = client.post("/token", data={"username": "testuser", "password": "password"})  # Use a senha correta aqui
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_token_wrong_credentials():
    response = client.post("/token", data={"username": "testuser", "password": "wrongpassword"})
    assert response.status_code == 401
