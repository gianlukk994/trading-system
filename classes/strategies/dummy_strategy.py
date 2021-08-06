from classes.indicators import Indicators
import matplotlib.pyplot as plt

class DummyStrategy: 
  def __init__(self, data):
      self.data = data
      self.indicators = Indicators(self.data)
      self.__apply_indicators__()

  def __apply_indicators__(self):
    self.data["SMA200"] = self.indicators.sma("Close", 200)
    self.data["BBU200"] = self.indicators.bollinger_bands("Close", 200, 2)
    self.data["BBL200"] = self.indicators.bollinger_bands("Close", 200, 2)
    self.data["ExpMax"] = self.indicators.expanding_max("High")
    self.data["DonchianChannelUp"] = self.indicators.donchian_channel_up("High", 50)
    self.data["DonchianChannelDown"] = self.indicators.donchian_channel_down("Low", 50)

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