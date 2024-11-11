import pytest
from app import app # Import The flask app

@pytest.fixture
def client():
    # Use Flask's test client for making requests to the API
    with app.test_client() as client:
        yield client

# GET request to the endpoint with test username
def test_get_gists(client):
    response = client.get('/octocat')
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    gists = response.get_json()
    assert isinstance(gists, list), "Expected response to be a list"
    
    # Check for existing gists if any
    if gists:
        required_keys = {"id", "url", "description"}
        for gist in gists:
            assert required_keys.issubset(gist.keys()), f"Gist missing keys: {required_keys - set(gist.keys())}"
            
def test_get_gists_user_not_found(client):
    response = client.get('/gfhfgbdgfbmokase3093?????')
    assert response.status_code == 404, "Expected status code 404 for a non-existent user"
    error_message = response.get_json()
    assert "error" in error_message, "Expected an error message in the response"
    assert "Not Found" in error_message["error"], "Expected 'Not Found' in the error message"
    