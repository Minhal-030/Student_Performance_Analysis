import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/StudentsPerformance.csv")

print(df.head())

print(df.info())

# Descriptive Statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Mean Scores ---")
print(df[['math score', 'reading score', 'writing score']].mean())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/StudentsPerformance.csv")

print(df.head())
print(df.info())

# Descriptive Statistics
print(df.describe())
print(df[['math score', 'reading score', 'writing score']].mean())


# GroupBy Analysis
print(df.groupby('gender')[['math score','reading score','writing score']].mean())

