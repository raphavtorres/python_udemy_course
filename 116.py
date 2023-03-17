"""
Closure and functions that return other functions (recursion)
"""


def create_greeting(greeting):  # Greeting has to remembered but name is dynamic
    def greet(name):
        return f'{greeting} {name}!'
    return greet


g1 = create_greeting('Good Morning')
g2 = create_greeting('Good evening ')

print(g1('Luiz'))
print(g2('Luiz'))

"""
Doubts: 
    What's call stack?
    Python needs to execute the internal function to finish the external??
"""

