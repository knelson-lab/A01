
# py -m pip install sklearn
from sklearn.datasets import fetch_california_housing # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load California Housing dataset
housing = fetch_california_housing(as_frame = True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# Generate boxplot for all features and target
df.boxplot(['MedInc', 'MedHouseVal'])
plt.savefig('./figs/boxplot.png')
