import multiprocessing 
  
def sender(conn, msgs): 
  
 for msg in msgs: 
     conn.send(msg) 
     print("Messages Sent: {}".format(msg)) 
 conn.close() 
  
def receiver(conn): 
  
 while 1: 
     msg = conn.recv() 
     if msg == 0: 
        break 
     print("Messages Received: {}".format(msg)) 

if __name__ == "__main__":

    msgs = [] 
    n = int(input("Enter dataset size: ")) 
    for i in range(n): 
        a = int(input("Enter the data: ")) 
        msgs.append(a) 
    
    
    parent_conn, child_conn = multiprocessing.Pipe() 
    
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))   
    
    p1.start() 
    p2.start() 
    
    
    p1.join() 
    p2.join()
