import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    data = pd.read_csv('price.csv')
    data['DATE'] = pd.to_datetime(data['DATE'])
    x = data['DATE']
    y1 = data['LOWEST']
    y2 = data['MEDIAN']

    plt.cla()

    plt.plot(x, y1, label='Lowest')
    plt.plot(x, y2, label='median')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.grid()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.grid()
plt.show()