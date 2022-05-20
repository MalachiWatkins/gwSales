import requests
import json
import time
import re

import pdb

#pdb.set_trace()
upright_api = 'https://app.uprightlabs.com/api/v2/products?page=1&per_page=500&sort=id.desc&user_id=6673'
# products[x] for each prod
# DATE FILTER
YEAR_MONTH = '2022-05'
lister = 'Alexander'

MONTH_OF_SALES = []

LISTERS = {
    'Alexander': '6673',
    'EXA': '2351'
}

MAX_PAGES = []
api_response = '' # This is where the api call is stored
def lister_api(page):

    id = LISTERS[lister]

    response = requests.get(
            'https://app.uprightlabs.com/api/v2/products?page=' + page + '&per_page=100&sort=id.desc&user_id=' + id)
    # Gathers a specific listers listed products
    json_response = response.json()
    # search Meta for page number max if greater than 1 turn that number into an int and go through all pages
    return
def parsing():
    USD_PER_SOLD_ITEM = []
    # change to get with api response
    page = ('C:\\Users\\Malachi\\Desktop\\gwSales\\products.json')
    with open(page, encoding='utf8') as page:
        page_data = json.load(page)
        PRODUCT_LIST = page_data["products"]

        #Month Filter
        MONTH_PROD = []
        x=0
        while x < len(PRODUCT_LIST):
            regex = r"(.*)-"
            Single_prod = PRODUCT_LIST[x]
            dateMatch = re.finditer(regex, Single_prod['created_at'], re.MULTILINE)
            for match in dateMatch:
                if match[1] == YEAR_MONTH:
                    MONTH_PROD.append(Single_prod)
            x+=1

        #Sold Filter
        for product in MONTH_PROD:
            PROD = product["product_listings"][0]
            if PROD['state'] == "SOLD":
                USD_PER_SOLD_ITEM.append(float(PROD['current_price']))

        meta = page_data["meta"]
        max_pages = meta['max_pages']

        #PAGE FILTER


    MONTH_OF_SALES.append(sum(USD_PER_SOLD_ITEM))
    return
#lister_api(page='')
parsing()
time.sleep(10000)
