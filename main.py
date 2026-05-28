import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cars1.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

avg_co2 = df.groupby('Car')['CO2'].mean()

print("\nAVERAGE CO2 BY COMPANY")
print(avg_co2)

avg_co2.plot(kind='bar')

plt.title("Average CO2 Emission by Car Company")
plt.xlabel("Car Company")
plt.ylabel("Average CO2")

plt.show()

plt.scatter(df['Weight'], df['CO2'])

plt.title("Weight vs CO2")
plt.xlabel("Weight")
plt.ylabel("CO2")

plt.show()

plt.hist(df['CO2'])

plt.title("Distribution of CO2 Emissions")
plt.xlabel("CO2")
plt.ylabel("Number of Cars")

plt.show()