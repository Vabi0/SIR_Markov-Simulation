import pandas as pd
import matplotlib.pyplot as plt

#load data from CSV
data = pd.read_csv("data.csv")

#calculate stats
total = data['Value'].sum()

count = data['Value'].count()

average = data['Value'].mean()

median = data['Value'].median()

std_dev = data['Value'].std()

maximum = data['Value'].max()

minimum = data['Value'].min()



print(f"Total: {total}, Count: {count}, Average: {average}")

print(f"Median: {median}, Std Dev: {std_dev}, Max: {maximum}, Min: {minimum}")



# Graphs

plt.hist(data['Value'], bins=10, color='skyblue', edgecolor='black')

plt.title("Distribution of Values")

plt.xlabel("Value")

plt.ylabel("Frequency")

plt.show()
