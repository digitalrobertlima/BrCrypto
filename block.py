import hashlib
import time
import binascii

class Block:
    __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
    self.index = index
    self.previousHash = previousHash
    self.timestamp = timestamp
    self.data = data
    self.hash = hash
    self.difficulty = difficulty
    self.nonce = nonce

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).enconde('UTF-8').hexdigest()

ts = int(round(time.time()*1000)) 

genesisBlock = Block(0, "", ts, "Genesis Block", calculateHash(0, "", ts, "Genesis Block"))

def hashMatchesDifficulty(self,hash, difficulty):
    hashBinary = binascii.unhexlify(hash)
    requiredPrefix = '0'*int(difficulty)
    return hashBinary.startswith(requiredPrefix)

def findBlock