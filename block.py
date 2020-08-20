import hashlib
import time
class Block:
    __init__(self, index, previousHash, timestamp, data, hash):
    self.index = index
    self.previousHash = previousHash
    self.timestamp = timestamp
    self.data = data
    self.hash = hash

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).hexdigest()

ts = int(round(time.time()*1000)) 

genesisBlock = Block(0, "", ts, "Genesis Block", calculateHash(0, "", ts, "Genesis Block"))
