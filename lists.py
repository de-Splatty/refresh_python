# lists are created using square brackets []
# lists can contain any data type form empty list to list of strings to list of numbers to list of mixed items or even a list of lists

acronyms = ["KDF", "NTSA", "KRA", "NSSF", "NHIF"]
# lists are numbered starting from 0 index. so the code above has 5 items but the last item is at index 4
print(acronyms[0])  # prints KDF
# the nth item is at index n-1
print(acronyms[4])  # prints NHIF

students = []
students.append("Alice")
students.append("Bob")
students.append("Charlie")
print(students)  # prints ['Alice', 'Bob', 'Charlie']

#the append built-in function adds an item to the end of the list

acronyms.remove("KDF") # removes KDF from the list. remove method applies when you know the value of the item
del students[1] # removes the item at index 1. del statement applies when you know the index of the item

if "KRA" in acronyms:
    print("KRA is in the list") # checks if KRA is in the list and prints the message if true
else:
    print("KRA is not in the list")   
    
for acronym in acronyms:
    print(acronym) # prints each item in the list 