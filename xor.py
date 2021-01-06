# Function to return 
# the nth XOR Fibonacci number  
def nthXorFib(n, a, b): 
    if n == 0 :  
        return a  
    if n == 1 :  
        return b  
    if n == 2 :  
        return a ^ b  
  
    return nthXorFib(n % 3, a, b)  
  
# Driver code  
a = 5
b = 11
n = 1000001
print(nthXorFib(n, a, b))  