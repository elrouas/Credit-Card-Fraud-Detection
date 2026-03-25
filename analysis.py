import pandas as pd

# Load data
df = pd.read_csv("creditcard.csv")

# Data quality checks
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# Basic fraud analysis
fraud_rate = df["Class"].mean()
total_fraud = df["Class"].sum()

print("Fraud rate:", fraud_rate)
print("Total fraud cases:", total_fraud)

# Simple anomaly rule
df["alert"] = df["Amount"] > 1000

print("Number of alerts:", df["alert"].sum())