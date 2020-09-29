import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
import numpy as np


bins = 20
boston = datasets.load_boston()
X_boston = boston.data
# print(boston.feature_names)
# print(X_boston)

X_sepal = X_boston[:, 2]

# plt.hist 把某個 feature 的所有數值(X_sepal)跟要切成幾個區段(bins)給他，就能畫直方圖
plt.hist(X_sepal, bins)
plt.title("Histogram Sepal Length")
plt.xlabel(boston.feature_names[0])
plt.ylabel("Frequency")
plt.show()