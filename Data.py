student = [
    {"Name": "Eugene", "Age": 18, "City": "London", "Subjects": ["Math", "Physics", "English"]},
    {"Name": "Joseph", "Age": 19, "City": "London", "Subjects": ["Math", "Biology", "Chemistry"]}
]

for s in student:
    print(f"{s['Name']} (Age {s['Age']}) studies: {', '.join(s['Subjects'])}")