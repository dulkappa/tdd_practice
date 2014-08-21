import sys

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
  if sys.version_info[0] == 2:
    return not isinstance(n, bool) and \
      (isinstance(n, int) or isinstance(n, long) or isinstance(n, float) or isinstance(n, complex))
  else:
    return not isinstance(n, bool) and \
      (isinstance(n, long) or isinstance(n, float) or isinstance(n, complex))
