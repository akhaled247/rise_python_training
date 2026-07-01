# Python.org Tutorials

## Sources
[https://docs.python.org/3/tutorial/introduction.html](https://docs.python.org/3/tutorial/introduction.html)

*Note: probably going to use this only for information I did not know beforehand; also not taking notes on strings since that information won't be useful in an RL workspace*

Comments use #  
`//` operator is to floor a division expression (i.e. integer)  
[**Control Flow Tools**](https://docs.python.org/3/tutorial/controlflow.html)
- List Operators: [Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) 
    - If `listB = listA`, `listB.append()` will affect `listA`; must use `listB = listA[:]` for separate copies
- For: `for n in nes` will return obj if nes is a list of objs
    - For loops should iterate over a copy of items if making edits to them
    - Iterate over indices `for i in range(len(a))`
        - Range functions return `iterable` which can be used in other functions
- Break/Continue: `break` will break out of a repeating loop, while `continue` will stay within that loop but move on to the next iteration of it
- Pass: `pass` is used for creating empty functions, classes, etc.
- Functions: Default argument values can be assigned in the function declaration:   
`def fun(test="TEST", example=3.14159, program=boston_university.rise)`  
    - Keyword arguments: When dealing with optional variables, you can assign either positionally (like normal) or with a `kwarg=value`:  
    `fun(example=809, test="DEPLOY")` will be the same as `fun("DEPLOY", 809)`  
- Lambdas: Creatd using the `lambda arg1, arg2, argN: cmd` syntax
- Dictionaries: `{key: value}` pair
**Syntax**
- 4-space indentation w/o tabs
- Wrap lines <= 79 chars
- Blank lines between functions/classes
- Comments on separate lines, docstrings
- `UpperCammelCase` for classes and `lowercase_with_underscores` for functions/methods
**Modules**
- Modules are their way of talking about files, or scripts
- Packages
```
sound/                          Top-level package
    __init__.py               Initialize the sound package
    formats/                  Subpackage for file format conversions
        __init__.py
        wavread.py
        wavwrite.py
        ...
    effects/                  Subpackage for sound effects
        __init__.py
        echo.py
        ...
    .../
```
[**Classes**](https://docs.python.org/3/tutorial/classes.html)

*Background Terminology*
- Namespace: Mapping from names to objects
- Attribute: In `modname.funcname`, `funcname` is the attribute; read or read/write; not all attributes are variables, can also be functions with a `return`
- Scope: Where a namespace is directly accessible without more references
    - Name assignments go to innermost scope, but `global` assigns to global scope and `nonlocal` increases scope by one level.
    - Priority is inversely related to scope (i.e. `local` highest, `global` lowest)
*Class Structure*
- Instantiation: When a new instance of a class is created, it calls the `__init__` function
- Method Objects: Can store functions within attributes (e.g. `hello = class.hello()`) and can be called at any time in the program
- Writing a class:
```python
class MyClass:
    var = "foo" # class variable (all instances)

    def __init__(self, var2):
        self.var2 = var2 # instance variable

    def fun(self, arg):
        return self.var2 + arg # instance vars are stored within each instance, acccessed separately

    __fun = fun # Private attribute

class DerivedClass(MyClass): # analogous to `classB extends classA` in Java
    #Inherited classes can use `super()` and are connected to base class
    def fun(self, arg):
        # changes here will not affect `__fun`
```