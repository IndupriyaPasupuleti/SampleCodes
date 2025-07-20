from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    required_fields = ["title", "description", "due_date", "priority"]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    tasks.append(data)
    return jsonify({"message": "Task added", "task": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
