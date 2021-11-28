from uuid import uuid4
from flask import Flask,jsonify, request

from blockchain import Blockchain

app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = uuid4().hex

# Instantiate the Blockchain
blockchain = Blockchain()
app.config['SERVER_NAME'] = 'myblockchain.com'  # needed to use subdomains

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)