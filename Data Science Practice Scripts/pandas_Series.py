import numpy as np
import pandas as pd

country = ["India", "USA", "Arab", "Egypt", "UK"]
c = pd.Series(country)
print(c)    # dtype for strings are refered as object here

marks = [80, 90, 70, 77, 89, 98]
m = pd.Series(marks)
print(m)

# Custom index
subject = ["eng", "maths", "science", "history", "hindi", "marathi"]
s = pd.Series(marks, index = subject)
print(s)

# Setting a name
arbazMarks = pd.Series(marks, index = subject, name = "Arbaz's Marks")
print(arbazMarks)


# Creating series from dict
AKmarks = {
    "eng": 80,
    "maths": 90,
    "hindi": 88
}
print(pd.Series(AKmarks))