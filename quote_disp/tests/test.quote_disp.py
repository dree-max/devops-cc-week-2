# /quote_disp/tests/test_quote_disp.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_quote_endpoint(client):
    response = client.get('/get_quote')
    assert response.status_code == 200
    assert 'quote' in response.get_json()
