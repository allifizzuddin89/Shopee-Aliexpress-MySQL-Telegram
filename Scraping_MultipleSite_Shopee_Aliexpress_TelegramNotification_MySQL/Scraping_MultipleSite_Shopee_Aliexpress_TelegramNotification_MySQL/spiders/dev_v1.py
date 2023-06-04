import scrapy
from scrapy import Request
from pprint import pprint
import json
from scrapy.shell import inspect_response
from scrapy.exceptions import CloseSpider
from pprint import pprint
import os
import sys
# from scrapy.statscollectors import StatsCollector as stats

# log the output
from scrapy.utils.log import configure_logging
import logging

## Telegram
# import the API Token and ID from creds.py module
# please use your own ID, API Token in that module
# Please see https://core.telegram.org/bots/faq to obtain the API TOKEN
# import API Token and user ID from cred.py module
# I might not upload it into remote git
from api_key import token_id
import requests

# REMINDER!
# Bot can't talk to bot
# Therefore you have to use non-bot ID
# use userinfobot in your telegram app to obtain your user ID (non-bot)
# If you insist on using the bot ID, it will produce error code 403

# # You might want to fill in your API TOKEN, and chat_id (user ID)
# TOKEN = token_id.TOKEN
# chat_id = token_id.chat_id

# url = f"https://api.telegram.org/bot{TOKEN}/getMe"
# print(requests.get(url).json())

# message = "hello from your telegram bot"

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message


# /mnt/0b6522c1-7577-423c-b7ec-a2a47184e34a/Documents/Freelance_ job/Portfolio/Shopee-Aliexpress-MySQL-Telegram/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/items.py

# current directory
path = os.getcwd()
print("\nCurrent Directory\n", path)
# parent of current directory
print(os.path.abspath(os.path.join(path, os.pardir)))
# insert current parent directory into sys.path
sys.path.insert(0,os.path.abspath(os.path.join(path, os.pardir)))
pprint(sys.path)


