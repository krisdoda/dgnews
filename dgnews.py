import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent

class ProxyRequests:
    def __init__(self):
        self.proxies = []

    def fetch_proxies(self):
        # Fetch proxies from a reliable source
        response = requests.get('https://www.sslproxies.org/')
        soup = BeautifulSoup(response.text, 'html.parser')
        for row in soup.find_all('tr')[1:]:
            columns = row.find_all('td')
            ip = columns[0].get_text()
            port = columns[1].get_text()
            self.proxies.append(f"{ip}:{port}")

    def get_random_proxy(self):
        # Get a random proxy from the list
        return random.choice(self.proxies) if self.proxies else None

class Scraper:
    def __init__(self):
        self.proxy = ProxyRequests()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        ]

    def scrape_url(self, url):
        # Fetch a random proxy
        proxy_addr = self.proxy.get_random_proxy()
        proxies = {"http": proxy_addr, "https": proxy_addr} if proxy_addr else None

        # Choose a random user agent
        user_agent = random.choice(self.user_agents)

        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

def main():
    scraper = Scraper()
    urls = [
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
        {'name': 'top-channel', 'url': 'https://top-channel.tv'},
        {'name': 'syri', 'url': 'https://syri.net'},
        {'name': 'lajmi', 'url': 'https://lajmi.net'},
        {'name': 'gazetablic', 'url': 'https://gazetablic.com'},
        {'name': 'demokracia', 'url': 'https://demokracia.com'},
        {'name': 'albanianpost', 'url': 'https://albanianpost.com'}
    ]

    articles = []  # Store all articles

    for site in urls:
        html = scraper.scrape_url(site['url'])
        if html:
            # Process the HTML content
            soup = BeautifulSoup(html, 'html.parser')
            # Find all the articles on the page
            article_links = soup.find_all('a', href=True)
            for link in article_links:
                article_url = link['href']
                # Check if the link is a valid article link
                if article_url.startswith('http'):
                    # Store the article URL along with the site name
                    articles.append({'site': site['name'], 'url': article_url})

    # Now you can process the articles list further as needed
    for article in articles:
        print(f"Site: {article['site']}, Article URL: {article['url']}")

if __name__ == "__main__":
    main()

