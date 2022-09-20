"""Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
"""
d ={}
list1 = [1,2,3,4]
list2 = ['ram','raj','ali','raju']
for key in list1:
    for value in list2:
        d[key]=value
        list2.remove(value)
        break
print(d)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""
"""
{1: 'ram', 2: 'raj', 3: 'ali', 4: 'raju'}
"""