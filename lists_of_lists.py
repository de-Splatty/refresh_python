menu = [
    ["egg", "bread", "bacon"],
    ["chapati", "spinach", "beans"],
    ["roti", "potato", "carrot"]
]

print(menu[0][1])  # Output: bread

#dictionary of lists
subjects = {
    'compulsory_one': ["Math", "English", "kiswahili"],
    'compulsory_two': ["Biology", "Chemistry", "Physics"],
    'optional_one': ["Agriculture", "Art", "Music"],
    'optional_two': ["PE", "Health", "Computer Science"]
}

print("compulsory one subjects are: \t ,", subjects['compulsory_one'])
print("optional two subjects are: \t ,", subjects['optional_two'])

for name, sub in subjects.items():
    print(name, ":", sub)
    
#using dictionaries to represent objects

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person.get('name'), 'is', person.get('age'), 'years old and lives in', person.get('city'))