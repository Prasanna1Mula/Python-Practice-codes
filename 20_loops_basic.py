#inventory management system

import time

def check_low_stock():
    return["Product A" , "Product B"]
def notify_manager(products):
    print("Low stock alert! Products:", products)

while True:
    low_stock_products_list=check_low_stock()
    if low_stock_products_list:
        notify_manager(low_stock_products_list)
        time.sleep(3600)

