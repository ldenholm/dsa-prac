# kinda like json right
d = {"some_key": 1, "second_key": 4}
d1 = {1: 'this val has an int key', 2: 'wordtwo'}
d2 = {}

d2['laptop'] = 4000
print(d2)

# GET FUNCTION
print(d2.get('laptop'))
# we can call it with a custom error msg
print(d2.get('doesnt_exist'), 'key error')

# POP
print(d1.pop(2))

# POP ITEM
d1.pop
#UPDATING
d1[1] = 'new val'
print(d1.get(1))