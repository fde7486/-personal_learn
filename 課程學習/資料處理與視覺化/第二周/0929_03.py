import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 讀取 seaborn 裡內建的範例資料集
lol = pd.read_csv("lol_data/high_diamond_ranked_10min.csv")
sns.displot(data = lol, x="blueWins", col="redCSPerMin", kde=True)
plt.show()
