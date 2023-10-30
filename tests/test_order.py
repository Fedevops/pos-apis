from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User, Order, Item
from database.base import SessionLocal

client = TestClient(app)

def setup_module():
    # criar um pedido de teste
    db = SessionLocal()
    test_order = Order(total_price=100.0)
    db.add(test_order)
    db.commit()

    test_item = Item(name="TestItem", price=50.0, quantity=2, order_id=test_order.id)
    db.add(test_item)
    db.commit()
    
    db.close()

def test_create_order():
    response = client.post("/order", json={"total_price": 150.0})
    assert response.status_code == 200
    assert response.json()["total_price"] == 150.0

def test_get_order():
    response = client.get("/order/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["total_price"] == 100.0

# ... e assim por diante, para outros endpoints e cenários de teste
