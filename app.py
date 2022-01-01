import os
from flask import jsonify, Flask

from blockchain.blockchain import Blockchain



app = Flask(__name__)


@app.route('/mine_block', methods=['GET'])
def mine_block():
    ''' Mining a new block '''
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations!, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200


# Getting the full blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    ''' Get current chain of block chain '''
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


# Checking if the blockchain is valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    ''' Checking blockchain is valid or not '''
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The blockchain is valid.'}
    else:
        response = {
            'message': 'We have a problem. The blockchain is not valid.'}
    return jsonify(response), 200


if __name__ == '__main__':

    # Creating a Blockchain
    blockchain = Blockchain()

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
