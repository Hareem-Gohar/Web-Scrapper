import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def fetch_and_save_data(site_name, url, parser_function):
    """
    Fetches data from a website using a custom parser function and saves it to a file.
    
    Args:
    - site_name (str): Name of the website for file naming.
    - url (str): Website URL to scrape.
    - parser_function (function): Custom function to parse the website's data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to load {url}. Status code: {response.status_code}")
        return

    print(f"Scraping {site_name}...")
    soup = BeautifulSoup(response.text, 'html.parser')
    data = parser_function(soup)

    if data:
        filename = f"{site_name}_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in data:
                file.write(entry + '\n')
        print(f"Data saved to {filename}")
    else:
        print(f"No data found for {site_name}.")

def parse_news_site(soup):
    """
    Parses article titles and image URLs from a news site.
    """
    articles = soup.find_all('main', id="main-content-area")
    data = []
    for article in articles:
        title = article.find('p', class_="article__subhead")
        img = article.find('img')
        title_text = title.text.strip() if title else "No title found"
        img_url = img['src'] if img and 'src' in img.attrs else "No image URL found"
        data.append(f"Title: {title_text}\nImage URL: {img_url}")
    return data


def parse_blog_site(soup):
    """
    Parses blog titles and their images from a blog site.
    """
    blogs = soup.find_all('span')  
    data = []
    for blog in blogs:
        title = blog.find('h3')
        img = blog.find('img')
        title_text = title.text.strip() if title else "No title found"
        img_url = img['src'] if img and 'src' in img.attrs else "No image URL found"
        data.append(f"Title: {title_text}\nImage URL: {img_url}")
    return data


def parse_ecommerce_site(soup):
    """
    Parses product names, prices, and image URLs from an e-commerce site.
    """
    products = soup.find_all('div', class_='_3n8fna1co')  
    data = []
    for product in products:
        name = product.find('div', class_='_58bkzq6c ')
        price = product.find('div', class_='_58bkzq6c ')
        img = product.find('img')
        name_text = name.text.strip() if name else "No name found"
        price_text = price.text.strip() if price else "No price found"
        img_url = img['src'] if img and 'src' in img.attrs else "No image URL found"
        data.append(f"Product: {name_text}\nPrice: {price_text}\nImage URL: {img_url}")
    return data

def parse_recipe_site(soup):
    """
    Parses recipe names and images from a recipe site.
    """
    recipes = soup.find_all('section', class_='comp')  
    data = []
    for recipe in recipes:
        name = recipe.find('span', class_='card__title-text')
        img = recipe.find('img')
        name_text = name.text.strip() if name else "No name found"
        img_url = img['src'] if img and 'src' in img.attrs else "No image URL found"
        data.append(f"Recipe: {name_text}\nImage URL: {img_url}")
    return data


# Example usage for multiple websites
websites = [
    {"site_name": "Aljazeera", "url": "https://www.aljazeera.com/news/", "parser": parse_news_site},
    {"site_name": "Blogger", "url": "https://www.blogger.com/about/?bpli=1", "parser": parse_blog_site},
    {"site_name": "Flipkart", "url": "https://www.flipkart.com/", "parser": parse_ecommerce_site},
    {"site_name": "AllRecipes", "url": "https://www.allrecipes.com/recipes/", "parser": parse_recipe_site},
]

for site in websites:
    fetch_and_save_data(site["site_name"], site["url"], site["parser"])
