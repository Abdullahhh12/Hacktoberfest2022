import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website you want to scrape
url = 'https://www.example.com/news'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements that contain the news article titles and links
    article_elements = soup.find_all('div', class_='news-article')

    # Create empty lists to store the scraped data
    titles = []
    links = []

    # Iterate through the article elements and extract the data
    for article in article_elements:
        title = article.find('h2').text
        link = article.find('a')['href']
        titles.append(title)
        links.append(link)

    # Create a DataFrame to store the scraped data
    data = {'Title': titles, 'Link': links}
    df = pd.DataFrame(data)

    # Output the scraped data to a CSV file
    df.to_csv('news_articles.csv', index=False)

    print('Data scraped and saved to news_articles.csv.')
else:
    print('Failed to retrieve the web page.')

