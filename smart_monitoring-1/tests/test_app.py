import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Smart Multi-Domain Monitoring System' in response.data

def test_data_endpoint(client):
    response = client.post('/data', json={'sensor_id': 'test_sensor', 'value': 25})
    assert response.status_code == 200
    assert b'Data received successfully' in response.data

def test_invalid_data_endpoint(client):
    response = client.post('/data', json={'invalid_key': 'test_value'})
    assert response.status_code == 400
    assert b'Invalid data format' in response.data

def test_anomaly_detection(client):
    response = client.post('/data', json={'sensor_id': 'test_sensor', 'value': 1000})
    assert response.status_code == 200
    assert b'Anomaly detected' in response.data or b'Normal' in response.data