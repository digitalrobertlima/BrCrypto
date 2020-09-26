const SHA256 = require('crypto-js/sha256');

class Transactions{
    constructor(fromAddress, toAddress, amount)
}

class Block{
    constructor(timestamp, transactions, previousHash = ''){
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nonce = 0;
    }

    calculateHash(){
        return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.transactions) + this.nonce).toString();
    }

    mineBlock(difficulty){
        while(this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")){
            this.nonce++;
            this.hash = this.calculateHash();
        }

        console.log("Hash do Bloco Minerado: " + this.hash);
    }
}


class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];
        this.difficulty = 5;
    }

    createGenesisBlock(){
        return new Block("24/09/2020", "Genesis Block", "0");
    }

    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }

    addBlock(newBlock){
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.mineBlock(this.difficulty);
        //newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock);
    }

    isChainValid(){
        for(let i = 1; i < this.chain.length; i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1 ];

            if(currentBlock.hash !== currentBlock.calculateHash()){
                return false;
            }

            if(currentBlock.previousHash !== previousBlock.hash){
                return false
            }
        }

        return true;
    }
}

let brCoin = new Blockchain();

console.log('Minerando Bloco 1...');
brCoin.addBlock(new Block(1, "24/09/2020", {amount: 4}));
console.log('Minerando Bloco 2...');
brCoin.addBlock(new Block(2, "24/09/2020", {amount: 10}));
console.log('Minerando Bloco 3...');
brCoin.addBlock(new Block(2, "24/09/2020", {amount: 1}));

//console.log('Is Blockchain valid? ' + brCoin.isChainValid());
//brCoin.chain[1] transactions = { amount:100};
//console.log('Is Blockchain valid? ' + brCoin.isChainValid());
//console.log(JSON.stringify(brCoin, null, 4));
