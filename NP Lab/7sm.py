import multiprocessing
 
def mult_ten(list, result, ssum):
 
 
 for idx, num in enumerate(list):
  result[idx] = num * 10
 ssum.value = sum(result)
 print("Result(in process p1): {}".format(result[:]))
 print("Sum of squares(in process p1): {}".format(ssum.value))
 
if __name__ == "__main__":
 
 list = []
 n = int(input("Enter the datasize: "))
 for i in range(n):
  a = int(input("Enter the data: "))
  list.append(a)
 result = multiprocessing.Array('i', n)
 ssum = multiprocessing.Value('i')
 p1 = multiprocessing.Process(target=mult_ten, args=(list, result, ssum))
 p1.start()
 p1.join()
 print("Result(in main program): {}".format(result[:]))
 print("Sum of squares(in main program): {}".format(ssum.value))