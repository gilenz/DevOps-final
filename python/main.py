from flask import Flask, request, jsonify, send_file
from script import results
import csv
import requests

app = Flask(__name__)

def generate_csv():
    file_path = 'results.csv'
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(results())
    
    return file_path

@app.route("/results")
def result():
    return jsonify(results())

@app.route("/csv")
def csv_download():
    csv_file = generate_csv()
    
    return send_file(csv_file, as_attachment=True)

def check_api_status():
    try:
        response = requests.get('http://localhost:8000/results')
        if response.status_code == 200:
            return f"API is up and running, status code {response.status_code}"
        else:
            return f"API is down, status code {response.status_code}"
    except requests.RequestException:
        return "API is down"
    
def check_csv_status():
    try:
        response = requests.get('http://localhost:8000/csv')
        if response.status_code == 200:
            return f"CSV service is runing, status code {response.status_code}"
        else:
            return f"CSV service is down, status code {response.status_code}"
    except requests.RequestException:
        return "csv service is down" 

@app.route("/healthcheck")
def check():
    api_status = check_api_status()
    csv_status = check_csv_status()
    return f"{api_status}\n{csv_status}", 200, {"Content-Type": "text/plain"}



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
