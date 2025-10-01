acronym = {
    "IDK": "I don't know",
    "BRB": "Be right back", 
    "LOL": "Laugh out loud",
}
 #the items in the dictionary are key-value pairs

print(acronym["IDK"])  #to look up a value in the dictionary, use the key inside square brackets
#dictionaries can comprise of different data types

sentence = 'IDK' + ' what to do. ' + 'BRB' + ', I will figure it out. ' 
translation = acronym.get('IDK' + ' what to do. ' + 'BRB' + ', I will figure it out.')

subjects = {}

subjects["Math"] = 90
subjects["English"] = 85
subjects["Science"] = 95
subjects["History"] = 80
print(subjects)  #prints the whole dictionary

subjects["Math"] = 95  #to change a value, use the key inside square brackets and assign a new value
print(subjects)

del subjects["History"]  #to delete a key-value pair, use the del keyword followed by the dictionary name and the key inside square brackets
print(subjects)

#if we try to access a key that does not exist, we get a KeyError
#print(subjects["Geography"]) #uncommenting this line will raise a KeyError

marks = subjects.get("Geography")  #to avoid KeyError, use the get() method which returns None or a default value if the key does not exist

if marks:
    print("Geography marks:", marks)
else:
    print("Geography marks not found")
    






#keys must be unique and immutable (cannot be changed)
#dictionaries are unordered, meaning the items do not have a defined order

#dictionaries are mutable, meaning you can change them