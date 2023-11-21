#Basic function definition
#To define a function, you use the 'def' keyword
def function1():
    print('Hello world')

#Call it using the function name followed by the parantheses
function1()

# Function with params
def functionWithParams(name):
    # print(name)
    #To use in a string, wrap the parameter name in curly braces
    print(f'Welcome {name}')

functionWithParams('John')

#Function with default parameters
def functionWithDefaultParams(name = 'programmer'):
    print(f'Welcome {name}')

functionWithDefaultParams()
functionWithDefaultParams('Caroline')

#Function with return values
def functionWithReturn(num1, num2):
    return num1 + num2;

print(functionWithReturn(1,5))
# print(functionWithReturn(1,3))

#Pass is used as a placeholder to represent the code that will be later added to the function
def functionWithPass():
    pass

functionWithPass()