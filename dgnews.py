import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_news(keyword, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)  # Set a timeout value
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

    soup = BeautifulSoup(response.content, 'html.parser')

    # Your actual scraping logic here
    articles = []
    for item in soup.find_all('article'):
        title_element = item.find('h2')
        link_element = title_element.find('a') if title_element else None
        if title_element and link_element:
            title = title_element.text.strip()
            link = link_element['href']
            if keyword.lower() in title.lower():
                articles.append({
                    'Keyword': keyword,
                    'Title': title,
                    'Link': link,
                })
    return pd.DataFrame(articles)

# List of keywords to scrape
keywords = ['Gervalla', 'Gervalles', 'MPJD', 'Donika', 'Schwarz']

# List of websites to scrape
websites = [
    {'name': 'nacionale', 'url': 'https://nacionale.com'},
    {'name': 'telegrafi', 'url': 'https://telegrafi.com'},
    {'name': 'indeksonline', 'url': 'https://indeksonline.com'},
    {'name': 'klankosova', 'url': 'https://klankosova.tv'},
    {'name': 'koha', 'url': 'https://koha.net'},
    {'name': 'gazetaexpress', 'url': 'https://gazetaexpress.com'},
    {'name': 'botasot', 'url': 'https://botasot.info'},
    {'name': 'gazetablic', 'url': 'https://gazetablic.com'},
    {'name': 'insajderi', 'url': 'https://insajderi.com'},
    {'name': 'zeri', 'url': 'https://zeri.info'},
    {'name': 'kohavision', 'url': 'https://kohavision.tv'},
    {'name': 'kosovapress', 'url': 'https://kosovapress.com'},
    {'name': 'gazetajnk', 'url': 'https://gazetajnk.com'},
    {'name': 'gazetafjala', 'url': 'https://gazetafjala.com'},
    {'name': 'tribunaonline', 'url': 'https://tribunaonline.com'},
    {'name': 'epokaere', 'url': 'https://epokaere.com'},
    {'name': 'rtv21', 'url': 'https://rtv21.tv'},
    {'name': 'lajmi', 'url': 'https://lajmi.net'},
    {'name': 'infopress', 'url': 'https://infopress.tv'},
    {'name': 'kosova-sot', 'url': 'https://kosova-sot.info'},
    {'name': 'kosova24', 'url': 'https://kosova24.info'},
    {'name': 'top-channel', 'url': 'https://top-channel.tv'},
    {'name': 'syri', 'url': 'https://syri.net'},
    {'name': 'demokracia', 'url': 'https://demokracia.com'},
    {'name': 'albanianpost', 'url': 'https://albanianpost.com'},
]

while True:
    all_news = pd.DataFrame()

    for site in websites:
        for keyword in keywords:
            news_data = scrape_news(keyword, site['url'])
            if not news_data.empty:  # Check if news_data is not empty
                all_news = pd.concat([all_news, news_data], ignore_index=True)

    if not all_news.empty:
        styled_table = all_news.style.set_table_styles([
            {'selector': 'tr:hover', 'props': [('background-color', '#ffff99')]},
            {'selector': 'th', 'props': [('background-color', '#f2f2f2')]},
            {'selector': 'td', 'props': [('border', '1px solid #dddddd')]}
        ])

        with open('news_table.html', 'w') as file:
            file.write(styled_table.to_html(render_links=True, escape=False))

        print("News data updated and saved.")
        print(all_news)

    time.sleep(60)
