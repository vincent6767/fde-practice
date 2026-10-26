from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_analyze_incident_endpoint_success():
    response = client.post("/analyze-incident", json={"description": "Hello there!"})
    assert response.status_code == 200
    assert response.json() == {
        "severity": "High",
        "summary": "The incident involves a critical system failure affecting multiple users.",
        "possible_causes": [
            "Hardware failure",
            "Software bug",
            "Network issue"
        ],
        "recommended_next_steps": [
            "Restart the affected systems",]
    }

def test_post_analyze_incident_endpoint_whitespace_only():
    response = client.post("/analyze-incident", json={"description": " "})
    assert response.status_code == 422

def test_post_analyze_incident_endpoint_missing_description():
    response = client.post("/analyze-incident", json={})
    assert response.status_code == 422

def test_post_analyze_incident_endpoint_empty_description():
    response = client.post("/analyze-incident", json={"description": ""})
    assert response.status_code == 422