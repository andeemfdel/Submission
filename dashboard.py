import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

# EDA
# relationship between weather and total users (df_day)
plt.figure(figsize=(10,6))
sb.barplot(x='weathersit', y='cnt', data=df_day)
plt.title('Relationship between Weather and Total Users')
plt.xlabel('Weather Condition')
plt.ylabel('Total Users')
plt.show()

#relationship between weather and total users (df_hour)
plt.figure(figsize=(10,6))
sb.barplot(x='weathersit', y='cnt', data=df_hour)
plt.title('Relationship between Weather and Total Users')
plt.xlabel('Weather Condition')
plt.ylabel('Total Users')
plt.show()

# calculating the correlation between temperature and total users (df_day)
correlation = df_day['temp'].corr(df_day['cnt'])
print('Corrrelation between temperature and total users:', correlation)

# calculating the correlation between temperature and total users (df_hour)
correlation = df_hour['temp'].corr(df_hour['cnt'])
print('Correlation between temperature and total users:', correlation)

# visualization and explanatory analysis
# question 1
# Load the cleaned datasets
df_day = pd.read_csv('day_cleaned.csv')
df_hour = pd.read_csv('hour_cleaned.csv')

# Group data by weather condition and calculate the average number of users
weather_effect_day = df_day.groupby('weathersit')['cnt'].mean()
weather_effect_hour = df_hour.groupby('weathersit')['cnt'].mean()

# Create bar plots for df_day and df_hour
plt.figure(figsize=(10, 6))
plt.bar(weather_effect_day.index, weather_effect_day.values)
plt.xlabel('Weather Condition')
plt.ylabel('Average Number of Users')
plt.title('Average Number of Users by Weather Condition (df_day)')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(weather_effect_hour.index, weather_effect_hour.values)
plt.xlabel('Weather Condition')
plt.ylabel('Average Number of Users')
plt.title('Average Number of Users by Weather Condition (df_hour)')
plt.show()

# question 2
# Group data by workingday and calculate the average number of users
weekday_effect_day = df_day.groupby('workingday')['cnt'].mean()
weekday_effect_hour = df_hour.groupby('workingday')['cnt'].mean()

# Create bar plots for df_day and df_hour
plt.figure(figsize=(10, 6))
plt.bar(weekday_effect_day.index, weekday_effect_day.values)
plt.xlabel('Working Day')
plt.ylabel('Average Number of Users')
plt.title('Average Number of Users by Working Day (df_day)')
plt.xticks([0, 1], ['Weekend', 'Weekday'])
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(weekday_effect_hour.index, weekday_effect_hour.values)
plt.xlabel('Working Day')
plt.ylabel('Average Number of Users')
plt.title('Average Number of Users by Working Day (df_hour)')
plt.xticks([0, 1], ['Weekend', 'Weekday'])
plt.show()

#advanced analysis
# assuming 'df' dataframe already concatenated (day & hour) and sorted by date
df['rental_date'] = pd.to_datetime(df['dteday']) 
recent_date = df['rental_date'].max()

# calculate the RFE for each user (assuming 'casual' + 'registered' = total users)
rfm_data = df.groupby('casual').agg(
    Recency=('rental_date', lambda x: (recent_date - x.max()).days),
    Frequency=('rental_date', 'count'),
    Engagement=('cnt', 'sum') 
)

# Combine and clean data (replace with your actual processing steps)
df = pd.concat([df_day, df_hour], ignore_index=True)
df['rental_date'] = pd.to_datetime(df['dteday'])
df.sort_values(by=['rental_date'], inplace=True)
df.set_index('rental_date', inplace=True)

# Time Series Plot
df['cnt'].plot(figsize=(12,6))
plt.title('Bike Rental Trend')
plt.ylabel('Total Users')
plt.show()
