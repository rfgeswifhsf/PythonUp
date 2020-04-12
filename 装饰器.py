from functools import  wraps
def debug(func):
    @wraps(func)
    def wrapper():
        print('[DEBUG]:enter {} ()'.format(func.__name__))
        return func
    return wrapper

@debug
def say_hello():
    print('hello')

'''
MULTATION
'''
def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))
# Output: [1]

print(add_to(2,add_to(1)))
# Output: [2]

print(add_to(3))
# Output: [3]
