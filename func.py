#When it comes to functions, Python uses the def keyword to define a function.
# in functions order matters. so one should define a function before calling it.


def greeting(name):
    print("Hello,", name)

#main program 
input_name = input("Enter your name: \n")
greeting(input_name) #function call with argument

# a variable created inside a function is local to that function and cannot be accessed outside of it.
# for example in code above name is local to greeting function.
# a variable created outside a function is global and can be accessed inside the function.

def addition(a, b):
    return a + b

def main():  
    num1 = int(input("Enter first number: \n"))
    num2 = int(input("Enter second number: \n"))
    result = addition(num1, num2)
    print("The sum is:", result)

main()
 #why use functions?
#1. Code Reusability: Functions allow you to reuse code without rewriting it.
#2. Improved Readability: Functions can make your code more organized and easier to read.
#3. Easier Maintenance: Functions allow you to isolate changes to a specific section of code.