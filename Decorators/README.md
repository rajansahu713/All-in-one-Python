## Python Decorators.

### Decorators
* A decorator is a special type of function that can change the default behavior of a function.
* Decorators can be used to add additional functionality to a function or method, such as caching, logging, or authentication, without actually changing the original code.
* A decorator is essentially a wrapper function that takes in another function as an argument and returns a new function that adds additional functionality to the original function. Decorators are typically used to simplify code, make it more modular, and reduce the amount of boilerplate code that is required.


#### To understand how decorators work in Python.

* Suppose when a method for two number division
```python
def twoNumberDevision(a, b):
    print(a/b)
```

* If i called the method with a=3 and b=0, then what will happen 
```
ERROR!
Traceback (most recent call last):
  File "<string>", line 4, in <module>
  File "<string>", line 2, in twoNumberDevision
ZeroDivisionError: division by zero
```
* We will get above error.
* So lets build a decorator that can tackle this problem.

```python
def checkParams(func):
    def inner(a, b):
        if b == 0:
            print("b should not be zero")
            return

        return func(a, b)
    return inner

@checkParams
def twoNumberDevision(a, b):
    print(a/b)
```

* As you can we have wrote a decorators for `checkParams` decorators.
* After puting decorator on method, from now when ever we can the function first it will check the parameter weather it is in corret format or not then it will execute the method.

```
twoNumberDevision(6,3)
>> 2.0

twoNumberDevision(6,0)
>> b should not be zero
```