class Indicators:
  def __init__(self, data):
    self.data = data

  def sma(self , index ,period):
    return self.data[index].rolling(period).mean()
  
  def bollinger_bands(self, index, period, k):
    return self.sma(index, period) + k * self.data[index].rolling(period).std()

  def expanding_max(self, index):
    return self.data[index].expanding().max()

  def donchian_channel_up(self, index, period):
    return self.data[index].rolling(period).max()
  
  def donchian_channel_down(self, index, period):
    return self.data[index].rolling(period).min()