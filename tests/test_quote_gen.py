# test_quote_gen.py
import pytest
from quote_gen.app import app as flask_app # Import the Flask application

@pytest.fixture
def app():
    """
    This is a fixture that provides the Flask app for testing.
    """
    yield flask_app

@pytest.fixture
def client(app):
    """
    This fixture provides a test client for the app.
    """
    return app.test_client()

def test_health_endpoint(client):
    """
    Test the /health endpoint to ensure it returns 'healthy'
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "healthy"

def test_home_endpoint(client):
    """
    Test the / endpoint to ensure it renders the correct page
    """
    response = client.get("/")
    assert response.status_code == 200
    # Check if the response contains part of the expected HTML
    assert '<title>Quote Gen Servic</title>' in response.data.decode('utf-8')

def test_quote_endpoint(client):
    """
    Test the /quote endpoint to ensure it returns a valid quote.
    """
    response = client.get("/quote")
    assert response.status_code == 200
    assert response.data.decode('utf-8') in [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    ]
