import requests

def item_to_track():
    item_link = input("Link to steam community market for your item: ")
    return item_link[47:]

def check_lowest_price(market_name):
    r = requests.get(f"http://steamcommunity.com/market/priceoverview/?market_hash_name={market_name}&appid=730&currency=29").json()
    print(r)


check_lowest_price(item_to_track())