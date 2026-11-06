def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["data"]["status"] == "ok"

def test_database_health_endpoint(client):
    response = client.get("/api/v1/health/db")

    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["data"]["database"] == "connected"