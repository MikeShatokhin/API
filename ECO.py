from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demo purposes
users = {
    "user1": {"name": "Alice", "age": 25, "email": "alice@example.com"},
    "user2": {"name": "Bob", "age": 30, "email": "bob@example.com"},
    "user3": {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
}

@app.route("/")
def home():
    return "Welcome to the User API!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = "user{}".format(len(users) + 1)
    users[user_id] = data
    return jsonify({"user_id": user_id})

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()