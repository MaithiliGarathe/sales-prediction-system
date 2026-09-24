import os
import numpy as np
import pandas as pd

np.random.seed(42)

n = 200

TV = np.random.uniform(0, 300, n)
Radio = np.random.uniform(0, 50, n)
Newspaper = np.random.uniform(0, 120, n)

Sales = (
    2.5
    + 0.045 * TV
    + 0.20 * Radio
    + 0.01 * Newspaper
    + np.random.normal(0, 1.5, n)
)

data = pd.DataFrame({
    "TV": TV,
    "Radio": Radio,
    "Newspaper": Newspaper,
    "Sales": Sales
})

os.makedirs("data", exist_ok=True)

data.to_csv("data/advertising.csv", index=False)

print("Dataset created successfully!")
print("Saved to: data/advertising.csv")
print(data.head())