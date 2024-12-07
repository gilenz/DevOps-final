from flask import Flask, request, jsonify
from script import results
import requests
app = Flask(__name__)

@app.route("/results")
def result():
    return results()


def check_api_status():
    try:
        response = requests.get('http://localhost:5000/results')
        if response.status_code == 200:
            return f"API is up and runing status code {response.status_code}"
        else:
            return f"API is down status code {response.status_code}"
    except requests.RequestException:
        return False

@app.route("/healthcheck")
def check():
    return check_api_status()
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    


