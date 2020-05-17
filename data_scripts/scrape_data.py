#PAGE 1 - Overview of US Market
import yfinance as yf
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

end = datetime.datetime(2020,3,12)
days = datetime.timedelta(365*3)
start = end - days

metals = ['GLD','SLV','COPX', 'PALL', 'SLX', 'REMX']
major_indexes = ['SPY','INDA','MCHI', 'EWZ', 'IEUR', 'AFK']
energy = ['USO','UNG','KOL', 'TAN', 'FAN']
currency = ['UUP','FXE']

def scrape_yield_curve():

    #https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldAll

    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldAll'

    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html)
    table = soup.find('table', {"class": "t-chart"})
    rows = table.find_all('tr')
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    result = pd.DataFrame(data, columns=['Date','1 Mo', '2 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr'])
    result[-252:].to_csv(r'./raw_data/yieldcurve.csv', index = False)

def scrape_yahoo_prices(stocks, start, end, file_label, format):
 
    #download
    data = yf.download(stocks, start=start, end=end)

    #print the header
    #data['Close'].head()

    if format == "daily-percent":
        #output to a file
        percent = round((data['Open']/data['Close']-1)*100,2)

        percent.to_csv(r"./raw_data/"+file_label+".csv")

    if format == "year-over-year":
        #https://stackoverflow.com/questions/28328636/calculating-year-over-year-growth-by-group-in-pandas
        data = (data['Close'] - data['Close'].shift(252))/ data['Close'].shift(252)
        data[-252:].to_csv(r"./raw_data/"+file_label+".csv")

    if format == "close_price":
        data['Close'].to_csv(r"./raw_data/"+file_label+".csv")

#http://www.worldgovernmentbonds.com/

scrape_yahoo_prices(major_indexes, start, end, "major_indexes", "year-over-year")
scrape_yahoo_prices(metals, start, end, "metals", "year-over-year")
scrape_yahoo_prices(energy, start, end, "energy", "year-over-year")
scrape_yahoo_prices(currency, start, end, "currency", "year-over-year")
scrape_yield_curve()