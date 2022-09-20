"""Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
"""
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
other_dict = {"Dict1":Dict1,
            "Dict2":Dict2,
            "Dict3":Dict3}
print(other_dict) 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""Ourtput"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
"""
dictionary 1-
{'Dict1': {}, 'Dict2': {}}

dictionary 2-
{'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}

dictionary 3-
{'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}
{'Dict1': {'Dict1': {}, 'Dict2': {}}, 'Dict2': {'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}, 'Dict3': {'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}, 'Dict3': {'Name': 'Ram kumar', 'age': '19'}}}
"""
