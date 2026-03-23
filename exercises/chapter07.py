#1 Start by importing pandas with the alias pd.
import pandas as pd

#2 Import the dataset as a dataframe named df from this url: 
# https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv"
df = pd.read_csv(url)
print(df)

#3 How many rows and columns are there in the dataframe?
print(df.shape)

#4 What is the type of data in each column of df?
print(df.map(type))
print(df.info())    # another solution

#5 What is the mean co2_emmission of the whole dataset?
print("Task 5:")
print(df["co2_emmission"].mean())

#6 How many different kinds of foods are there in the dataset? How many countries are in the dataset?
print(f"There are {df['food_category'].nunique()} foods.")
print(f"There are {df['country'].nunique()} countries.")

#7 What is the maximum co2_emmission in the dataset and which food type and country does it belong to?
print(df.iloc[df['co2_emmission'].idxmax()])

#8 How many countries produce more than 1000 Kg CO2/person/year for at least one food type?
print(df.query("co2_emmission > 1000"))

#9 Which country consumes the least amount of beef per person per year?
print(df.query("food_category == 'Beef'").sort_values(by="consumption").head(1))

#10 Which country consumes the most amount of soybeans per person per year?
print(df.query("food_category == 'Soybeans'").sort_values(by="consumption", ascending=False).head(1))

#11 What is the total emissions of all the meat products (Pork, Poultry, Fish, Lamb & Goat, Beef) in the dataset combined?
meat = ['Poultry', 'Pork', 'Fish', 'Lamb & Goat', 'Beef']
print(df["co2_emmission"][df['food_category'].isin(meat)].sum())

#12 What is the total emissions of all other (non-meat) products in the dataset combined?
print(df["co2_emmission"][~df['food_category'].isin(meat)].sum())