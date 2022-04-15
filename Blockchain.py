import hashlib

class BitcoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = f"{'-'.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Noah sends 5 BTC to Mark"
t2 = "Mark sends 3.4 BTC to Trevor"
t3 = "Trevor sends 7.8 BTC to Jimmy"
t4 = "Jimmy sends 1.1 BTC to Noah"


block1 = BitcoinBlock('firstblock', [t1, t2])

print(f"Block 1 data: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")

block2 = BitcoinBlock('firstblock', [t3,t4])

print(f"Block 2 data: {block1.block_data}")
print(f"Block 2 hash: {block1.block_hash}")


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(BitcoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(BitcoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Data {i + 1}: {self.chain[i].block_data}\n")

    @property
    def last_block(self):
        return self.chain[-1]


t1 = "Noah sends 5 BTC to Mark"
t2 = "Mark sends 3.4 BTC to Trevor"
t3 = "Trevor sends 7.8 BTC to Neo"
t4 = "Neo sends 1.1 BTC to Noah"
t5 = "Noah sends 0.2 BTC to Diego"
t6 = "Diego sends 0.1 BTC to Billy"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()