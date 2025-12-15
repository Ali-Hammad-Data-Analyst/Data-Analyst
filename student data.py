import pandas as pd

# Data
data = {
    "name": [
        "Ahmed", "Ali", "Hammad", "Ahsan", "Bilal",
        "Hassan", "Hussain", "Umer", "Usman", "Yahya",
        "Zaid", "Hamza", "Daniyal", "Ibrahim", "Ismail",
        "Imran", "Talha", "Khalid", "Saad", "Salman",
        "Rayan", "Rehan", "Faisal", "Farhan", "Noman",
        "Shahzaib", "Shahmeer", "Arham", "Ayaan", "Ammar",
        "Hashir", "Huzaifa", "Junaid", "Kamil", "Kamran",
        "Moiz", "Naveed", "Rayyan", "Suleman", "Usaid",
        "Yasir", "Zubair", "Zeeshan", "Taha", "Sameer",
        "Jibran", "Arslan", "Furqan", "Sarim", "Azlan"
    ],
    "class": [
        "10th","9th","8th","7th","6th"] * 10,
    "marks": [
        85, 90, 78, 88, 92,
        75, 69, 95, 80, 77,
        91, 84, 73, 89, 67,
        96, 82, 79, 88, 94,
        72, 90, 85, 68, 93,
        81, 76, 87, 95, 70,
        89, 83, 78, 91, 74,
        86, 92, 80, 69, 88,
        75, 84, 97, 66, 90,
        82, 79, 85, 93, 71
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# User input
name = input("Enter student name: ")

# Search student
student = df[df["name"].str.lower() == name.lower()]

if student.empty:
    print("No record found for this name.")
else:
    marks = student.iloc[0]["marks"]

    if marks >= 85:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f" Name: {student.iloc[0]['name']}")
    print(f" Marks: {marks}")
    print(f" Grade: {grade}")
