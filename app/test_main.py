import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test case for a valid query with top_k = 3
def test_valid_query():
    response = client.post("/query", json={"query": "Engineer", "top_k": 3})
    
    assert response.status_code == 200
    assert "Engineer" in response.text 
    assert "1:" in response.text  

# Test case for a query that returns no results
def test_query_no_results():
    response = client.post("/query", json={"query": "Astronaut", "top_k": 3})
    
    assert response.status_code == 200
    assert "No relevant contexts found for your query." in response.text  # Ensure no results message is returned

# Test case for invalid top_k
def test_invalid_top_k():
    response = client.post("/query", json={"query": "Engineer", "top_k": -1})
    
    assert response.status_code == 200
    assert "Warning: 'top_k' was invalid. Using default value of 5." in response.text  # Ensure warning message for invalid top_k

# Test case for missing query field
def test_missing_query():
    response = client.post("/query", json={"top_k": 3})
    
    assert response.status_code == 422  # Unprocessable Entity (validation error)
    assert "query" in response.json()['detail'][0]['loc']  # Ensure 'query' field is missing in the error


