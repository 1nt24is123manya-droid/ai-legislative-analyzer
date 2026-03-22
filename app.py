from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # ✅ Fixes frontend-backend connection

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query", "")

    print("Request received:", query)   # ✅ Debug

    # Simple logic (your analyzer)
    results = [
        f"Input received: {query}",
        "Legal rule detected in the text",
        "Possible penalty clause found",
        "Citizens must comply with regulations"
    ]

    return jsonify({"results": results})
import os
if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
