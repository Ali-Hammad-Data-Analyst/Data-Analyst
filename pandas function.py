import pandas as pd

data = {
    "name": ["Ahmed", "Ali", "Hammad"],
    "class": ["10th", "9th", "8th"],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# -------------------------
# Function to Add a Row
# -------------------------
def add_row(df, name, class_, marks):
    new_row = {"name": name, "class": class_, "marks": marks}
    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# -------------------------
# Function to Remove a Row
# -------------------------
def remove_row(df, name):
    return df[df["name"] != name]

# -------------------------
# Function to Add a Column
# -------------------------
def add_column(df, col_name, values):
    df[col_name] = values
    return df

# -------------------------
# Function to Remove a Column
# -------------------------
def remove_column(df, col_name):
    return df.drop(columns=[col_name])


# -------------------------
# Testing the functions
# -------------------------

print("Original DataFrame:")
print(df)

# Add Row
df = add_row(df, "Bilal", "7th", 92)
print("\nAfter Adding Row:")
print(df)

# Remove Row
df = remove_row(df, "Ali")
print("\nAfter Removing Row:")
print(df)

# Add Column
df = add_column(df, "grade", ["A", "B", "A"])
print("\nAfter Adding Column:")
print(df)

# Remove Column
df = remove_column(df, "grade")
print("\nAfter Removing Column:")
print(df)