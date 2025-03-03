from flask import Flask, jsonify, request

app = Flask(__name__)
users = []  # In-memory storage for users

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the IELTS Speaking Test Platform!"})

# Info Route
@app.route('/info')
def info():
    return jsonify({
        "platform_name": "IELTS Speaking Test Platform",
        "version": "1.0",
        "developer_contact": "support@example.com"
    })

# Register User Route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Name and Email are required"}), 400

    users.append({"name": data["name"], "email": data["email"]})
    return jsonify({"message": "User registered successfully!"})

# Get Users Route
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)