class DevV1Spider(scrapy.Spider):
    name = "dev_v1"
    # allowed_domains = ["x"]
    # start_urls = ["https://x"]

    # log the output
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.log',
        format='%(levelname)s: %(message)s',
        level=logging.WARNING
    )

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

    # Aliexpress cookies, headers, url methods
    # Key in search item in below
    def ali_var(self, search_text, page_no):
        # search_text = "repair kit iphone"
        search_text_dash = search_text.replace(' ','-')
        search_text_plus = search_text.replace(' ','+')
        # page_no = 1
        search_referer_value= f"https://www.aliexpress.com/w/wholesale-{search_text_dash}.html?d=y&page={page_no}&sorttype=total_tranpro_desc&SearchText={search_text_plus}&trafficChannel=main&g=y&sortType=total_tranpro_desc"

        ali_headers = {
            "authority": "www.aliexpress.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
            "bx-v": "2.5.0",
            "content-type": "application/json;charset=UTF-8",
            "dnt": "1",
            "origin": "https://www.aliexpress.com",
            "referer": search_referer_value,
            "sec-ch-ua": "\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
        }

        ali_cookies = {
            "ali_apache_id": "33.1.212.167.1685333181679.217556.7",
            "intl_locale": "en_US",
            "xman_f": "ZLeLX56GgZCgHtU/6ThJzZ76A+W5gA7qaOPluMEzsrTh8jTIyE8bx6t+YevVy9fhDCJdsfxsKpFj2c+0FkpUX+TjrGfGh4utcrOStqe5ynwadKbssEol0A==",
            "acs_usuc_t": "x_csrf=10m9uf0lxbqfy&acs_rt=e36f78ca5a4446d39d3f1ca46c446e13",
            "xman_t": "eorrgaT0F3qJDlyv4N7pPa67ljw+Pogx0+qtCGY4PtqAj/6NY3U8d7JA0OM4dOat",
            "aep_usuc_f": "site=glo&c_tp=MYR&region=MY&b_locale=en_US",
            "AKA_A2": "A",
            "_m_h5_tk": "67940435aa9764e143d9b204f4a69137_1685335802709",
            "_m_h5_tk_enc": "309b593451d6b0fcd72fcf73d6fdf223",
            "cna": "yRL7HOQtcWYCAXOkWwlsP9dS",
            "_gcl_au": "1.1.1015877035.1685333195",
            "_ga": "GA1.1.522781794.1685333195",
            "e_id": "pt40",
            "xman_us_f": "x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22aeuCID%22%3A%22%22%2C%22cookieCacheEffectTime%22%3A1685333481697%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=e36f78ca5a4446d39d3f1ca46c446e13",
            "JSESSIONID": "C504B5077898B0CB5405A0B42EFDF6E0",
            "intl_common_forever": "xg7O3W9heI+b9plt6+/iGdDhm+ItakyTYJ6/M5rH5NoA2bxqv+LAPQ==",
            "_ga_VED1YSGNC7": "GS1.1.1685333195.1.1.1685334070.60.0.0",
            "tfstk": "ccVcBiZ5ypY1qSCTVoGfGkArpq_Ra5dZx5P7aN4Pd9UqJUrmusfpUp5j1amcAiJ1.",
            "l": "fBPhcEBuN1a52JkUBO5Courza779UQdbzsPzaNbMiIEGa6B16tZruNC_yJQMJdtj_T5DaetzDWAfHdeM8l4Uzx60MGLwQhH0PB9p8e__E-ZF.",
            "isg": "BDAwaoHvIEfOe_xD_rfRGoM2AfeCeRTDK3LGuCqCLgvy5dKP0ohAUguTPeWF9cyb"
        }

        # body_pre = {"pageVersion":"984c9a58b6d16e5d8c31de9b899f058a","target":"root","data":{"d":"y","page":page_no,"sorttype":"total_tranpro_desc","SearchText":search_text,"trafficChannel":"main","g":"y","sortType":"total_tranpro_desc","origin":"y"},"eventName":"onChange","dependency":[]}
        # ali_body = f'{body_pre}'

        body_pre = {"pageVersion":"984c9a58b6d16e5d8c31de9b899f058a","target":"root","data":{"SearchText":search_text,"catId":"0","initiative_id":"SB_20230528201035","spm":"a2g0o.home.1000002.0","trafficChannel":"main","g":"y","page":page_no,"origin":"y"},"eventName":"onChange","dependency":[]}

        ali_body = f'{body_pre}'

        return ali_body, ali_headers, ali_cookies, search_referer_value
    
    # def stats(self):    
    #     print("\nSTATS SCRAPY\n")
    #     # print(self.crawler.stats.set_value())
    #     print(self.crawler.stats.get_stats())
    #     # You might want to fill in your API TOKEN, and chat_id (user ID)

    #     TOKEN = token_id.TOKEN
    #     chat_id = token_id.chat_id

    #     url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    #     print(requests.get(url).json())

    #     message = self.crawler.stats.get_stats()

    #     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    #     print(requests.get(url).json()) # this sends the message

    # Request shopee
    def start_requests(self):
        request = Request(
            url=self.url,
            method='GET',
            dont_filter=True,
            headers=self.headers,
            cookies=self.cookies,
            callback=self.shopee_parse,
            )
        yield request

    # Parse shopee sample data
    def shopee_parse(self, response):
        # inspect_response(response, self)
        raw_data = response.body
        # data is dict type
        data = json.loads(raw_data)

        # with open("data.json","w") as json_file:
        #     json.dump(data, json_file)

        # export data into json file
        # copy and paste the dict into https://jsonpathfinder.com/
        # easier to parse the desired data
        # uncomment this if you wish to find and add more data
        # with open("data.json", "w") as json_file:
        #     # convert dict into string using dump (serialize)
        #     json.dump(data, json_file)

        # 60 samples only
        # Uncomment code below for all item in a page
        # total = len(data["data"]["sections"][0]["data"]["item"])
        # for i in  range(total):
        for i in range(60):
            item_shopee = {
                'Item' : data["data"]["sections"][0]["data"]["item"][i]["name"],
                'Currency' : data["data"]["sections"][0]["data"]["item"][i]["currency"],
                'Price' : data["data"]["sections"][0]["data"]["item"][i]["price"]/100000,
                'Rating' : data["data"]["sections"][0]["data"]["item"][i]["item_rating"]["rating_star"],
                'Sold/Month' : data["data"]["sections"][0]["data"]["item"][i]["sold"],
            }
            # yield item_shopee
            # print('\n')
            # print(type(item))
            # print('\n')
            # yield item
            # print('\n')
            # print(item["Item"])
            # print(item["Price"])
            # print('\n')
            # too much words, it might buzz the search
            # shorten the words
            # words = item["Item"]
            # new_item = words.split()
            # joined_item = " ".join(new_item[:5])
            # new_words = [' '.join(x[:5]) for x in new_item]
            # print('Shorten item {}'.format(new_words))
            # print('New item {}'.format(new_item))
            # print('New item type {}'.format(type(new_item)))
            # print(joined_item)
            # print('\n')

            ali_body, ali_headers, ali_cookies, ali_url = self.ali_var(item_shopee['Item'],1)
            # print('\n')
            # pprint('Headers : {}'.format(ali_headers))
            # print('\n')
            # pprint('Cookies:{}'.format(ali_cookies))
            # print('\n')
            # pprint('Body: {}'.format(ali_body))
            # print('\n')
            # pprint('URL: {}'.format(ali_url))
            # print('\n\n')

            # if i == 59:
                # # You might want to fill in your API TOKEN, and chat_id (user ID)
                # TOKEN = token_id.TOKEN
                # chat_id = token_id.chat_id

                # url = f"https://api.telegram.org/bot{TOKEN}/getMe"
                # print(requests.get(url).json())

                # message = self.crawler.stats.get_stats()

                # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                # print(requests.get(url).json()) # this sends the message
            
            yield Request(
                url=ali_url,
                method='POST',
                dont_filter=True,
                headers=ali_headers,
                body=ali_body,
                cookies=ali_cookies,
                cb_kwargs= {'item_shopee': item_shopee},
                callback=self.ali_parse
            )
        # Name = data["data"]["sections"][0]["data"]["item"][1]["name"]
        # print('\n')
        # print(type(item))
        # print('\n')
        # yield item
        # print('\n')
        # print(Name)
        # print('\n')
        # too much words, it might buzz the search
        # shorten the words
        # words = Name
        # new_item = words.split()
        # joined_item = ' '.join(new_item)
        # # joined_item = " ".join(new_item[:5])
        # # new_words = [' '.join(x[:5]) for x in new_item]
        # # print('Shorten item {}'.format(new_words))
        # print('New item {}'.format(new_item))
        # print('New item type {}'.format(type(new_item)))
        # print(joined_item)
        # print('\n')

        # ali_body, ali_headers, ali_cookies, ali_url = self.ali_var(joined_item,1)
        # print('\n')
        # pprint('Headers : {}'.format(ali_headers))
        # print('\n')
        # pprint('Cookies:{}'.format(ali_cookies))
        # print('\n')
        # pprint('Body: {}'.format(ali_body))
        # print('\n')
        # pprint('URL: {}'.format(ali_url))
        # print('\n\n')

        # yield Request(
        #     url=ali_url,
        #     method='POST',
        #     dont_filter=True,
        #     headers=ali_headers,
        #     body=ali_body,
        #     cookies=ali_cookies,
        #     callback=self.ali_parse
        # )


    def ali_parse(self, response,item_shopee):
        
        print('\nSUCCESSFULL\n')
        # print(item['Item'])
        # inspect_response(response, self)
       
        # Exit if the connection is declined
        if response.status == 404: 
            raise CloseSpider('Receive 404 response')
        # elif response.status == 435:
        #     # You might want to fill in your API TOKEN, and chat_id (user ID)
        #     TOKEN = token_id.TOKEN
        #     chat_id = token_id.chat_id

        #     url = f"https://api.telegram.org/bot{TOKEN}/getMe"
        #     print(requests.get(url).json())

        #     message = self.crawler.stats.get_stats()

        #     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        #     print(requests.get(url).json()) # this sends the message
            
        
        raw_data= response.body
        data = json.loads(raw_data)

        # inspect_response(response, self)

        # with open("data_ali.json", "w") as json_file:
        #     convert dict into string using dump (serialize)
        #     json.dump(data, json_file)
        
        # Name = data[x.data.result.mods.itemList.content[0].title.displayTitle

        total_data_perpage = len(data['data']['result']['mods']['itemList']['content'])
        try:
            total_data_perpage = data['data']['result']['pageInfo']['pageSize']
        except KeyError:
            raise CloseSpider('Data per page is not exist, no more data')
        print('\n\n Has {} DATA\n\n'.format(total_data_perpage))
        
        # Exit if there is no data available data
        if total_data_perpage == 0:
            raise CloseSpider('No data in response')
        
        # Name = data['data']['result']['mods']['itemList']['content'][0]['title']['displayTitle']
        # # yield Name
        # print(Name)

        from Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL.items import ScrapingMultiplesiteShopeeAliexpressTelegramnotificationMysqlItem

        item = ScrapingMultiplesiteShopeeAliexpressTelegramnotificationMysqlItem()

        # Name
        # Price
        # Currency
        # Sold
        # SHOPEE_Ref
        # SHOPEE_Price
        # SHOPEE_Sold
        
        # output csv file is in data folder in this project folder root
        for i in range(total_data_perpage):
            try:
                item['Name'] = data['data']['result']['mods']['itemList']['content'][i]['title']['displayTitle']
                item['Price'] = data['data']['result']['mods']['itemList']['content'][i]['prices']['salePrice']['minPrice']
                item['Currency'] = data['data']['result']['mods']['itemList']['content'][i]['prices']["currencySymbol"]
                item['Sold'] = data['data']['result']['mods']['itemList']['content'][i]["trade"]["tradeDesc"].strip(' sold').strip('+')
                item['SHOPEE_Ref'] = item_shopee['Item']
                item['SHOPEE_Price'] = item_shopee['Price']
                item['SHOPEE_Sold'] = item_shopee['Sold/Month']
                yield item
            except KeyError:
                item={
                    'Name' : None,
                    'Price' : None
                }
            except IndexError:
                item={
                    'Name' : None,
                    'Price' : None
                }

    # Sent stats to telegram after finished scraping
    def closed(self,reason):
        print('DAH HABIS WEIII')
        ## You might want to fill in your API TOKEN, and chat_id (user ID)
        TOKEN = token_id.TOKEN
        chat_id = token_id.chat_id

        url = f"https://api.telegram.org/bot{TOKEN}/getMe"
        print(requests.get(url).json())

        message = self.crawler.stats.get_stats()

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message

        
# print("\nSTATS SCRAPY\n")
# object = DevV1Spider()
# object.stats()

