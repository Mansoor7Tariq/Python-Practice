# In Python, a lambda function is a special type of function without the function name. For example,

# lambda: print('Lambda')

# lambda argument(s) : expression
# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned

# ------ simple lambda function


def greet(): return print('Hello World')


greet()

# ------- lambda funtion with argunment


def greet_user(name): return print('Hey there,', name)


greet_user('Mansoor')

# ---------

namesArr = ['ahmed', 'umair', 'junaid', 'tom', 'mansoor']

namesArr.sort()
print('names ->', namesArr)

# with lambda function According to length with key

namesArr.sort(key=lambda x: len(x))
print('names ->', namesArr)
