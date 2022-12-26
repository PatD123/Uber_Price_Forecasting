import pandas as pd
from matplotlib import pyplot

series = pd.read_csv("data.csv", header=0, index_col=0, parse_dates=True)
series[-2500:].plot()
pyplot.show()
