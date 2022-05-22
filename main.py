import requests
import json
import time
import re
import sys,socket
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from io import BytesIO
import pdb
## TODO: ADD CONFIG FOR Lister name and ID and API TOKEN Cleanup Code
## Once Committed Create a readme



# CONFIGS
API_TOKEN = ''
LISTERS = {
    'Troy': '6112',
    'Mattison': '3183',
}
lister_names = ["Troy", "Mattison"]
year_list = ['2020', '2021', '2022']
month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09','10', '11', '12']


TOTAL_SALES = []
def return_sales(LISTER, DATE):
    final= Tk()
    final.title("Goodwill Sales Dashboard")
    final.geometry("500x260")
    final.minsize(500, 260)
    final.maxsize(500, 260)
    final.configure(background='#ffffff')
    # Goodwill Icon
    icon_url = "https://images.crowdspring.com/blog/wp-content/uploads/2010/08/27132550/goodwill-logo.jpg"
    icon_response = requests.get(icon_url)
    ico_data = icon_response.content
    icon = ImageTk.PhotoImage(Image.open(BytesIO(ico_data)))

    # Goodwill Logo
    gwlogo_url = "https://p.kindpng.com/picc/s/224-2248260_goodwill-industries-hd-png-download.png"
    gwlogo_response = requests.get(gwlogo_url)
    gwlogo_data = gwlogo_response.content
    gwlogo = ImageTk.PhotoImage(Image.open(BytesIO(gwlogo_data)))

    gwLable = Label(image = gwlogo)
    gwLable.place(x=0,y=0)

    main_lab = Label(final, text="Goodwill Sales Dashboard" ,font=("Arial", 15))
    main_lab.config(bg='#ffffff')
    main_lab.place(x=40, y=30)

    lister_lable = Label(final, text=DATE+' Sales for ' + LISTER ,font=("Arial", 15))
    lister_lable.config(bg='#ffffff')
    lister_lable.place(x=50, y=70)

    Sales_lable = Label(final, text='$' + str(TOTAL_SALES[0]) ,font=("Arial", 15))
    Sales_lable.config(bg='#ffffff')
    Sales_lable.place(x=110, y=115)

    final.iconphoto(False, icon)
    final.mainloop()
    return

def main(YEAR_MONTH, lister):
    sales_per_page = [] # Sales Per Api request
    MAX_PAGE = [] # Max Pages for lister
    def sales(current_page):
        id = LISTERS[lister] # Gets Lister And Lister ID

        # Gathers a specific listers listed products
        response = requests.get( # Upright API
            'https://app.uprightlabs.com/api/v2/products?page=' + str(current_page) + '&per_page=100&sort=id.desc&user_id=' + id, headers={'X-Authorization': API_TOKEN})
        json_response = response.json()

        USD_PER_PAGE = []
        API_CALL = json_response # Just Renaming API CALL
        PRODUCT_LIST = API_CALL["products"] # Gets All Products
        # Month Filter
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

        # Sold Filter
        for product in MONTH_PROD:
            PROD = product["product_listings"][0]
            if PROD['state'] == "SOLD":
                USD_PER_PAGE.append(float(PROD['current_price']))

        sales_per_page.append(sum(USD_PER_PAGE))
        return
    def page_filter():
        id = LISTERS[lister]
        response = requests.get('https://app.uprightlabs.com/api/v2/products?page=&per_page=100&sort=id.desc&user_id=' + id, headers={'X-Authorization': API_TOKEN})
        # Gathers a specific listers listed products
        json_response = response.json()

        ##
        ## Use this area to check if unauthed then run a tkinter window saying UNAUTHORIZED
        ##
        # search Meta for page number max if greater than 1 turn that number into an int and go through all pages
        meta = json_response["meta"]
        max_pages = meta['max_pages']
        MAX_PAGE.append(max_pages)
        return

    page_filter()
    # Parse Through all pages of a lister
    x = 1
    while x <= MAX_PAGE[0]:
        sales(current_page=x)
        x+=1

    total_sales_month = sum(sales_per_page)
    t_sales_int = int(total_sales_month)
    TOTAL_SALES.append(t_sales_int)
    return_sales(LISTER= lister, DATE = YEAR_MONTH)
    return

####################################################
################### Main GUI #######################
####################################################
win= Tk()
win.title("Goodwill Sales Dashboard")
# Gui Window Config
win.geometry("310x350")
win.minsize(310, 350)
win.maxsize(310, 350)
win.configure(background='black')

# Goodwill Icon
icon_url = "https://images.crowdspring.com/blog/wp-content/uploads/2010/08/27132550/goodwill-logo.jpg"
icon_response = requests.get(icon_url)
ico_data = icon_response.content
icon = ImageTk.PhotoImage(Image.open(BytesIO(ico_data)))

# Goodwill Logo
gwlogo_url = "https://www.goodwilldetroit.org/wp-content/uploads/2018/09/Goodwill_BusinessCards_NoBleed_P01-1-600x360.png"
gwlogo_response = requests.get(gwlogo_url)
gwlogo_data = gwlogo_response.content
gwlogo = ImageTk.PhotoImage(Image.open(BytesIO(gwlogo_data)))

gwLable = Label(image = gwlogo)
gwLable.place(x=-150,y=0)

main_lab = Label(win, text="Good Will Sales Dashboard",font=("Arial", 15))
main_lab.config(bg="#0e4883")
main_lab.place(x=30, y=10)

# Lister Select
listerVar = StringVar(win)
listerVar.set('Lister Name') # Def Value
lister = OptionMenu(win, listerVar, *lister_names)
lister.config(bg="#ffffff")
lister.place(x=20,y=45)


# Year Select
yearVar = StringVar(win)
yearVar.set('Year') # Def Value
year = OptionMenu(win, yearVar, *year_list)
year.config(bg="#ffffff")
year.place(x=130,y=45)

# Month Select
monthVar = StringVar(win)
monthVar.set('Month') # Def Value
month = OptionMenu(win, monthVar, *month_list)
month.config(bg="#ffffff")
month.place(x=200,y=45)
def search():
    yr = yearVar.get()
    mth = monthVar.get()
    yr_mth =  yr + '-' + mth
    win.destroy()
    main(YEAR_MONTH = yr_mth, lister = listerVar.get())
    return
# Query Data
ttk.Button(win, text= "Search",width= 20, command= search ).pack(side = BOTTOM, pady = 10)

win.iconphoto(False, icon)
win.mainloop()
