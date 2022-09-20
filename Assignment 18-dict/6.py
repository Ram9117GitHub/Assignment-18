"""Write a python program to create a dictionary that contains three dictionaries.(nested)"""

Dict1 = { 'Dict1': { },
         'Dict2': { }}
print("\n dictionary 1-")
print(Dict1)
Dict2 = { 'Dict1': {'name': 'Ali', 'age': '19'},
         'Dict2': {'name': 'Bob', 'age': '25'}
          ,'Dict3':{'Name':'Ram kumar','age':'19'}}
print("\n dictionary 2-")
print(Dict2)

Dict3 = { 'Dict1': {'name': 'Ali', 'age': '19'},
         'Dict2': {'name': 'Bob', 'age': '25'}
          ,'Dict3':{'Name':'Ram kumar','age':'19'}}

print("\n dictionary 3-")
print(Dict3)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
dictionary 1-
{'Dict1': {}, 'Dict2': {}}

 dictionary 2-
{'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}

 dictionary 3-
{'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}
"""
