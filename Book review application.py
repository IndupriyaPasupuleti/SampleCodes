from flask import Flask, request, jsonify

app = Flask(__name__)
reviews = []

@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(reviews)

@app.route("/reviews", methods=["POST"])
def add_review():
    data = request.json
    required = ["book_name", "review", "rating"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if not (1 <= data["rating"] <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    reviews.append(data)
    return jsonify({"message": "Review added", "review": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
