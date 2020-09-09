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
            leftover = currentAmount - amount
            return leftover, finalListUtxo

def creatingInput(unspentOutput):
    input = Input()
    input.outputId = unspentOutput.outputId
    input.outputIndex = unspentOutput.outputIndex
    return input

def creatingOutputs(addressTo, addressFrom, amount, leftover):
    output1 = Output(addressTo, amount)
    if leftover == 0:
        return output1
    else:
        leftoverTx = Output(addressFrom, leftover)
        return output1, leftoverTx

unsignedInputs = []

def createTransaction(addressTo, addressFrom, amount, leftOver key):
    transaction = Transaction()
    transaction.inputs = unsignedInputs
    transaction.outputs = creatingOutputs(addressTo, addressFrom, amount, leftOver)

inptIndex = 0
    for inpt in transaction.inputs:
        inpt = signingInput(transaction, inptIndex, transaction.output)
        inptIndex = inptIndex + 1