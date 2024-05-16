import requests
from bs4 import BeautifulSoup

def scrape_news(keyword, url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout value (e.g., 10 seconds)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    # Your existing scraping logic here
    # ...
    return articles

    # Extract relevant information (date, title, link)
    # Example code:
    # dates = soup.find_all('span', class_='date')
    # titles = soup.find_all('h2', class_='title')
    # links = soup.find_all('a', class_='link')

    # Create a DataFrame to store the data
    # news_data = pd.DataFrame({
    #     'Date & Time': dates,
    #     'Title': titles,
    #     'Link': links,
    #     'Keyword': [keyword] * len(dates)  # Repeat the keyword for each entry
    # })

    # Return the DataFrame
    # return news_data
    return None  # Placeholder for actual scraping logic

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
    {'name': 'indeksonline', 'url': 'https://indeksonline.net'},
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
    {'name': 'lajmi', 'url': 'https://lajmi.net'},
    {'name': 'gazetablic', 'url': 'https://gazetablic.com'},
    {'name': 'demokracia', 'url': 'https://demokracia.com'},
    {'name': 'albanianpost', 'url': 'https://albanianpost.com'},
]

while True:
    # Create an empty DataFrame to store all news
    all_news = pd.DataFrame()

    # Iterate through websites and scrape news for each keyword
    for site in websites:
        for keyword in keywords:
            news_data = scrape_news(keyword, site['url'])
            if news_data is not None:  # Check if news_data is not empty
                all_news = pd.concat([all_news, news_data])

    # Apply styling to the DataFrame
    styled_table = all_news.style.set_table_styles([
        {'selector': 'tr:hover', 'props': [('background-color', '#ffff99')]},  # Highlight on hover
        {'selector': 'th', 'props': [('background-color', '#f2f2f2')]},       # Header background color
        {'selector': 'td', 'props': [('border', '1px solid #dddddd')]}       # Cell border
    ])

    # Write the HTML output to a file
    with open('news_table.html', 'w') as file:
        file.write(styled_table.to_html(render_links=True, escape=False))

    # Print the DataFrame
    print(all_news)

    # Wait for 60 seconds before fetching information again
    time.sleep(60)
