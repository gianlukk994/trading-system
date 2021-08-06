from classes.data_import import DataImporter
from classes.strategies.dummy_strategy import DummyStrategy

data = DataImporter("SPY.txt")
strategy = DummyStrategy(data.get_all_data())
print(strategy.get_graph())