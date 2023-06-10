"""
list toire te must ListName=[....] use krte hbe.

"""

subjects=["Math","Physics","Chemistry","Programming"]
'''print(len(subjects)) #len use to check the length of the list.lenght starts from 1'''
subjects.append("ICS") #listname.append use to add something in list
'''subjects.insert(2,"OS")#listname.insert use to add something in list manualy'''
'''subjects.remove("Chemistry") #listname.remove use to remove something from subjects'''
'''subjects.sort() #listname.sort use for sorting from ascending mannerr
subjects.reverse() #listname.reverse use for sorting from discending mannerr'''
'''subjects.pop() #listname.pop use korle list er sesh er item take tule niye bakigulo show hbe'''
'''subjects.clear() #to clear the list'''
subjects2=subjects.copy() #copy from one list to another

pos=subjects.index("Chemistry") #kono list er item koto number e ase ta janar jnno
print(subjects)
print(pos)
coun=subjects2.count("Math") #list e kono item kotobar ase ta janar jnno
print(subjects2)
print(coun)