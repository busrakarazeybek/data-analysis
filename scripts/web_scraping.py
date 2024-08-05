import requests
from bs4 import BeautifulSoup

def scrape_data(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data (example)
    data = []
    for item in soup.select('.data-item'):
        data.append({
            'title': item.select_one('.title').text,
            'value': item.select_one('.value').text
        })
    
    # Save data to CSV
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Data scraped and saved to {output_file}")

if __name__ == "__main__":
    scrape_data('https://example.com/data', 'data/raw/web_scraped_data.csv')
