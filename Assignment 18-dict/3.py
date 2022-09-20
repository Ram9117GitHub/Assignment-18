""" Write a python program to get a list of the values from a dictionary."""
dict1= {}
l = [1,2,3,4]
for x in l:
    print("Enter list of values :",x)
    dict1[x]=input()
print("Change list values dictionary = ",dict1)
"""""""""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Enter list of values : 1
ramkumar
Enter list of values : 2
18
Enter list of values : 3
male
Enter list of values : 4
98
Change list values dictionary =  {1: 'ramkumar', 2: '18', 3: 'male', 4: '98'}
"""