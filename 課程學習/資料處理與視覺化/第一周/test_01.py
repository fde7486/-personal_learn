import numpy as np
import pandas as pd

# a = np.array([1, 2, 3])
# print(type(a))
# print(a.shape, end = '\n\n')

# b = np.array([[1,2,3],[4,5,6]])
# print(type(b))
# print(b.shape)


# df = pd.DataFrame({
#     "Name": ["Jerry", "Mary", "Tom"], 
#     "Age": [25, 29, 30], 
#     "Sex": ["male", "female", "male"]}
#     )
# print(type(df))
# print(df.describe())

titanic = pd.read_csv("titanic_data/train.csv")
male = titanic[titanic["Sex"] == "male"]
age51 = male[male["Age"] > 50]

titanic.loc(age51[:,2]) = 50

print(age51)