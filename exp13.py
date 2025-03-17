import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "Toyota.csv"
df = pd.read_csv(file_path)


df['KM'] = pd.to_numeric(df['KM'], errors='coerce')
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')
df['Doors'] = pd.to_numeric(df['Doors'], errors='coerce')


sns.set_style("whitegrid")


plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=30, kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Age'], y=df['Price'], alpha=0.6)
plt.title('Price vs. Age of Cars')
plt.xlabel('Age (months)')
plt.ylabel('Price')
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(x=df['FuelType'], y=df['Price'])
plt.title('Price Distribution by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.show()


plt.figure(figsize=(8, 5))
sns.countplot(x=df['FuelType'], palette='pastel')
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()
