#SYNTAX ERRORS
#These errors are a result of incorrect systax and are usually spotted by the Python interpreter

#Example1: Multiplying 2 by a * results in a syntax error:  2 * *
#Example2: print(Hello world)

#LOGIC ERRORS
#These errors are a result of an error in the logic of a code block. An example of this is when the programmer does not increment the count in a loop resulting in an infinite loop. 
#There are not usually spotted by the interpreter. The programmer has to find them manually.
#They dont crash the program

#Example: If the programmer intends to add two elements then divide by 2 i.e 2+4/2. The programmer expects a value of 3 but gets a value of 4. This can be corrected by wrapping the addition logic i.e (2+4) / 2

#EXCEPTIONS
#The python interpreter is able to read the rest of the application even if there is an exception

#1. AssertionError
#It arises when there is an error or exception inside an assert() statement. If true, there is no assertion error

#Example1: This following statement raises an AssertionError as the statement inside is incorrect:  assert(1 > 10)

#2. IndexError & KeyError
#IndexError occurs when trying to access an element from a sequence using an invalid index. 
#Example : Assume you have a list [1,2,3,4] and you are trying to access index 7

#KeyError occurs when trying to access an invalid key in a dictionary
#Example : Assume you have a dictionary {'key1':1, 'key2':2} and you try to access 'key4'

#3. NameError 
#occurs when trying a variable or a function that does not exist or is undefined

#4. TypeError
#occurs when trying to use a function on the wrong object 
#Example: sum = 5 + '10'