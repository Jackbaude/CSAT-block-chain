import time
from block import Block
  
class Chain():
    def __init__(self):
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_prevblock(self, index):
        return (self.blocks[index -1].hashBlock())

    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks),
                time.time(),
                data,
                self.get_prevblock(len(self.blocks) -1)))

    def verify_chain(self):
        for v in range(1 ,(len(self.blocks) -1)):
            if (self.blocks[v].hashBlock() != self.get_prevblock(v)):
                return False
            else:
                return True 
    
    def get_chain(self):
        chain = []
        for z in range(0, (len(self.blocks) -1)):
            chain.append(self.blocks[z].get_block())
        return chain
    def get_chain_length(self):
        return (len(self.blocks))



"""
chain = Chain()
chain.add_block("money given to jack")
time.sleep(0.5)
chain.add_block("money given to jack1")
time.sleep(0.5)
chain.add_block("money given to jack2")
chain.add_block("money given to jack3")
chain.add_block("money given to jack4")
chain.add_block("money given to jack5")
chain.add_block("money given to jack6")
chain.add_block("money given to jack7")
print("the length of the chain is {}". format(chain.get_chain_length()))
print(chain.get_chain())
print(chain.verify_chain())

"""