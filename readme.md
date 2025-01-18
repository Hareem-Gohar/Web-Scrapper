# Web Scraping Projects

This repository contains basic web scraping projects using Python and the `BeautifulSoup` library. The scripts demonstrate how to fetch data from various websites and extract relevant information like titles, product details, and images.

## Project Structure

The project consists of multiple scraping scripts, each targeting different types of websites:

1. **Basic News Site Scraper**: Scrapes article titles from a news website.
2. **E-commerce Scraper**: Scrapes product details (name, price, image) from an e-commerce website.
3. **Recipe Scraper**: Extracts recipe names and images from a recipe website.
4. **Customizable Scraper**: A generic scraper that can be customized to scrape any website based on a provided parser function.

## Requirements

- Python 3.x
- Requests
- BeautifulSoup4

To install the required dependencies, use:

```bash
pip install requests beautifulsoup4
```

## Scripts Overview

### 1. **Basic News Site Scraper**

This script scrapes the titles from a news article page and saves them into a text file.

- **URL**: `'https://www.dawn.com/news/1882014'`
- **Data Extracted**: Article titles (subtitles)
- **Output**: `news_article_subtitles.txt`

### 2. **E-commerce Scraper**

Scrapes product details from an e-commerce site (e.g., Flipkart).

- **URL**: `'https://www.flipkart.com/audio-video/headset/pr?...'`
- **Data Extracted**: Product name, price, and image URL.
- **Output**: Customizable file with product information.

### 3. **Recipe Scraper**

Extracts recipe names and associated images from a recipe site.

- **URL**: `'https://www.allrecipes.com/recipes/'`
- **Data Extracted**: Recipe names and images.
- **Output**: Custom file with recipe information.

### 4. **Customizable Scraper**

A versatile scraper that can scrape any website. The script takes a URL and a custom parser function to extract relevant data.

### Example Usage:

```python
scrape_website('https://en.wikipedia.org/wiki/Pakistan', "p", "output.txt")
```

### **Fetch and Save Data**:

You can scrape data from multiple websites by defining the appropriate parser function for each one.

For example, the `parse_news_site`, `parse_blog_site`, `parse_ecommerce_site`, and `parse_recipe_site` functions can be used to handle different sites.
