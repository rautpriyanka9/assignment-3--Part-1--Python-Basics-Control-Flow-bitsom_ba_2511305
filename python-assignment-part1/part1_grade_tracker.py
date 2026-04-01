
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

       # ================================
# Task 2 — Marks Analysis
# ================================

print("\n===== Task 2: Marks Analysis =====\n")

student_name = "Ayesha Sharma"

subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Student:", student_name)
print()

# -------- Print subject, marks, grade --------
for i in range(len(subjects)):
    m = marks[i]

    # grading logic
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], "-", m, "-", grade)


# -------- Total & Average --------
total = sum(marks)
average = round(total / len(marks), 2)

print("\nTotal marks:", total)
print("Average marks:", average)


# -------- Highest & Lowest --------
max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Highest:", subjects[max_index], "-", max_marks)
print("Lowest:", subjects[min_index], "-", min_marks)


# -------- While loop for new entries --------
count = 0

while True:
    subject = input("\nEnter subject (or type done): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # check numeric
    if not mark_input.isdigit():
        print("Invalid input! Enter number.")
        continue

    mark = int(mark_input)

    # check range
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        continue

    # add valid data
    subjects.append(subject)
    marks.append(mark)
    count += 1


# -------- Final output --------
print("\nNew subjects added:", count)

new_avg = round(sum(marks) / len(marks), 2)
print("Updated average:", new_avg)

print("\nMoving to Task 3...\n")

# ================================
# Task 3 — Class Performance Summary
# ================================

print("\nMoving to Task 3...\n")
print("===== Task 3: Class Performance Summary =====\n")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_avg_sum = 0

print("Name              | Average | Status")
print("----------------------------------------")

for name, marks in class_data:

    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # check topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # formatted row
    print(f"{name:<18} | {avg:>7} | {status}")

# class average
class_avg = round(total_avg_sum / len(class_data), 2)

print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Topper:", topper_name, "-", topper_avg)
print("Class Average:", class_avg)

# ================================
# Task 4 — String Manipulation Utility
# ================================

print("\n===== Task 4: String Manipulation Utility =====\n")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)

# Step 2: Title Case
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)

# Step 3: Count 'python'
count_python = clean_essay.count("python")
print("\n3. Count of 'python':", count_python)

# Step 4: Replace 'python'
replaced_text = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Text:")
print(replaced_text)

# Step 5: Split into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentences List:")
print(sentences)

# Step 6: Print numbered sentences
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]

    # ensure sentence ends with "."
    if not sentence.endswith("."):
        sentence = sentence + "."

    print(f"{i+1}. {sentence}")