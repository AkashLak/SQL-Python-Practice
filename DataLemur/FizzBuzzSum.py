def fizz_buzz_sum(target):
  
  total = 0

  for i in range(target):
    if i % 3 == 0 or i % 5 == 0:
      total += i
      
  return total
