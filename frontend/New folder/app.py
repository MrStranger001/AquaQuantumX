from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# In-memory databases (for demo only)
users = {}
entangled_pairs = {}
messages = {}

# Simulate user login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if username not in users:
        users[username] = {'qubit': None}
    return jsonify({'message': f'Welcome, {username}!'}), 200

# Create entangled pair
@app.route('/entangle', methods=['POST'])
def entangle():
    user1 = request.json.get('user1')
    user2 = request.json.get('user2')
    pair_id = f'{user1}_{user2}'

    qubit_pair = {'id': pair_id, 'encoded': False, 'collapsed': False, 'bits': None}
    entangled_pairs[pair_id] = qubit_pair
    users[user1]['qubit'] = pair_id
    users[user2]['qubit'] = pair_id

    return jsonify({'status': 'Entangled pair established.', 'pair_id': pair_id})

# Alice encodes a message
@app.route('/send', methods=['POST'])
def send_message():
    sender = request.json.get('sender')
    message_bits = request.json.get('bits')  # 2-bit message, like '01'

    pair_id = users[sender]['qubit']
    pair = entangled_pairs.get(pair_id)

    if pair and not pair['collapsed']:
        pair['bits'] = message_bits
        pair['encoded'] = True
        messages[pair_id] = {'from': sender, 'bits': message_bits}
        return jsonify({'status': f'{sender} sent message: {message_bits}'})
    else:
        return jsonify({'error': 'No entangled pair or channel compromised'}), 400

# Simulate Eve (eavesdropper)
@app.route('/eavesdrop', methods=['POST'])
def eavesdrop():
    pair_id = request.json.get('pair_id')
    pair = entangled_pairs.get(pair_id)
    if pair:
        pair['collapsed'] = True
        return jsonify({'warning': 'Quantum state collapsed! Possible eavesdropping detected.'})
    return jsonify({'error': 'Pair not found'}), 404

# Bob receives the message
@app.route('/receive', methods=['POST'])
def receive():
    receiver = request.json.get('receiver')
    pair_id = users[receiver]['qubit']
    pair = entangled_pairs.get(pair_id)

    if pair:
        if pair['collapsed']:
            return jsonify({'status': 'WARNING: Quantum state collapsed! Possible eavesdropping detected.'})
        elif pair['encoded']:
            bits = pair['bits']
            return jsonify({'status': f'Message received: {bits}'})
        else:
            return jsonify({'status': 'Waiting for message...'})
    return jsonify({'error': 'No valid entangled pair found'}), 400

if __name__ == '__main__':
    app.run(debug=True)
