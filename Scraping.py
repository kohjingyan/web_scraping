import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

try:
    # Send GET request
    source = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets')
    
    # Check if url is valid
    source.raise_for_status()
    
    # Parse HTML text
    soup = BeautifulSoup(source.text, 'html.parser')
    
    # Scrape the prices
    prices = soup.find_all('h4', class_="pull-right price")
    price = []
    for content in prices:    
        price.append(content.text.split("$")[1])
    
    # Scrape the product names
    titles = soup.find_all('h4')
    name = []
    for title in titles:
        texts = title.find('a')
        if texts:
            name.append(texts.text)
    
    # Scrape the description of the product
    descriptions = soup.find_all('p', class_ = "description")
    description = []
    for content in descriptions:
        description.append(content.text)
    
    # Scrape the number of reviews
    reviews = soup.find_all('p', class_="pull-right")
    review = []
    for content in reviews:
        text = content.text.split()[0]
        review.append(text)
    
    # Scrape the number of stars ratings
    ratings = soup.find_all('p', attrs={'data-rating':True})
    rating = []
    for p in ratings:
        rating.append(p['data-rating'])
    
    df = pd.DataFrame({'Name': name,
                       'Price': price,
                       'Description': description,
                       'no_of_reviews': review,
                       'no_of_ratings': rating})

except Exception as e:
    print(e)

df