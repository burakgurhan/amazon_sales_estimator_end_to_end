import os
import requests
from bs4 import BeautifulSoup

class Scraper:
    def url_create(asin):
        if len(asin)==10:
            base_url = "https://www.amazon.com/dp/"
            url = base_url + asin
            return url
        else: 
            raise Exception
    def scrape_amazon_product(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find BSR, category, and sales data (replace with actual selectors)
            bsr_element = soup.find(id='productDetails_feature_div')  # Adjust selector
            category_element = soup.find(id='breadcrumb')  # Adjust selector
            sales_element = soup.find(id='salesRank')  # Adjust selector

            if bsr_element and category_element and sales_element:
                bsr = bsr_element.text.strip()
                category = category_element.text.strip()
                sales = sales_element.text.strip()

                return {'BSR': bsr, 'Category': category, 'Sales': sales}
            else:
                print("Error: Could not find required elements for", url)
                return None

        except Exception as e:
            print("An error occurred:", e)
            return None
scr = Scraper
scr.scrape_amazon_product("https://www.amazon.com/dp/B08N5DQJ17")