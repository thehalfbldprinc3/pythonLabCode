# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path to the dataset
file_path = "Toyota.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert relevant columns to numeric, handling errors gracefully
df['KM'] = pd.to_numeric(df['KM'], errors='coerce')   # Convert KM column to numeric
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')   # Convert HP column to numeric
df['Doors'] = pd.to_numeric(df['Doors'], errors='coerce') # Convert Doors column to numeric

# Set Seaborn style for better plot aesthetics
sns.set_style("whitegrid")

# ===========================
# 1. Distribution of Car Prices
# ===========================
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=30, kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

# ===========================
# 2. Price vs. Age of Cars
# ===========================
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Age'], y=df['Price'], alpha=0.6)
plt.title('Price vs. Age of Cars')
plt.xlabel('Age (months)')
plt.ylabel('Price')
plt.show()

# ===========================
# 3. Price Distribution by Fuel Type
# ===========================
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['FuelType'], y=df['Price'])
plt.title('Price Distribution by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.show()

# ===========================
# 4. Count of Cars by Fuel Type
# ===========================
plt.figure(figsize=(8, 5))
sns.countplot(x=df['FuelType'], palette='pastel')
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()