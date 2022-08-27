#7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
# default dict doesnot give key error it also available in collections modue,if we have empty vale of key then it automatically fill it.
from collections import defaultdict
def first_value():
    return "not present"
dict_of_lists=defaultdict(first_value)
dict_of_lists['a'] ='something for a'
print(dict_of_lists['a'])
print(dict_of_lists['b'])
# it does not give key error here.