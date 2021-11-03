n = int(input('what number would you like to start from?: ')) 
while True: 
  p = 1 
  nMultiples = []
  if n == 1 or n == 0:
    n = n + 1
  while p <= n: 
    if n % p == 0: 
      nMultiples.append(p)
    p = p + 1
  i = len(nMultiples)
  if i == 2: 
    print(f"{n} is a prime number")
  n = n + 1 
