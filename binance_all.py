from requests import Request, Session
import json
import pprint
import datetime
import time
import os
from config_binance_all import *
from binance.client import Client
client = Client(API_KEY, SECRET_KEY)


## ==================================##
## setup config_cmc.py in the same folder
## ==================================##





#===== Setup Date and Time #======== 
# Date
generation_date = datetime.datetime.now()
generation_date = generation_date.strftime("%d_%m_%Y")


## ======= Making the Request ========= ####
#info = client.get_symbol_info('BNBBTC')
binance_info = client.get_all_tickers()

# response
# [ {'symbol': 'ETHBTC', 'price': '0.07002700'}, .... ] 

#print(binance_info[0])

symbols = []

for info in binance_info:
    for wantedCurrency in WANTED_CURRENCIES:
        wantedCurrencyLen = len(wantedCurrency)
        if info['symbol'][-wantedCurrencyLen:] == wantedCurrency:
            symbols.append(info['symbol'])

#print(symbols)

### ====== Helper Functon====
## remove UPUSDT and DOWNUSDT ## 

derivatives = ['UPUSDT', 'DOWNUSDT']
noDerivativeSymbols = []

def removeUnwanted(symbols):
    for symbol in symbols:
        for derivative in derivatives:
            if symbol[-6:] != derivative and symbol[-8:] != derivative:
                noDerivativeSymbols.append(symbol)

removeUnwanted(symbols)


#print(len(noDerivativeSymbols))








##  ========   Helper Function ======== ####
# Append "Binance:" to each of these trading pairs above

finalSymbols = []

def appendExchange(symbols):
    for symbol in symbols:
        finalSymbols.append(EXCHANGES[0] + ":" + symbol)

appendExchange(noDerivativeSymbols)

#print(finalSymbols)


#================================================
# Group output from last Step
# to a list containing lists of n 

# Group size, in production n=400
n=GROUP_SIZE

def group_into_n(data_list, n):
    return [data_list[i:i+n] for i in range(0, len(data_list), n)]

#test = [1,2,3,4,5,6,7,8]
#print(group_into_n(test, n))

grouped_pairs = group_into_n(finalSymbols, n)

#print(grouped_pairs)


#================================================

# write a function to output each of the group in last
# to a separate file


#def output_to_text_file(nested_grouped_pairs):
#    for idx, group in enumerate(nested_grouped_pairs):
#        with open(f'{idx+1}CMC p.{idx+1} {generation_date}.txt ', 'w') as f:
#            for pair in group:
#                f.write("%s,\n" % pair)


# /Users/raysonkong/code/python/webscrapping/scripts_v2/cmc_api_to_tradingview/outputs
def output_to_text_file(nested_grouped_pairs):
    for idx, group in enumerate(nested_grouped_pairs):
            filename=f"{os.getcwd()}/Binance_All_{generation_date}_/-1.0 {idx+1}.BINANCE_All_{generation_date}.txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                for pair in group:
                  f.write("%s,\n" % pair)

#output_to_text_file(grouped_pairs)


def run_srapper():
    os.system('clear')
    output_to_text_file(grouped_pairs)


    print("== Binance Scrapping Completed ==")
    print('\n')
    #print("======================================================")
if __name__ =='__main__':
    run_srapper()

