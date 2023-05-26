import json
import scrapy
from scrapy import Request
from scrapy.shell import inspect_response
from pprint import pprint
import os
from dotenv import load_dotenv
# Rotating proxy
# API key imported from env
# Obtain your API key from
def configure():
    load_dotenv()

configure()
from scraper_api import ScraperAPIClient
client = ScraperAPIClient(os.getenv('API_KEY'))



class MainSpider(scrapy.Spider):
    name = "main"
    # allowed_domains = ["x"]
    # start_urls = ["http://x/"]
    ## Due to 'Application.run_async' was never awaited' erro
    import nest_asyncio
    nest_asyncio.apply()

    custom_settings={
        'COOKIES_ENABLED':True,
        'COOKIES_DEBUG':True
    }

    url = "https://shopee.com.my/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11000710&limit=60&offset=0"

    headers = {
        'authority': 'shopee.com.my',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__LOCALE__null=MY; csrftoken=SiTypa3S5O9aIn7Vt10ZYkL9hSqtM1ZC; SPC_SI=1WVsZAAAAABnZ2FQa1hINzezMwAAAAAAcUE4Y3ltdXM=; SPC_F=21VD6lv1TJZxaBLglHsXaUfi7oLjXtPX; REC_T_ID=eb3b9415-fb81-11ed-936a-08f1ea7bcd30; _QPWSDCXHZQA=2c456e81-f31d-4907-8ad6-541b7c6b1e47; language=en; SPC_CLIENTID=MjFWRDZsdjFUSlp4xfdvmbggzqrvlswh; SPC_ST=.eHJRb3VMUmszYVNZZlYyapp8YtP/SiPE15++GEx7v3BAhwVoJPxrOl6zSvJn+1lcZ/sIWPAs9n+bF5AxXfd83vdVm7Jvw6d4MRACL2qSnODnHyDIofjpjbVcUIIWGsZYkcnm0JfsM/dV+yM+CPlqDZs8X7Xx6YNI7rgfqxInvUwwdmguqAf4Fkf2qpzv3dsYb4jMFnevqmabmFU5bWrcHQ==; SPC_U=1005828798; SPC_R_T_ID=LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=; SPC_R_T_IV=VkF4NW96T0ZuOTNPa01xcg==; SPC_T_ID=LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=; SPC_T_IV=VkF4NW96T0ZuOTNPa01xcg==; shopee_webUnique_ccd=MwhOpl7%2Fxfl4BjyUZG4ouw%3D%3D%7CPV9HgIOCF%2FiQS7SABVfaIy6G5DGr7szkcApitY%2F5XXzboGGkMJfBm5%2BH9Iy3ZqlUMW3884wKcOPhaQAXsZ9f6LTRcaPvd2W85s0%3D%7CJAG3%2FQc4nsXEX1N5%7C06%7C3; ds=818f4333fa56937aa25fa41aa1b21d7c; SPC_EC=bkhEY04zc1ZKeEVkNjAzNfoc574sSYLTMQmU7dAU0kenAk2qFHi3mkwLqTa/cxRlPT6T2WZx9uyEoLu5l5w4q8C8quND6vBBnzFUCr2a92AT0FOlfyoA5H8q3A0EHctHo3l7nJXR5T8yZPuOZYDWYm3mCgv/0FNAuM1h33B+K5s=; SPC_EC=aWhsOVhVVzhKZmhCZ2JZUaJ/lZgAbztsTBsCKd4xAmCfBp7GjBV4FlRzlOF+8+j8WMK2gJJdJCEyIRFsEoXsx4xcz39TWGFr6Pq/VUJ+SQNmleoMFxkmv0km87SDUx6C8i7ajbcwh+nSVSgeanRCZVmvfMfE93CBs0c6WHBWGCY=; SPC_R_T_ID=LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=; SPC_R_T_IV=VkF4NW96T0ZuOTNPa01xcg==; SPC_SI=1WVsZAAAAABnZ2FQa1hINzezMwAAAAAAcUE4Y3ltdXM=; SPC_ST=.eHJRb3VMUmszYVNZZlYyapp8YtP/SiPE15++GEx7v3BAhwVoJPxrOl6zSvJn+1lcZ/sIWPAs9n+bF5AxXfd83vdVm7Jvw6d4MRACL2qSnODnHyDIofjpjbVcUIIWGsZYkcnm0JfsM/dV+yM+CPlqDZs8X7Xx6YNI7rgfqxInvUwwdmguqAf4Fkf2qpzv3dsYb4jMFnevqmabmFU5bWrcHQ==; SPC_T_ID=LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=; SPC_T_IV=VkF4NW96T0ZuOTNPa01xcg==; SPC_U=1005828798',
        'dnt': '1',
        'if-none-match-': '55b03-35336ac42c699e76fab05573ab31404c',
        'referer': 'https://shopee.com.my/Women\'s-Bags-cat.11000710?page=0',
        'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest',
        'x-shopee-language': 'en'
    }

    
    def start_requests(self):
        
        yield Request(
            client.scrapyGet(url=self.url),
            headers=self.headers,
            callback=self.parse
        )

    def parse(self, response):
        # inspect_response(response, self)
        raw_data = response.body
        data = json.loads(raw_data)
        pprint(data)
        item = {
            'Name' : data["data"]["sections"][0]["data"]["item"][0]["name"]
        }
        yield item