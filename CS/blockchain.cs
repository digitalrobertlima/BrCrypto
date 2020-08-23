using System;
using System.Collections.Generic;
using System.Text;

namespace Cripto
{
    class Blockchain
    {
        private List<Block> chain = new List<Block>();
        public const int DIFFICULTY_ADJUSTMENT = 10;
        public const int BLOCK_INTERVAL = 10;

        public Blockchain(Block genesisBlock)
        {
            chain.Add(genesisBlock);
        }
        public Block getLatestBlock()
        {
            return chain[-1];
        }

        public static String GetTimestamp(DateTime value)
        {
            return value.ToString("yyyyMMddHHmmssffff");
        }
        public void generateNextBlock(String data, int difficulty)
        {
            var previousBlock = getLatestBlock();
            int nextIndex = previousBlock.index + 1;
            String nextTimestamp = GetTimestamp(DateTime.Now);
            String nextPreviousHash = previousBlock.hash;
            Block newBlock = findBlock(nextIndex, nextPreviousHash, nextTimestamp, data, difficulty);
        }

        public Block findBlock(int index, string previousHash, int timestamp, string data, int difficulty)
        {
            int nonce = 0;
            while(true)
            {
                string hash = Block.calculateHash(index, previousHash, timestamp, data, difficulty, nonce);
                if(hashMatchesDifficulty(hash, difficulty))
                {
                    Block block = new Block(index, hash, previousHash, timestamp, data, difficulty, nonce);
                    return block;
                }
                nonce++;
            }
        }

        public Boolean hashMatchesDifficulty(string hash, int difficulty)
        {
            String hashBinary = StringToBinary(hash);
            String requiredPrefix = new string('0', difficulty);
            return hashBinary.StatsWith(requiredPrefix);
        }

        public int getDifficulty()
        {
            Block latestBlock = getLatestBlock();
            if (latestBlock.index % DIFFICULTY_ADJUSTMENT == 0 && latestBlock.index != 0)
            {
                return getAdjustedDifficukty();
            } else {
                return latestBlock.difficulty();
            }   }
        
        public int getAdjustedDifficulty()
        {
            Block latestBlock = getLatestBlock();
            Block prevAdjustmentBlock = chain[chain.Count - DIFFICULTY_ADJUSTMENT];
            int timeExpected = BLOCK_INTERVAL * DIFFICULTY_ADJUSTMENT;
            int timeTaken = Convert.ToInt32(latestBlock.timestamp) - Convert.ToInt32(prevAdjustmentBlock.timestamp);
            if (timeTaken < timeExpected *2)
            {
                return prevAdjustmentBlock.difficulty + 1;
            } else if (timeTaken > timeExpected * 2)
            {
                return prevAdjustmentBlock.difficulty - 1;
            } else
            {
                return prevAdjustmentBlock.difficulty;
            }
        }
    }
}