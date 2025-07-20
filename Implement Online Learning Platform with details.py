from flask import Flask, request, jsonify

app = Flask(__name__)
modules = []

@app.route("/modules", methods=["GET"])
def get_modules():
    return jsonify(modules)

@app.route("/modules", methods=["POST"])
def add_module():
    data = request.json
    required = ["module_name", "status", "completed_on"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    modules.append(data)
    return jsonify({"message": "Module added", "module": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
