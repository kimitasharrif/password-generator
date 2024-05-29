from flask import Flask, render_template, request, jsonify
import random
import string
import re

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    # Simple example: Check if the password contains at least one uppercase letter, one lowercase letter, and one digit.
    if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
        return 'Strong'
    else:
        return 'Weak'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    try:
        length = int(request.form['length'])
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        password = generate_password(length)
        return jsonify({'password': password})
    except ValueError as e:
        return jsonify({'error': str(e)})

@app.route('/check_strength', methods=['POST'])
def check_strength_route():
    try:
        password = request.form['password']
        strength = check_password_strength(password)
        return jsonify({'strength': strength})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
