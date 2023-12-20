# /quote_gen/tests/test_quote_gen.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_quote_endpoint(client):
    response = client.get('/quote')
    assert response.status_code == 200
    assert 'quote' in response.get_json()
