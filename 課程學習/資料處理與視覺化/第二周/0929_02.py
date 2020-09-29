import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("recent_grads_data/recent-grads.csv")

top_medians = df[df["Median"] < 40000].sort_values("Median").head()
top_medians.plot(x="Major", y=[ "Median"], kind="barh")
plt.show()