from classes.data_import import DataImporter

data = DataImporter('SPY.txt')
print(data.get_first_data())