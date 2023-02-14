import pandas as pd
import requests

# Create list of prices
df = pd.read_csv('avocado.csv')
prices = df['AveragePrice'].to_list()
data = {'data':prices}


url = 'https://charmingly-gigantic-dragon-fort-dev.wayscript.cloud'
response = requests.post(url, json = data)
print(response.content)