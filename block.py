import hashlib
import time
class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        
        

    def hashBlock(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        key.hexdigest()
        return key
        
        
        
        
block = Block(0, time.time(), "john is fat", 0000)
print(str(block.hashBlock().encode('utf-8')))