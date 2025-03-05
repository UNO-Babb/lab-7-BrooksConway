#Problem3.py
#Project Euler problem 3
#Done
from NumberTests import isPrime
from NumberTests import Factors

def main():
  number = 13195
  factors = Factors(number)
  print(factors)

  for f in factors:
    if isPrime(f):  
      print(f)



if __name__ == '__main__':
  main()
