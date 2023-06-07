# Web scraping multisite Shopee and Aliexpress
- Web scraping through backend API in both Shopee and Aliexpress.
- Scraped data from shopee is used as reference for scraping items in Aliexpress.
- Final scraped data is saved as csv file format and also uploaded to MySQL database.
- Stats notification is sent to telegram after spider is done working.

# Result
- Please see the generated scraped data in [scraped data](https://github.com/allifizzuddin89/Shopee-Aliexpress-MySQL-Telegram/tree/development/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/spiders/data/main)

## Requirement : 
- Scrapy 2.9.0.
- Python 3.7 or above.
- Any working environment to install the required packages such as conda or pyenv.

### Install environment
- Refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/)
 
### HOW-TO
- Clone the repository
```bash  
  git clone https://github.com/allifizzuddin89/Shopee-Aliexpress-MySQL-Telegram.git
```
  - Create working environment (skip if already have any working environment)
```bash
  conda create --name scraping_env -c conda-forge python=3.10.13 scrapy=2.9.0
```
- Activate the working environment
```bash
  conda activate scraping_env
```
 - Run the spider
 ```bash
 scrapy runspider Shopee-Aliexpress-MySQL-Telegram/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/Scraping_MultipleSite_Shopee_Aliexpress_TelegramNotification_MySQL/spiders/main.py
 
 ```
 
 ## Troubleshoot
- Error might happen due to the cookies/ body/ API already expired or request being rejected by the server or the API simply has been changed by the administrator.
  - Please bear in mind, the web owner might change the web's code dynamically anytime. Therefore this web scraping code might not work if that happens.
- Solution: 
  1. Get new cookies using any API tools such as POSTMAN
  2. Using rotating proxy such as scraperapi.
  3. Search for new API. (experience and keen of eyes required)
  
## DISCLAIMER
- This work only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Every action is on your own responsibilities.
