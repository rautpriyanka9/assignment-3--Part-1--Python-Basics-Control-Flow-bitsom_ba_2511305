
# Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# store cleaned data
cleaned_students = []

# loop through students
for student in raw_students:

    # clean name
    name = student["name"].strip().title()

    # convert roll to integer
    roll = int(student["roll"])

    # convert marks string to list
    marks_list = student["marks_str"].split(",")
    marks = []

    for m in marks_list:
        marks.append(int(m.strip()))

    # validate name
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    if valid:
        print("✓ Valid name:", name)
    else:
        print("✗ Invalid name:", name)

    # print profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

    # store cleaned student
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })


# find student with roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSpecial Output:")
        print(s["name"].upper())
        print(s["name"].lower())