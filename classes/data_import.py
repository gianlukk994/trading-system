import pandas as pd
import numpy as np

class DataImporter: 
  def __init__(self, file):
    self.filename = file
    self.data = pd.read_csv(file, parse_dates = ["Date"])
    self.data.set_index("Date", inplace = True)
    self.data["PrevClose"] = self.data.Close.shift(1)
  
  def get_all_data(self):
    return self.data

  def get_first_data(self, num = 5):
    return self.data.head(num)

  def get_last_data(self, num = 5):
    return self.data.tail(num)
  