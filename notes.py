import pprint  # pretty print
def p(v):
    pprint.pprint(v, sort_dicts=False, width=60)
    
    
# Old way
list = []
for x in range(3):
    for y in range(3):
        list.append((x, y))
print(list)
# With list comprehension
new_list = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(new_list)

new_list = [
    [x for y in range(3)]
    for x in range(3)
]
print(new_list)





# REVIEW HOW THIS CODE WORKS
string = "Raphael Valderrama Torres"
letters_amount = 2
new_string = '.'.join([
    string[index:index + letters_amount]
    for index in range(0, len(string), letters_amount)
])
print(new_string)
