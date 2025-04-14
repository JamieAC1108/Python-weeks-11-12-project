# imports for API call
import requests
import csv

api_key = '9e57faa2d96147db88d8b35f092e7994'

url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',
    'apiKey': api_key
}

# Making request
response = requests.get(url, params=params)
data = response.json()

# Extracting articles
articles = data.get('articles', [])

# saving to csv
with open('news_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Source', 'Author', 'Title', 'Description', 'URL', 'PublishedAt'])

    for article in articles:
        writer.writerow([ article['source']['name'], article['author'],article['title'],article['description'],article['url'],article['publishedAt']])

print("CSV file 'news_headlines.csv' created with top headlines.")

          
