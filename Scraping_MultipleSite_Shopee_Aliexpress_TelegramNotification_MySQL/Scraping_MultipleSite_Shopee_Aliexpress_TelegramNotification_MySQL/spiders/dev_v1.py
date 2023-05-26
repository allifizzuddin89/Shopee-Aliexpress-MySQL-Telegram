import scrapy
from scrapy import Request
import json
from scrapy.shell import inspect_response
import os
from dotenv import load_dotenv
# Rotating proxy
# API key imported from env
# Obtain your API key from
load_dotenv()
from scraper_api import ScraperAPIClient
client = ScraperAPIClient(os.getenv('API_KEY'))


class DevV1Spider(scrapy.Spider):
    name = "dev_v1"
    # allowed_domains = ["x"]
    # start_urls = ["https://x"]

    # Scraping women's bag category
    # Scraping hidden/backend API
    # URL, HEADERS and COOKIES are generated from curl
    # paste the curl into "https://michael-shub.github.io/curl2scrapy/"
    # We only scraped 60 items then to be used in the aliexpress
    # Telegram notification will be sent after scraping is finished
    # All scraped item from Aliexpress will be stored in DB MySQL

    url = 'https://shopee.com.my/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11000710&limit=60&offset=60'

    headers = {
        "authority": "shopee.com.my",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "if-none-match-": "55b03-81791b7699852afd3b9d57dde13b13cd",
        "referer": "https://shopee.com.my/Women\'s-Bags-cat.11000710?page=0&sortBy=sales",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57",
        "x-api-source": "pc",
        "x-requested-with": "XMLHttpRequest",
        "x-shopee-language": "en"
    }

    cookies = {
        "__LOCALE__null": "MY",
        "csrftoken": "SiTypa3S5O9aIn7Vt10ZYkL9hSqtM1ZC",
        "SPC_SI": "1WVsZAAAAABnZ2FQa1hINzezMwAAAAAAcUE4Y3ltdXM=",
        "SPC_F": "21VD6lv1TJZxaBLglHsXaUfi7oLjXtPX",
        "REC_T_ID": "eb3b9415-fb81-11ed-936a-08f1ea7bcd30",
        "_QPWSDCXHZQA": "2c456e81-f31d-4907-8ad6-541b7c6b1e47",
        "language": "en",
        "SPC_CLIENTID": "MjFWRDZsdjFUSlp4xfdvmbggzqrvlswh",
        "SPC_ST": ".eHJRb3VMUmszYVNZZlYyapp8YtP/SiPE15++GEx7v3BAhwVoJPxrOl6zSvJn+1lcZ/sIWPAs9n+bF5AxXfd83vdVm7Jvw6d4MRACL2qSnODnHyDIofjpjbVcUIIWGsZYkcnm0JfsM/dV+yM+CPlqDZs8X7Xx6YNI7rgfqxInvUwwdmguqAf4Fkf2qpzv3dsYb4jMFnevqmabmFU5bWrcHQ==",
        "SPC_U": "1005828798",
        "SPC_R_T_ID": "LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=",
        "SPC_R_T_IV": "VkF4NW96T0ZuOTNPa01xcg==",
        "SPC_T_ID": "LO5O13hYVGiybnOKZLoetcIFF7UMXh/M+vY3Q2xYMOsJMWbC4wcfLpgLkvL5m2lMcc5BGoFpgnOtmmvwrTUAlbCle2uLE3GaiHWnqg+xlJOXoBz3KZmnfeFjoCLoFZsQfM3+CZwfBwHWg7wnhK5bFzK0I4/VEPyhIpJcbhlNgrE=",
        "SPC_T_IV": "VkF4NW96T0ZuOTNPa01xcg==",
        "shopee_webUnique_ccd": "BCFSaLhJLvw2Gy9WJIy1fA%3D%3D%7CPFRHgIOCF%2FiQS7SABVfaIy6G5DGr7szkcApitY%2F5XXzboGGkMJfBm5%2BH9Iy3ZqlUMW3884wKcOPhaQAXsZ5f6rnZfazhd2W85s0%3D%7CJAG3%2FQc4nsXEX1N5%7C06%7C3",
        "ds": "92e12ee2d6a381d33af6d1da677e756a",
        "SPC_EC": "eTRTWlBwWEQwZEVCV2ZGVmevNQixAFz+x8/2bQSaiBTzBka2oxGhsGYd/8RkM9mLz2Re6luc5SpQrbRDXMBL3ZsxiOFnrzRI/aGYk9ZFzoTcMnVjNw5jd0OVrvYYICr3Q7rAbEA0n8w3bYB5s/+mg/FIF2cFb3m+poJHafPsZvo="
    }

    def start_requests(self):
        request = Request(
            url=self.url,
            method='GET',
            dont_filter=True,
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse,
            )
        yield request

    def parse(self, response):
        # inspect_response(response, self)
        raw_data = response.body
        # data is dict type
        data = json.loads(raw_data)

        # export data into json file
        # copy and paste the dict into https://jsonpathfinder.com/
        # easier to parse the desired data
        # uncomment this if you wish to find and add more data
        with open("data.json", "w") as json_file:
            # convert dict into string using dump (serialize)
            json.dump(data, json_file)

        # 60 samples ony
        # Uncomment code below for all item in a page
        # total = len(data["data"]["sections"][0]["data"]["item"])
        # for i in  range(total):
        for i in range(60):
            item = {
                'Item' : data["data"]["sections"][0]["data"]["item"][i]["name"],
                'Currency' : data["data"]["sections"][0]["data"]["item"][i]["currency"],
                'Price' : data["data"]["sections"][0]["data"]["item"][i]["price"]/100000,
                'Rating' : data["data"]["sections"][0]["data"]["item"][i]["item_rating"]["rating_star"],
                'Sold/Month' : data["data"]["sections"][0]["data"]["item"][i]["sold"],
            }
            yield item