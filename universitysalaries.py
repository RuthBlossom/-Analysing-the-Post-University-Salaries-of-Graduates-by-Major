# -*- coding: utf-8 -*-
"""universitysalaries.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/RuthBlossom/2506a959b1567c5c448fa001df5d556e/universitysalaries.ipynb
"""

import pandas as pd

# Load the DataFrame
clean_df = pd.read_csv('/content/sample_data/salaries_by_college_major.csv')

# Display the first few rows to understand the structure
clean_df.head()

# Find the highest mid-career salary
highest_mid_career_salary = clean_df['Mid-Career Median Salary'].max()

# Find the index of the highest mid-career salary
index_highest_mid_career = clean_df['Mid-Career Median Salary'].idxmax()

# Find the college major with the highest mid-career salary
major_highest_mid_career = clean_df['Undergraduate Major'].loc[index_highest_mid_career]

print(f"The college major with the highest mid-career salary is {major_highest_mid_career}, earning ${highest_mid_career_salary}.")

# Find the lowest starting salary
lowest_starting_salary = clean_df['Starting Median Salary'].min()

# Find the index of the lowest starting salary
index_lowest_starting = clean_df['Starting Median Salary'].idxmin()

# Find the college major with the lowest starting salary
major_lowest_starting = clean_df['Undergraduate Major'].loc[index_lowest_starting]

print(f"The college major with the lowest starting salary is {major_lowest_starting}, earning ${lowest_starting_salary}.")

# Calculate the spread
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

# Insert the spread column into the DataFrame
clean_df.insert(1, 'Spread', spread_col)

# Display the first few rows to confirm the new column
clean_df.head()

# Sort by the 'Spread' column to find the lowest risk majors
low_risk = clean_df.sort_values('Spread')

# Display the top 5 low-risk majors
low_risk[['Undergraduate Major', 'Spread']].head()

# Sort by the 'Mid-Career 90th Percentile Salary' to find degrees with the highest potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)

# Display the top 5 degrees with the highest potential
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# Sort by the 'Spread' column in descending order to find the degrees with the greatest spread
greatest_spread = clean_df.sort_values('Spread', ascending=False)

# Display the top 5 degrees with the greatest spread
greatest_spread[['Undergraduate Major', 'Spread']].head()

# Group by 'Group' column and count the number of majors in each category
group_counts = clean_df.groupby('Group').count()

# Display the result
group_counts

import requests
from bs4 import BeautifulSoup

# Example URL (update with the actual URL you want to scrape)
url = 'https://www.payscale.com/college-salary-report'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extract data (this will vary based on the page structure)
salaries = soup.find_all('div', class_='salary-data-class')  # Update with the actual class or tag

# Process and print the extracted data
for salary in salaries:
    print(salary.text)

# Display the types of each column to identify numeric columns
clean_df.dtypes

# Select only numeric columns
numeric_cols = clean_df.select_dtypes(include='number')

# Group by 'Group' and calculate the mean for numeric columns only
group_mean_salaries = numeric_cols.groupby(clean_df['Group']).mean()

# Display the result
group_mean_salaries

# Find the lowest mid-career salary
lowest_mid_career_salary = clean_df['Mid-Career Median Salary'].min()

# Find the index of the lowest mid-career salary
index_lowest_mid_career = clean_df['Mid-Career Median Salary'].idxmin()

# Find the college major with the lowest mid-career salary
major_lowest_mid_career = clean_df['Undergraduate Major'].loc[index_lowest_mid_career]

print(f"The college major with the lowest mid-career salary is {major_lowest_mid_career}, earning ${lowest_mid_career_salary}.")