# print("\nSTATS SCRAPY\n")
# # print(self.crawler.stats.set_value())
# print(crawler.stats.get_stats())
# # You might want to fill in your API TOKEN, and chat_id (user ID)

# TOKEN = token_id.TOKEN
# chat_id = token_id.chat_id

# url = f"https://api.telegram.org/bot{TOKEN}/getMe"
# print(requests.get(url).json())

# message = self.crawler.stats.get_stats()

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message
        # print(self.crawler.stats.set_value())
        # print(self.crawler.stats.get_stats())
        # You might want to fill in your API TOKEN, and chat_id (user ID)

        # TOKEN = token_id.TOKEN
        # chat_id = token_id.chat_id

        # url = f"https://api.telegram.org/bot{TOKEN}/getMe"
        # print(requests.get(url).json())

        # message = self.crawler.stats.get_stats()

        # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        # print(requests.get(url).json()) # this sends the message

    # def stats(self):    
    #     print("\nSTATS SCRAPY\n")
    #     # print(self.crawler.stats.set_value())
    #     print(self.crawler.stats.get_stats())
    #     # You might want to fill in your API TOKEN, and chat_id (user ID)

    #     TOKEN = token_id.TOKEN
    #     chat_id = token_id.chat_id

    #     url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    #     print(requests.get(url).json())

    #     message = self.crawler.stats.get_stats()

    #     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    #     print(requests.get(url).json()) # this sends the message
        
                
            # try:
            #     item ={
            #         'Name' : data['data']['result']['mods']['itemList']['content'][i]['title']['displayTitle'],
            #         'Price' : data['data']['result']['mods']['itemList']['content'][i]['prices']['salePrice']['minPrice'],
            #         'Currency' : data['data']['result']['mods']['itemList']['content'][i]['prices']["currencySymbol"],
            #         'Sold' : data['data']['result']['mods']['itemList']['content'][i]["trade"]["tradeDesc"].strip(' sold'),
            #         'SHOPEE Ref' : item['Item'],
            #         'SHOPEE Price' : item['Price'],
            #         'SHOPEE Sold' : item['Sold/Month'],
            #         # 'URL Link' : response.css('div.list--gallery--34TropR > a.manhattan--container--1lP57Ag::attr(href)')  # please review
            #     }
            #     yield item
            # except KeyError:
            #     item={
            #         'Name' : None,
            #         'Price' : None
            #     }
            #     # yield item
            # except IndexError:
            #     item={
            #         'Name' : None,
            #         'Price' : None
            #     }
            #     # yield item
        
        

        # self.page_no += 1
        # search_referer_value= f"https://www.aliexpress.com/w/wholesale-{self.search_text_dash}.html?d=y&page={self.page_no}&sorttype=total_tranpro_desc&SearchText={self.search_text_plus}&trafficChannel=main&g=y&sortType=total_tranpro_desc"

        # self.body_pre['data']['page'] = self.page_no
        # self.body = f'{self.body_pre}'

        # self.headers['referer'] = search_referer_value
        
        # # print('\n\n Has {} DATA in page {}\n'.format(total_data_perpage,self.page_no-1))
        # # print('\nPAGE NO {}'.format(self.page_no))
        # # print('\n')
        # # pprint('HEADERS : {}'.format(self.headers))
        # # print('\n')
        # # pprint('BODY : {}'.format(self.body))
        # # print('\n')

        # yield response.follow(
        #     url=self.url,
        #     method='POST',
        #     dont_filter=True,
        #     cookies=self.cookies,
        #     headers=self.headers,
        #     body=self.body,
        #     callback= self.parse