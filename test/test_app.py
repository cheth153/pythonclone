# tests/test_app.py
from flask import Flask
from app import app
import requests_mock

def test_home_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Hello, CI/CD!'

# New test for the /external-check route, using a mock to avoid actual API calls.
def test_external_check_route():
    with app.test_client() as client:
        with requests_mock.Mocker() as m:
            m.get('https://api.github.com', status_code=200)
            response = client.get('/external-check')
            assert response.status_code == 200
            assert response.data.decode('utf-8') == 'GitHub API Status: 200'
