def fizzbuzz(num):
  if is_numeric(num):
    if num%15 == 0:
      return "FizzBuzz"
    elif num%3 == 0:
      return "Fizz"
    elif num%5 == 0:
      return "Buzz"
    else:
      return num
  else:
    return "Error!"

def is_numeric(n):
  return not isinstance(n, bool) and \
  (isinstance(n, int) or isinstance(n, long) or isinstance(n, float) or isinstance(n, complex))
