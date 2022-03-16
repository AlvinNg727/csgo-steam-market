import threading

from main import main
import graph

def item_to_track():
    item_link = input("Link to steam community market for your item: ")
    return item_link[47:]

item = item_to_track()
print(item)

thread1 = threading.Thread(target=main, args=(item, ), daemon=True)
thread1.start()

thread2 = threading.Thread(target=graph.main)
thread2.start()