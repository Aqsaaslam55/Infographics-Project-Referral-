import pandas as pd
import matplotlib.pyplot as plt

# Load the crime rates dataset
crime_data = pd.read_csv('US_Crime_Rates_1960_2014.csv')

# Filter the data for the year 2014
data_2014 = crime_data[crime_data['Year'] == 2014].iloc[0]

# Exclude 'Year' and 'Population' columns and sort by crime rates
crime_data_2014_sorted = data_2014.drop(['Year', 'Population']).sort_values(ascending=True)

# Select the five lowest crimes in 2014
bottom_5_crimes_2014 = crime_data_2014_sorted.head(5)

# Plotting the bar chart for the five lowest crimes in 2014
plt.figure(figsize=(12, 8))
bars = plt.bar(bottom_5_crimes_2014.index, bottom_5_crimes_2014.values, color='green', edgecolor='black')

# Adding numbers on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + height*0.02, f'{height:,.0f}', ha='center', va='bottom', color='black', fontweight='bold')


plt.xlabel('Crime Type', fontweight='bold')
plt.ylabel('Number of Crimes', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.grid(True)
plt.show()

# Filter the data for the year 2000
data_2014 = crime_data[crime_data['Year'] == 2014].iloc[0]

# Property and violent crimes
property_crimes = ['Burglary', 'Larceny_Theft', 'Vehicle_Theft']
violent_crimes = ['Murder', 'Forcible_Rape', 'Robbery', 'Aggravated_assault']

# Plotting the bar chart for property vs violent crimes in 2000
plt.figure(figsize=(12, 8))
bars_property = plt.bar(property_crimes, data_2014[property_crimes], color='blue', edgecolor='black', label='Property Crimes')
bars_violent = plt.bar(violent_crimes, data_2014[violent_crimes], color='red', edgecolor='black', label='Violent Crimes')

# Adding numbers on top of the bars for property crimes
for bar in bars_property:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + height*0.02, f'{height:,.0f}', ha='center', va='bottom', color='black', fontweight='bold')

# Adding numbers on top of the bars for violent crimes
for bar in bars_violent:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + height*0.02, f'{height:,.0f}', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Crime Type', fontweight='bold')
plt.ylabel('Number of Crimes', fontweight='bold')
plt.legend(loc='upper right')
plt.xticks(rotation=20, fontweight='bold')
plt.yticks( fontweight='bold')
plt.grid(True)
plt.show()


# Filter the data for the year 2014
data_2014 = crime_data[crime_data['Year'] == 2014].iloc[0]

# Exclude 'Year' and 'Population' columns and sort by crime rates
crime_data_2014_sorted = data_2014.drop(['Year', 'Population','Total']).sort_values(ascending=False)

# Select the top five highest crimes in 2014
top_5_crimes_2014 = crime_data_2014_sorted.head(5)

# Plotting the bar chart for the top five highest crimes in 2014
plt.figure(figsize=(12, 8))
bars = plt.bar(top_5_crimes_2014.index, top_5_crimes_2014.values, color='purple', edgecolor='black')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + height*0.02, f'{height:,.0f}', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Crime Type',fontweight='bold')
plt.ylabel('Number of Crimes',fontweight='bold')
plt.xticks( fontweight='bold')
plt.yticks( fontweight='bold')
plt.grid(True)
plt.show()




# Select a  crime categories for plotting
selected_crimes = ['Property', 'Larceny_Theft', 'Burglary', 'Violent','Aggravated_assault']

# Plotting the line chart for the selected crimes
plt.figure(figsize=(14, 8))
for crime in selected_crimes:
    plt.plot(crime_data['Year'], crime_data[crime], label=crime)

plt.xlabel('Year',fontweight='bold')
plt.ylabel('Number of Crimes',fontweight='bold')
plt.legend()
plt.xticks( fontweight='bold')
plt.yticks( fontweight='bold')
plt.grid(True)
plt.show()
