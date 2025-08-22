# app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, CI/CD!"

# New route to demonstrate dependency changes
@app.route('/external-check')
def external_check():
    response = requests.get('https://api.github.com')
    return f"GitHub API Status: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
