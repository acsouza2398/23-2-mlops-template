# Data
import pandas as pd

df = pd.read_csv("data/bank.csv")
df.sample(3)
dep_mapping = {"yes": 1, "no": 0}

# Convert the column to category and map the values
df["deposit"] = df["deposit"].astype("category").map(dep_mapping)

df = df.drop(labels = ["default", "contact", "day", "month", "pdays", "previous", "loan", "poutcome", "poutcome"], axis=1)

df.sample(3)

df.to_csv("data/bank_prepro.csv", index=False)

x = df.drop("deposit", axis=1)

x.to_csv("data/bank_predict.csv", index=False)