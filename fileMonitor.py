import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from block import Block
from chain import Chain

chain = Chain()
log_file = open("../log_history.txt","w")
log_file.close()
class Event(LoggingEventHandler):
    def on_modified(self, event):
        mod = (f'event type: {event.event_type}  path : {event.src_path}')
    
        #adding everything to the log file
        log_file = open("../log_history.txt","w")
        log_file.write("{} \n\n\n".format(mod))
        log_file.close()
        
        #printing everything to the shell
        print (mod)
        chain.add_block(mod)
        print ("block chain length is {}".format(chain.get_chain_length()))
        print (chain.get_chain())
        print ("the chain is null: {}".format(chain.verify_chain()))
        
    def on_deleted(self, event):
        del_ = (f'event type: {event.event_type}  path : {event.src_path}')
        
        #adding everything to the log file
        log_file = open("../log_history.txt","w")
        log_file.write("{} \n\n\n".format(del_))
        log_file.close()
    
        #printing everything to the shell
        print (del_)
        chain.add_block(del_)
        print ("block chain length is {}".format(chain.get_chain_length()))
        print (chain.get_chain())
        print ("the chain is null: {}".format(chain.verify_chain()))
        
    def on_moved(self, event):
        mov = (f'event type: {event.event_type}  path : {event.src_path}')
        
        #adding everything to the log file
        log_file = open("../log_history.txt","w")
        log_file.write("{} \n\n\n".format(mov))
        log_file.close()
        
        #printing everything to the shell
        print (mov)
        chain.add_block(mov)
        print ("block chain length is {}".format(chain.get_chain_length()))
        print (chain.get_chain())
        print ("the chain is null: {}".format(chain.verify_chain()))
        
    def on_created(self, event):
        cre = (f'event type: {event.event_type}  path : {event.src_path}')
    
        #adding everything to the log file
        log_file = open("../log_history.txt","w")
        log_file.write("{} \n\n\n".format(cre))
        log_file.close()
        
        #printing everything to the shell
        print (cre)
        chain.add_block(cre)
        print ("block chain length is {}".format(chain.get_chain_length()))
        print (chain.get_chain())
        print ("the chain is null: {}".format(chain.verify_chain()))
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
     
     