def check_prime(n):
  num = int(round(n / 2 , 0))
  for i in range(2,num):
    if n % i == 0:
      return False
  return True

def main():
  i = 1
  while True:
    if i == 1:
      pass
    elif i == 2:
      print(2)
    elif i == 3:
      print(3)
    elif check_prime(i) == True:
      print(i)
    else:
      pass  
    i += 1

if __name__ == '__main__':
  main()
