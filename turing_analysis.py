# turing_analysis.py

import pandas as pd

# 1. Importing the CSV file (cardio_base)
cardio_base = pd.read_csv("cardio_base.csv")

# 2. Count smokers among men and women
men_smokers_count = ((cardio_base['gender'] == 1) & (cardio_base['smoking'] == 0)).sum()
women_smokers_count = ((cardio_base['gender'] == 2) & (cardio_base['smoking'] == 0)).sum()

if men_smokers_count > women_smokers_count:
    print("Men smoke more.")
elif men_smokers_count < women_smokers_count:
    print("Women smoke more.")
else:
    print("Men and women smoke equally.")

# 3. Percentage of people >2 std deviations above average height
avg_height = cardio_base['height'].mean()
std_dev_height = cardio_base['height'].std()
threshold = avg_height + (2 * std_dev_height)
num_above_threshold = (cardio_base['height'] > threshold).sum()
percentage_above_threshold = (num_above_threshold / len(cardio_base)) * 100
print(f"Percentage of people more than 2 standard deviations away from the average height: {percentage_above_threshold}")

# 4. People over 50 who consume alcohol (merged_df assumed to exist)
# merged_df = pd.read_csv("your_merged_df.csv") # Uncomment and set your actual filename
# For demonstration, this block is commented out until you have merged_df available
# over_50_alcohol_consumers = merged_df[(merged_df['age'] > 50) & (merged_df['alco'] == 1)]
# num_over_50_alcohol_consumers = over_50_alcohol_consumers.shape[0]
# print("Number of people over 50 who consume alcohol:", num_over_50_alcohol_consumers)

# 5. Percentage of people over 50 who drink alcohol
# over_50 = merged_df[merged_df['age'] > 50]
# num_alcohol_consumers = (over_50['alco'] == 1).sum()
# total_over_50 = over_50.shape[0]
# percentage_alcohol_consumers = (num_alcohol_consumers / total_over_50) * 100
# print(f"Percentage of people over 50 who drink alcohol: {percentage_alcohol_consumers}%")

# 6. Cholesterol: Over 50 vs Under 50
cholesterol_over_50 = cardio_base.loc[cardio_base['age'] > 50, 'cholesterol'].mean()
cholesterol_below_50 = cardio_base.loc[cardio_base['age'] <= 50, 'cholesterol'].mean()
percentage_difference = ((cholesterol_over_50 - cholesterol_below_50) / cholesterol_below_50) * 100
print(f"The percentage difference in cholesterol levels between people over 50 and the rest is {percentage_difference}%.")

# 7. Cholesterol: Smokers vs Non-Smokers (merged_df required)
# smokers_cholesterol = merged_df.loc[merged_df['smoke'] == 1, 'cholesterol'].mean()
# non_smokers_cholesterol = merged_df.loc[merged_df['smoke'] == 0, 'cholesterol'].mean()
# if smokers_cholesterol > non_smokers_cholesterol:
#     print("Smokers have higher cholesterol levels than non-smokers.")
# elif smokers_cholesterol < non_smokers_cholesterol:
#     print("Non-smokers have higher cholesterol levels than smokers.")
# else:
#     print("Smokers and non-smokers have the same cholesterol levels.")

# 8. COVID data: 3rd highest death rate (covid_data required)
# covid_data = pd.read_csv("covid_data.csv") # Uncomment and set your actual filename
# covid_data = covid_data.sort_values(['location', 'date'])
# covid_data['cumulative_deaths'] = covid_data.groupby('location')['new_deaths'].cumsum()
# covid_data['death_rate'] = (covid_data['cumulative_deaths'] / covid_data['population']) * 1e6
# sorted_data = covid_data.sort_values(by='death_rate', ascending=False)
# if sorted_data['location'].nunique() >= 3:
#     third_highest_country = sorted_data['location'].unique()[2]
#     print(third_highest_country)
# else:
#     print("Insufficient data to determine the 3rd highest death rate.")

# 9. COVID data: Italy subset, days passed (covid_data required)
# italy_data_subset = covid_data[
#     (covid_data['location'] == "Italy") &
#     (covid_data['date'] >= "2020-02-28") &
#     (covid_data['date'] <= "2020-03-20")
# ].copy()
# italy_data_subset['days_passed'] = (
#     pd.to_datetime(italy_data_subset['date']) - pd.to_datetime("2020-02-28")
# ).dt.days
# print(italy_data_subset)

# NOTE: For sections involving merged_df or covid_data, ensure you load those DataFrames with the appropriate CSV or merge logic before running those blocks.
