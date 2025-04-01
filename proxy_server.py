from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import requests

app = Flask(__name__)

# Enable CORS for all routes and allow requests from the frontend's origin
CORS(app, resources={r"/proxy/*": {"origins": "http://127.0.0.1:8000"}}, supports_credentials=True)

@app.route('/proxy/analyze', methods=['POST'])
def proxy_analyze():
    try:
        data = request.json  # Parse JSON from the request
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request body"}), 400

        # Forward the request to the main backend
        response = requests.post("http://127.0.0.1:5000/api/analyze", json=data)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Return the response from the main backend
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error forwarding request: {e}")
        return jsonify({"error": "Failed to forward request"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)