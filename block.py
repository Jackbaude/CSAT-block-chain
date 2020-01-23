import hashlib
import time
class Block():
    #constructor for each block
    #data is abstarct and can be anything
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
    #hash the block inorder to add it to the chain
    def hashBlock(self):
        key = hashlib.sha256()
        key.update(str(self.index) +
               str(self.timestamp) +
               str(self.data) +
               str(self.previous_hash).encode('utf-8'))

        return key.hexdigest()

    def get_block(self):
        return [self.index, self.timestamp, self.data, self.previous_hash]



#test
block = Block(0, time.time(), "john is fat", 0000)
#print(block.hashBlock())
