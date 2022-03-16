import requests
import schedule
import time

def item_to_track():
    item_link = input("Link to steam community market for your item: ")
    return item_link[47:]

def check_item_price(market_name):
    r = requests.get(f"http://steamcommunity.com/market/priceoverview/?market_hash_name={market_name}&appid=730&currency=29").json()
    return r

def check_lowest_price(data):
    return float(data['lowest_price'][4:])

def main_loop(name):
    item_price_data = check_item_price(name)
    lowest_price = check_lowest_price(item_price_data)

    with open("price.txt", "a") as f:
        f.write(f"${lowest_price}\n")
    if lowest_price > 6.22:
        print(f"LARGER THAN 6.22: ${lowest_price}")
    else:
        print(f"${lowest_price}")

def main():
    item_name = item_to_track()
    schedule.every(5).seconds.do(main_loop, name=item_name)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
main()