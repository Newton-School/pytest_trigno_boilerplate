
def factorial(n):
     #This will be required to find the cos and sin functions 
     if n < 0:
         return "Factorial of negative number doesn't exist"
     elif n == 0 or n == 1:
         return 1
     else:
         return n * factorial(n-1) 

def sin(x, n_terms=10):
    #Return value of sin(x) through Taylor series expansion upto n terms rounded to 2 decimal places.

def cos(x, n_terms=10):
    #Return value of cos(x) through Taylor series expansion upto n terms rounded to 2 decimal places.