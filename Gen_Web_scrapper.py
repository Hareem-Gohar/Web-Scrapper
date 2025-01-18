import requests
from bs4 import BeautifulSoup

# Function to scrape a website
def scrape_website(url, element, output_file):
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Page loaded successfully: {url}")
    else:
        print(f"Failed to load {url}. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = soup.find_all(element)
    
    if data:
        print(f"Data from {url}:")
        with open(output_file, 'w', encoding='utf-8') as file:
            for item in data:
                text = item.text.strip()
                print(text) 
                file.write(text + '\n')  
        print(f"Data saved to {output_file}")
    else:
        print(f"No data found on {url}")

# Example usage
scrape_website('https://en.wikipedia.org/wiki/Pakistan', "p", "output.txt")
