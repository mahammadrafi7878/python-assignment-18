#6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
#we dont have OrderdDictionary in pytho , it is available in collections module,.
from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
for key,value in od.items():
    print(key,value ,end=' ')
#print same but not printed as dict
