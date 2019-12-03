import pandas as pd
import matplotlib.pyplot as plt
import datetime

a = pd.read_csv("game_play.csv")

b = a[a['movement'].str.contains("Moved")]
b['movement'] = b['movement'].str.replace("Moved: ", "")
new = b['movement'].str.split("_", n = 1, expand = True) 
b['x'] = pd.to_numeric(new[0])
b['y'] = pd.to_numeric(new[1])
b = b.drop("movement", axis = 1)
b['time'] = b['time'].map(str) + "." + b['num'].map(str)
b = b.drop("num", axis = 1)

b['time'] = b['time'].apply(lambda x : datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))

copy = b.shift(-1)
b['delta_t'] = copy['time'] - b['time']
b['delta_t'] = b['delta_t'].apply(lambda x : x.total_seconds())

b['delta_x'] = copy['x'] - b['x']
b['delta_y'] = copy['y'] - b['y']
b['dist'] = (b['delta_x'] ** 2 + b['delta_y'] ** 2 ) ** .5
b['avg_velocity'] = b['dist'] / b['delta_t']
graph = b[['time', 'avg_velocity']]
graph.drop(graph.tail(1).index, inplace = True)
graph = graph.copy(deep=True)

ax = plt.gca()
graph['rolling'] = graph['avg_velocity'].rolling(150).mean()
graph['rolling_two'] = graph['avg_velocity'].rolling(50).mean()
ax = graph.plot(kind='line', x = 'time', y = 'rolling', ax = ax, title = "Rolling Average Velocity During League of Legends", figsize=(16,5), legend = False)

ax.set_xlabel("Time (Day-Hours-Minutes")
ax.set_ylabel("Average Velocity (pixels/s)")
plt.savefig("avg_velocity.png")
