import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

df = pd.read_csv('../Data/Data in Process/mooc-noWebScrapping.csv')

df['rating'] = ''

counter = 0

invalid_url = []

for index, row in df.iterrows():
    if row['mooc'] == 'coursera':
        url = row['url']
        print(url)

        pattern = r"https://www.coursera.org/learn/(.*)"
        match = re.match(pattern, url)

        if match:
            course_title = match.group(1)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            if course_title in response.url:
                main = soup.find('main')
                
                if main:
                    div1 = main.find('div', id='main')
                    div1a = div1.find('div', class_='_iul6hq')
                    ratingSpan = div1a.find('span', class_='_16ni8zai')
                    rating = ratingSpan.text
                    rating = rating.replace('stars', '')
                    print(rating)
                    df.at[index, 'rating'] = rating
            else:
                invalid_url.append(url)
        else:
            invalid_url.append(url)
        counter += 1
        print('counter:', counter)
        print(' ')

    elif row['mooc'] == 'udemy':
        url = row['url']
        print(url)

        pattern = r"https://www.udemy.com/(.*)"
        match = re.match(pattern, url)

        if match:
            course_title = match.group(1)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            if course_title in response.url:
                div1 = soup.find('div', class_='course-landing-page__main-content dark-background-inner-text-container')
                if div1:
                    div1a = div1.find('div', class_='clp-lead__badge-ratings-enrollment')
                    rating_string = div1a.find('span', class_='ud-sr-only')
                    rating = re.findall(r'\d+\.\d+', rating_string.text)
                    if rating:
                        rating = rating[0]
                        print(rating)
                        df.at[index, 'rating'] = rating
            else:
                invalid_url.append(url)
        else:
            invalid_url.append(url)
        counter += 1
        print('counter:', counter)
        print(' ')

df.to_csv('../Data/Cleaned Data/webScrapping.csv', index=False)

with open("../Data/Invalid Data/invalid_urls.txt", "w") as file:
    for item in invalid_url:
        file.write(str(item) + "/n")