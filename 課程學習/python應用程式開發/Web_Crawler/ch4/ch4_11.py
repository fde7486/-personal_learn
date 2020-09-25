# ch4_11.py
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
name = ['王大','王二','王三','王四','王五']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame([chinese, eng, math, nature, social],
                  columns = course,
                  index = name)
print(df)






