import numpy as np
import pandas as pd
data={"name":['smith','alice','surya','david','rohit'],'maths':[80,67,91,59,45],'science':[90,85,95,64,76],'english':[68,79,87,34,50]}
df=pd.DataFrame(data)
print("_________Students Marks Data__________")
print(df)

df['total']=df[['maths','science','english']].sum(axis=1)
df['average']=df[['maths','science','english']].mean(axis=1)
print("total marks and average mark")
print(df)


def get_grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=85:
        return "A"
    elif avg >=80:
        return "B+"
    elif avg >=75:
        return "B"
    elif avg >=70:
        return "C+"
    elif avg >=65:
        return "C"
    elif avg >=60:
        return "D+"
    elif avg >=55:
        return "D"
    else:
        return "E"
df["grade"]=df["average"].apply(get_grade)
print("final report grade")
print(df)

print("\n📈 Analytics Report:")
print("Class Average Marks:", np.mean(df["average"]))
print("Highest Score:", df["total"].max(), "by", df.loc[df["total"].idxmax(), "name"])
print("Lowest Score:", df["total"].min(), "by", df.loc[df["total"].idxmin(), "name"])
print("\nGrade Distribution:")
print(df["grade"].value_counts())


df.to_csv("student_report.csv", index=False)
print("\n✅ Report saved to 'student_report.csv'")
