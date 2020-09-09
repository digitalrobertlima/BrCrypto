from Block import *
from Transaction import *
from Main import *
from ecdsa import SiigningKey, NIST384p

def getBalance(address, listUnspentOutput):
    balance = 0
    for utxo in listUnspentOutput:
        if utxo.address == address:
            balance = balance + utxo.amount
    return balance

def verifyingAmounts(amount, userListUtxo):
    currentAmount = 0
    finalListUtxo = []
    for utxo in userListUtxo:
        finalListUtxo.append(utxo)
        currentAmount = currentAmount + utxo.amount
        if currentAmount >= amount: