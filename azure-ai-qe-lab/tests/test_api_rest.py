import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_validates_contract():
    """
    Enterprise API Test: Validates status code, schema contract, and required fields.
    """
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data
    print("API Contract Test PASSED: GET /posts/1")

def test_post_resource_creation():
    """
    Enterprise API Test: Validates resource creation via POST request.
    """
    payload = {
        "title": "Azure AI QE Lab",
        "body": "Automated API contract testing",
        "userId": 101
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    
    response = requests.post(f"{BASE_URL}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data
    print("API Resource Creation Test PASSED: POST /posts")
