import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataImporter: 
  def __init__(self, file):
    self.filename = file
    self.data = pd.read_csv(file, parse_dates = ["Date"])
    self.data.set_index("Date", inplace = True)
  
  def get_first_data(self, num = 5):
    return self.data.head(num)

  def get_last_data(self, num = 5):
    return self.data.tail(num)
  
  def get_graph(self):
    plt.figure(figsize=(8,4), dpi=300)
    plt.plot(self.data.Close, color='green')
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("")
    plt.grid(True)
    return plt.show()