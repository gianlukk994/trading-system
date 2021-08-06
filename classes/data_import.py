import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from classes.indicators import Indicators

class DataImporter: 
  def __init__(self, file):
    self.filename = file
    self.data = pd.read_csv(file, parse_dates = ["Date"])
    self.data.set_index("Date", inplace = True)
    self.data["PrevClose"] = self.data.Close.shift(1)
    self.indicators = Indicators(self.data)
    self.data["SMA200"] = self.indicators.sma("Close", 200)
    self.data["BBU200"] = self.indicators.bollinger_bands("Close", 200, 2)
    self.data["BBL200"] = self.indicators.bollinger_bands("Close", 200, 2)
    self.data["ExpMax"] = self.indicators.expanding_max("High")
    self.data["DonchianChannelUp"] = self.indicators.donchian_channel_up("High", 50)
    self.data["DonchianChannelDown"] = self.indicators.donchian_channel_down("Low", 50)

  def get_first_data(self, num = 5):
    return self.data.head(num)

  def get_last_data(self, num = 5):
    return self.data.tail(num)
  
  def get_graph(self):
    plt.figure(figsize=(8,4), dpi=300)
    plt.plot(self.data.DonchianChannelUp, color='blue', linewidth=1.0)
    plt.plot(self.data.DonchianChannelDown, color='red', linewidth=1.0)
    plt.plot(self.data.ExpMax, color='orange', linewidth=2.0)
    plt.plot(self.data.Close, color='green', linewidth=1.0)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("")
    plt.grid(True)
    return plt.show()