#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"] #column names

df = pd.read_csv("C:\\Users\\coryw\\OneDrive\\Documents\\random code\\Chicken\\magic04.data", names = cols) #read the data in, set the cols to the correct names
df["class"] = (df["class"] == "g").astype(int) #change g/h class to 1/0
print(df.head()) #preview the data

#%%

for label in cols[:-1]:
  plt.hist(df[df["class"]==1][label], color='blue', label='gamma', alpha=0.7, density=True)
  plt.hist(df[df["class"]==0][label], color='red', label='hadron', alpha=0.7, density=True)
  plt.title(label)
  plt.ylabel("Probability")
  plt.xlabel(label)
  plt.legend()
  plt.show()

# %%
