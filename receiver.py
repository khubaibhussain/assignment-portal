from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def receive_report():
    data = request.get_json()
    
    with open('test-report.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Report received and saved to test-report.json!")
    return jsonify({"status": "success", "message": "Report saved"}), 200

if __name__ == '__main__':
    app.run(port=5001)