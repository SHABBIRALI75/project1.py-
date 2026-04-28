import pandas as pd

class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = None

    def check_status(self):
        average = (self.math_score + self.science_score) / 2
        if average >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"


df = pd.read_csv("raw_grades.csv")
df = df.fillna(0)  # replace blanks with 0

# convert scores to int
df["Math_Score"] = df["Math_Score"].astype(int)
df["Science_Score"] = df["Science_Score"].astype(int)

students = []

for index, row in df.iterrows():
    student = Student(row["Student_Name"], row["Math_Score"], row["Science_Score"])
    student.check_status()

    students.append({
        "Student_Name": student.name,
        "Math_Score": student.math_score,
        "Science_Score": student.science_score,
        "Status": student.status
    })

final_df = pd.DataFrame(students)
final_df["School_Year"] = "2023-2024"

final_df.to_csv("final_grades.csv", index=False)

print(" final_grades.csv created successfully!")