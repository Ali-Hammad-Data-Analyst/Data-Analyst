import pandas as pd

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
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th",
        "10th","9th","8th","7th","6th"
    ],
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

df = pd.DataFrame(data)

# ------------ Condition ------------
user_name = input("Enter name: ")

# search ignoring uppercase/lowercase
result = df[df["name"].str.lower() == user_name.lower()]

if not result.empty:
    print("\nRecord Found!")
    print(result[["name","class","marks"]])
else:
    print("\nNo record found for this name..")
