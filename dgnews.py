import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from proxy_requests import ProxyRequests

# Function to scrape news
def scrape_news(keyword, url):
    try:
        # Initialize ProxyRequests object
        proxy = ProxyRequests(url)
        
        # Fetch a list of proxies
        proxy.get_proxies_from_url('https://www.sslproxies.org/')
        proxy.set_proxy()
        
        response = proxy.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return pd.DataFrame()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
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

# Function to rotate user agents
def rotate_user_agent():
    return choice(USER_AGENTS)

# Function to scrape news
def scrape_news(keyword, url):
    try:
        # Initialize ProxyRequests object
        proxy = ProxyRequests(url)
        
        # Fetch a list of proxies
        proxy.get_proxies_from_url('https://www.sslproxies.org/')
        proxy.set_proxy()
        
        response = proxy.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return pd.DataFrame()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
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
    {'name': '
