# Python.org Tutorials

## Sources
[https://docs.python.org/3/tutorial/introduction.html](https://docs.python.org/3/tutorial/introduction.html)

*Note: probably going to use this only for information I did not know beforehand; also not taking notes on strings since that information won't be useful in an RL workspace*

Comments use #  
`//` operator is to floor a division expression (i.e. integer)  
**Control Flow Tools**
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

