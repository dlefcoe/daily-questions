'''
Blockchain — The million-dollar buzzword. 
We’ve all heard the stories of overnight crypto riches. 
But will cryptocurrencies like Bitcoin (or blockchain, their underlying data structure) revolutionize the world?
Or will they remain a fascinating experiment in open-source?
Nobody can say for sure.


we will create functions to add blocks, transactions, and encryption so that our data’s tamper-proof.
Let’s dive in!

source:
https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531

'''



import hashlib
import json
from time import time

class Blockchain(object):
    ''' a Blockchain class '''

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash='some random hash comment from me', proof=100)

    def new_block(self, proof, previous_hash=None):
        '''
        create a new block
        
        inputs:
            proof: {str} this is a string
            previous_hash: the hash
        return:
            block: return the block
        '''

        block = {
            'index':len(self.chain) + 1, #the length of our blockchain and add 1 to it.
            'timestamp': time(), # stamp the block when it’s created
            'transactions': self.pending_transactions, # any transactions that are sitting in the ‘pending’ 
            'proof': proof, # a valid “nonce”, or “proof”
            'previous_hash': previous_hash or self.hash(self.chain[-1]) # a hashed version of the most recent approved block
        }

        self.pending_transactions = [] # when users send our coins to each other
        self.chain.append(block) # an empty list that we’ll add blocks to. Quite literally our ‘block-chain’.

        return block



    @property
    def last_block(self):
        ''' the last block '''
        return self.chain[-1]
    

    def new_transaction(self, sender, recipient, amount):
        """method with our three most important variables

        Args:
            sender ([type]): [description]
            recipient ([type]): [description]
            amount ([type]): [description]

        Returns:
            [type]: the last block
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.pending_transactions.append(transaction)


        return self.last_block['index'] + 1



    def hash(self, block):
        '''
        blockchains use SHA-256, an encryption hash function,
        which takes in some text string (stored as a Unicode value)
        and spits out a 64-character long encrypted string.
        '''

        # takes our new block and changes its key/value pairs all into strings
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode() # string into Unicode

        # create 64-character long encrypted string
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


def main():
    blockchain = Blockchain()
    t1 = blockchain.new_transaction('flef', 'juan', '5 possy coin')
    t2 = blockchain.new_transaction('juan', 'juepetto', '1 possy coin')
    t3 = blockchain.new_transaction('flef', 'big_jase', '1 possy coin')
    blockchain.new_block(12345)

    t4 = blockchain.new_transaction('flef', 'juan', '2 possy coin')
    t5 = blockchain.new_transaction('juan', 'big_jase', '1 possy coin')
    t6 = blockchain.new_transaction('juan', 'juepetto', '1 possy coin')
    blockchain.new_block(6789)

    print('blockchain:', blockchain.chain)


main()
