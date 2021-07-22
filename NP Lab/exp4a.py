import os
def driver():
  n = os.fork()
  if n > 0:
    print("Parent process : ", os.getpid())
  else:
    print("Child process : ", os.getpid())

driver()
