import pandas as pd
import ydata_profiling as ydata

# Read the datasets
df = pd.read_csv('../Data/Data in Process/mooc-noWebScrapping.csv')

# Perform EDA using pandas_profiling
profile = ydata.ProfileReport(df)

# Export as HTML
profile.to_file('../Web/Routes/mooc-noWebScrapping.html')