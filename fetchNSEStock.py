## (C) 2019 Zafrul Umar
## fetch live stock price and store in CSV file
import sys
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

def fetch_NSE_stock_price(stock_code):
    
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_code)
    response = requests.get(stock_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item)+1
            latestPrice=data_array[index].split('"')[1]
            return float(latestPrice.replace(',',''))
    

stock_code = sys.argv[1]
t_iteration = int(sys.argv[2])
d_sleep = int(sys.argv[3]) 

data_file = open(stock_code+'_NSE_stock.csv','w'); 


iteration = 0
while iteration < t_iteration:
    c_date = date.today().strftime("%B %d, %Y")
    c_time = datetime.now().strftime("%H:%M:%S")
    current_stock_price = fetch_NSE_stock_price(stock_code)
    print (stock_code + ',' + c_date + ','  + c_time + ',' + str(current_stock_price) )
    print(stock_code + ',' + c_date + ','  + c_time + ',' + str(current_stock_price), file=data_file)
    time.sleep(d_sleep)
    iteration = iteration + 1

data_file.close()