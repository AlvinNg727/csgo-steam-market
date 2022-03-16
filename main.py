import requests
import schedule
import time
import os
import csv
import sys
#import graph

def item_to_track():
    item_link = input("Link to steam community market for your item: ")
    return item_link[47:]

def check_item_price(market_name):
    r = requests.get(f"http://steamcommunity.com/market/priceoverview/?market_hash_name={market_name}&appid=730&currency=29").json()
    return r

def check_lowest_price(data):
    return float(data['lowest_price'][4:])

def check_median_price(data):
    return float(data['median_price'][4:])

def check_file_size():
    try:
        if os.path.getsize("price.csv") >= 1048576:
            return False
        else:
            return True
    except:
        print("Creating price csv...", flush=True)
        sys.stdout.flush()
        return 2

def write_to_file(time, lowest_price, median_price):
    file_size = check_file_size()

    if file_size == 2:
        with open("price.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["DATE", "LOWEST", "MEDIAN"])
            writer.writerow([time, lowest_price, median_price])
    elif file_size == False:
        print("Resetting csv...")
        sys.stdout.flush()
        with open("price.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["DATE", "LOWEST", "MEDIAN"])
            writer.writerow([time, lowest_price, median_price])
    elif file_size == True:
        with open("price.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time, lowest_price, median_price])

def main_loop(name):
    item_price_data = check_item_price(name)
    lowest_price = check_lowest_price(item_price_data)
    median_price = check_median_price(item_price_data)

    current_time = time.strftime("%Y %b %d %H:%M:%S")

    write_to_file(current_time, lowest_price, median_price)

    print(f"{current_time}  ${lowest_price}  ${median_price}")
    sys.stdout.flush()


def main(item):
    main_loop(item)
    schedule.every(10).seconds.do(main_loop, name=item)
    while True:
        schedule.run_pending()
        time.sleep(1)