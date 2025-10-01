contacts = {
    'number': '4',
    'students': [
        { 'name': 'Adkins Macharia', 'email': 'admacharia18@gmail.com'},
        { 'name': 'John Doe', 'email': 'johndoe@example.com'},
        { 'name': 'Jane Smith', 'email': 'janesmith@example.com'},
        { 'name': 'Emily Davis', 'email': 'emilydavis@example.com'}
    ]
}

print('Students emails')
for student in contacts['students']:
    print (student['email'])