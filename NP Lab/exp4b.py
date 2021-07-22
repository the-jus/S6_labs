import time
from threading import Thread
def findsquare(nums):
    for i in nums:
        time.sleep(0.3)
        print(f"Square of {i}: {i*i}")

def fact(i):
    if i == 1:
        return 1
    else:
        return(i*fact(i-1))

def findfactorial(nums):
    for i in nums:
        time.sleep(0.2)
        print(f"Factorial of {i}: {fact(i)}")

nums = [1,2,3,4,5]

t = time.time()
t1 = Thread(target=findsquare, args=(nums,))
t2 = Thread(target=findfactorial, args=(nums,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Execution Finished, total time: ", time.time()-t)

