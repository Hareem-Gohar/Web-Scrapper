import requests
from bs4 import BeautifulSoup

def scrape_news_site(url, output_file):
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Page loaded successfully: {url}")
    else:
        print(f"Failed to load {url}. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find_all('h2')
    
    if titles:
        print("Article SubTitles:")
        with open(output_file, 'w', encoding='utf-8') as file:
            for title in titles:
                title_text = title.text.strip()
                print(title_text)  
                file.write(title_text + '\n')  
        print(f"Article titles saved to {output_file}")
    else:
        print("No article titles found.")

# Example usage
output_filename = "news_article_subtitles.txt"  
scrape_news_site('https://www.dawn.com/news/1882014', output_filename)
