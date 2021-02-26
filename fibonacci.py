# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
#print(Fibonacci(i))

#Function for nth factorial number
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return None
    else:
        return n*recur_factorial(n-1)

# Driver Program
#print (recur_factorial(int()))