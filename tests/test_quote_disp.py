# test_quote_disp.py
import pytest
from quote_disp.app import app as flask_app
from unittest.mock import Mock

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_endpoint(client):
    """Test the /health endpoint for the quote display service"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"healthy"

def test_home_endpoint(client):
    """Test the / endpoint to ensure it renders the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Quote Display Servic</title>" in response.data

def test_get_quote_endpoint(client, mocker):
    """Test the /get_quote endpoint to ensure it displays a quote"""
    mock_response = Mock()
    mock_response.text = "Test quote"
    mocker.patch('requests.get', return_value=mock_response)

    response = client.get("/get_quote")
    assert response.status_code == 200
    assert b"Test quote" in response.data