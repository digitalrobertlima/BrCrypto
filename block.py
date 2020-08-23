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

def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
 return hashlib.sha256(str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).enconde('UTF-8').hexdigest()

ts = int(round(time.time()*1000)) 

genesisBlock = Block(0, "", ts, "Genesis Block", calculateHash(0, "", ts, "Genesis Block"))

def hashMatchesDifficulty(self, hash, difficulty):
    hashBinary = binascii.unhexlify(hash)
    requiredPrefix = '0'*int(difficulty)
    return hashBinary.startswith(requiredPrefix)

def findBlock(self, index, previousHash, timestamp, data, difficulty):
    nonce = 0
    while True:
        hash = self.calculateHash(index, previousHash, timestamp, data, difficulty, nonce)
        if self.hashMatchesDifficulty(hash, difficulty):
            block = Block(index, previousHash, timestamp, data, difficulty, nonce)
            return block
        nonce = nonce + 1

def getDifficulty(self):
    latestBlock = self.getLatestBlock()
    if latestBlock.index % self.DIFFICULTY_ADJUSTMENT == 0 and latestBlock.index != 0:
        return self.getAdjustedDifficulty()
    else:
        return latestBlock.difficulty

def getAdjustedDifficulty(self):
    prevAdjustmentBlock = self.blockchain[len(self.blockchain) - self.DIFFICULTY_ADJUSTMENT]
    timeExpected = self.BLOCK-INTERVAL * self.DIFFICULTY_ADJUSTMENT
    timeTaken = latestBlock.timestamp - prevAdjustmentBlock.timestamp
    if timeTaken < timeExpected * 2:
        return prevAdjustmentBlock.difficulty + 1
    elif timeTaken > timeExpected * 2:
    return prevAdjustmentBlock.difficulty - 1
    else:
        return prevAdjustmentBlock.difficulty
