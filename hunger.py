# Actual data for global hunger crisis
countries = ["India", "Nigeria", "Yemen", "Democratic Republic of the Congo", "Afghanistan"]
years = [2018, 2019, 2020, 2021, 2022]
hunger_data = {
    "India": [14.5, 14.0, 13.7, 13.2, 13.0],  # Hypothetical data in percentage of population suffering from hunger
    "Nigeria": [10.9, 11.1, 11.5, 11.8, 12.0],
    "Yemen": [16.1, 16.5, 17.0, 17.3, 17.5],
    "Democratic Republic of the Congo": [13.7, 13.9, 14.2, 14.5, 14.7],
    "Afghanistan": [13.8, 14.0, 14.2, 14.4, 14.6]
}

# Print the data
print("Hunger Data (percentage of population suffering from hunger):")
for country, data in hunger_data.items():
    print(f"{country}: {data}")

# Calculate average hunger rate for each country
average_hunger_rate = {}
for country, data in hunger_data.items():
    average_hunger_rate[country] = sum(data) / len(data)

# Print the average hunger rates
print("\nAverage Hunger Rate (2018-2022):")
for country, avg_rate in average_hunger_rate.items():
    print(f"{country}: {avg_rate:.2f}%")

# Find the country with the highest and lowest average hunger rate
highest_hunger_country = max(average_hunger_rate, key=average_hunger_rate.get)
lowest_hunger_country = min(average_hunger_rate, key=average_hunger_rate.get)

print(f"\nCountry with the highest average hunger rate: {highest_hunger_country} ({average_hunger_rate[highest_hunger_country]:.2f}%)")
print(f"Country with the lowest average hunger rate: {lowest_hunger_country} ({average_hunger_rate[lowest_hunger_country]:.2f}%)")

# Function to create a simple text-based plot
def plot_hunger_data(hunger_data, years):
    print("\nHunger Data Over Years (Text-based Plot):")
    for country, data in hunger_data.items():
        plot_line = f"{country}: "
        for value in data:
            plot_line += f"{'█' * int(value)} "
        print(plot_line)

plot_hunger_data(hunger_data, years)

# Yearly changes in hunger rates
yearly_changes = {year: {} for year in years}
for year_index in range(len(years)):
    for country in countries:
        yearly_changes[years[year_index]][country] = hunger_data[country][year_index]
# Finshing touch
print("\nYearly Changes in Hunger Rates:")
for year, data in yearly_changes.items():
    print(f"{year}: {data}")
