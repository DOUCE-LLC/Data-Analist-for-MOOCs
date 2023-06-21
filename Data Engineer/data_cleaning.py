import pandas as pd
import numpy as np

# Read the datasets
df1 = pd.read_csv('../Data/Raw Data/Coursera_courses.csv')
df2 = pd.read_csv('../Data/Raw Data/edx_courses.csv')
df3 = pd.read_csv('../Data/Raw Data/udemy_courses.csv')

# Functions

def remove_duplicates(dataframe):
    dataframe.drop_duplicates(inplace=True)
    return dataframe

def rename_columns(dataframe, column_map):
    dataframe = dataframe.rename(columns=column_map)
    return dataframe

def data_types(dataframe):
    for column in dataframe.columns:
        data_type = dataframe[column].dtype
        print(f"{column}: {data_type}")
    print('\n')

def column_to_int(dataframe, columns):
    for column in columns:
        if column == 'price':
            dataframe['price'] = dataframe['price'].str.lower()
            dataframe.loc[dataframe['price'].str.contains('free', na=False, case=False) & dataframe['paid'].isnull(), 'paid'] = False
        df[column] = df[column].replace(r'\D', '', regex=True)
        dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
        dataframe[column] = dataframe[column].fillna(np.nan).astype('Int64')
    return dataframe

def process_duration_column(column, df):
    # Fill missing values with an empty string
    df[column].fillna('', inplace=True)

    # Remove word 'Weeks' and spaces, convert to numeric, and multiply by 168
    df.loc[df[column].str.contains('Weeks', na=False), column] = df.loc[df[column].str.contains('Weeks', na=False), column].str.replace('Weeks', '').str.replace(' ', '').astype(float) * 168

    # Optional: Convert the column to numeric data type if needed
    df[column] = pd.to_numeric(df[column])

# Functions on action...

remove_duplicates(df1)
remove_duplicates(df2)
remove_duplicates(df3)

map1 = {'name': 'title', 'course_url': 'url', 'course_id': 'id'}
map2 = {'course_url': 'url', 'course_syllabus': 'curriculum', 'course_type': 'modality', 'Level': 'level', 'n_enrolled': 'n_subscribers', 'course_effort': 'effort', 'course_length': 'duration', 'course_description': 'description'}
map3 = {'course_title': 'title', 'course_id': 'id', 'num_subscribers': 'n_subscribers', 'content_duration': 'duration', 'num_reviews': 'n_reviews', 'num_lectures': 'n_lectures', 'is_paid': 'paid', 'published_timestamp': 'published'}

df1 = rename_columns(df1, map1)
df2 = rename_columns(df2, map2)
df3 = rename_columns(df3, map3)

df1['mooc'] = 'coursera'
df2['mooc'] = 'edx'
df3['mooc'] = 'udemy'

# Concatenate the DataFrames
df = pd.concat([df1, df2, df3], ignore_index=True)

to_int = ['n_subscribers', 'price', 'n_reviews', 'n_lectures']
df = column_to_int(df, to_int)

df.fillna(value=pd.NA, inplace=True)

process_duration_column('duration', df)

# Save DataFrame as a CSV file
df.to_csv('../Data/Data in Process/mooc-noWebScrapping.csv', index=False)
df.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/mooc-noWebScrapping.csv', index=False)