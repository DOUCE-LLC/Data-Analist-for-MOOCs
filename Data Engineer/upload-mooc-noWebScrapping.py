import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

# Load the environment variables from the file
load_dotenv('credentials.env')

# Get the password from the environment variable
password = os.getenv('PASSWORD')

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="mooc"
)

# Read the CSV file using pandas
data = pd.read_csv('../Data/Data in Process/mooc-noWebScrapping.csv')

# Create a cursor object
cursor = connection.cursor()

# Iterate over the rows of the DataFrame and insert into the table
for _, row in data.iterrows():
    sql = "INSERT INTO your_table (title, institution, url, id, mooc, summary, n_subscribers, modality, instructors, level, subject, language, subtitles, effort, duration, price, description, curriculum, paid, n_reviews, n_lectures, published) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = tuple(row)
    cursor.execute(sql, values)

# Commit the changes and close the connection
connection.commit()
connection.close()
