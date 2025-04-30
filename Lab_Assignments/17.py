# 17.Write a program which will implement decorators for functions and methods in python.

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

class MyClass:
    @uppercase_decorator
    def say_hello(self):
        return "hello from method"

print(greet("jay")) 
obj = MyClass()
print(obj.say_hello())

