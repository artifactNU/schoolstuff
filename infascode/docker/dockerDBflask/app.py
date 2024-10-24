from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {}


@app.route("/")
def hello():
    return "Hello, Docker!"


@app.route("/data", methods=["GET", "POST"])
def handle_data():
    if request.method == "GET":
        return jsonify(data_store), 200

    if request.method == "POST":
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400

            key = data.get("key")
            value = data.get("value")

            if not key or not value:
                return jsonify({"error": "Both 'key' and 'value' are required"}), 400

            data_store[key] = value
            return jsonify({"message": "Data stored successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# curl -X POST http://localhost:5000/data -H "Content-Type: application/json" -d '{"key": "example", "value": "Hello, World!"}'
# curl -X GET http://localhost:5000/data
