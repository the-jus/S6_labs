
wt = 1
re = 1
n1 = int(input("Enter readers: "))
n2 = int(input("Enter writers: "))
read = [0] * n1
write = [0] * n2
count=0
    
while(1):
    ch = int(input("\n\nREADER 1  WRITER 2: "))
    if(ch==1):
        id = int(input("Enter reader: "))
        action= int(input("REQUEST 1 OR HALT 2: "))
        if(action==1):
            re=re-1
            if(re<0):
                print("READER "+str(id)+"CANNOT READ")
                read[id]=1
                
            else:
                wt=wt-1
                read[id]=2
                re=re+1
                
            
        else:
            count=count-1
            if(count==0):
                wt = wt+1
            wt=wt+1
            read[id]=0
                    
                   
        
    else:
        id = int(input("Enter writer: "))
        action= int(input("REQUEST 1 OR HALT 2: "))
        if(action==1):
            wt=wt-1
            if(wt<0):
                 print("WRITER "+str(id)+" CANNOT WRITE")
                 write[id]=1
           
            else:
                write[id]=2
        else:
            write[id]=0
            wt=wt+1
            
        
        
        

    print("........READERS..........\n")

    for i in range(n1):
            if(read[i]==2):
                count=count+1
                print("Reader "+str(i)+" is READING")

    for i in range(n1):
            print(read[i],end=' ')
    
    print("\n........WRITERS............\n")

    for i in range(n2):
            if(write[i]==2):
                print("Writer "+str(i)+" is Writing")
    
    for i in range(n2):
            
            print(+write[i],end=' ')
                    
        
        
        

        
        
        
        
                
            
        
        


    
