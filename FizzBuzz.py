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
  if is_python2():
    return not is_bool(n) and (is_int(n) or is_long(n) or is_float(n) or is_complex(n))
  else:
    return not is_bool(n) and (is_int(n) or is_float(n) or is_complex(n))

def is_bool(n):
  return isinstance(n, bool)

def is_int(n):
  return isinstance(n, int)

def is_long(n):
  return isinstance(n, long)

def is_float(n):
  return isinstance(n, float)

def is_complex(n):
  return isinstance(n, complex)

def is_python2():
  return True if sys.version_info[0]==2 else False
