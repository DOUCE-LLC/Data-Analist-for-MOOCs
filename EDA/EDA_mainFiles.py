import pandas as pd
import ydata_profiling as ydata

# Read the datasets
df1 = pd.read_csv('../Data/Raw Data/Coursera_courses.csv')
df2 = pd.read_csv('../Data/Raw Data/edx_courses.csv')
df3 = pd.read_csv('../Data/Raw Data/udemy_courses.csv')
# df4 = pd.read_pickle('../Data/Raw Data/Coursera_reviews.pkl')

# Perform EDA using pandas_profiling
profile1 = ydata.ProfileReport(df1)
profile2 = ydata.ProfileReport(df2)
profile3 = ydata.ProfileReport(df3)
# profile4 = ydata.ProfileReport(df4)

# Export as HTML
profile1.to_file('../Web/Routes/Coursera_courses.html')
profile2.to_file('../Web/Routes/edx_courses.html')
profile3.to_file('../Web/Routes/udemy_courses.html')
# profile4.to_file('../Web/Routes/Coursera_reviews.html')