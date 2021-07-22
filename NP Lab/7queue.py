import multiprocessing 
  
def mult_ten(list, q): 
 print("Queue = list * 10") 
 for num in list: 
    q.put(num * 10) 
  
def print_queue(q): 
  
 print("Queue elements:") 
 while not q.empty(): 
    print(q.get()) 
  
  
if __name__ == "__main__":
        
    list= [] 

    n = int(input("Enter the datasize: ")) 
    for i in range(n): 
        a = int(input("Enter the data: ")) 
        list.append(a) 


    q = multiprocessing.Queue() 


    p1 = multiprocessing.Process(target=mult_ten, args=(list, q))  
    p2 = multiprocessing.Process(target=print_queue, args=(q,))   

    p1.start() 
    p1.join() 


    p2.start() 
    p2.join()
