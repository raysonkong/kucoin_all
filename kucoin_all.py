from requests import Request, Session
import json
import pprint
import datetime
import time
import os
from config import *
from kucoin.client import Client
client = Client(API_KEY, SECRET_KEY, PASSPHRASE)


# ## ==================================##
# ## setup config_cmc.py in the same folder
# ## ==================================##


# HOW_MANY_COINS = 400

# EXCHANGES=["KUCOIN"] # can only have one exchange .....haha

# WANTED_CURRENCIES = ['USDT'] ## can only have one ....for now

# # # Do not alter below easily
# GROUP_SIZE = len(EXCHANGES) * 1000


# API_KEY = 'Your Key'
# SECRET_KEY = 'Your Key'
# PASSPHRASE = 'Your PassPhrase'
# ## end of Config file


# ## ==================================##
# ## End of Config
# ## ==================================##



## ==================================##
#===== Setup Date and Time #======== 
## ==================================##
# Date
generation_date = datetime.datetime.now()
generation_date = generation_date.strftime("%d_%m_%Y")


## ==================================##
## ======= Making the Request ========= ####
## ==================================##

#info = client.get_symbol_info('BNBBTC')
allCurrencies = client.get_currencies()

# response
# [ {'symbol': 'ETHBTC', 'price': '0.07002700'}, .... ] 

#print(allCurrencies)

symbols = []

for coin in allCurrencies:
    symbols.append(coin['name'])

#print(symbols)


## ===================================================##
##  ========   Helper Function: Append "Kucoin:" and  "USDT" to pairs ======== ####
## =====================================================##

finalSymbols = []

def appendExchange(symbols):
    for symbol in symbols:
        finalSymbols.append(EXCHANGES[0] + ":" + symbol + WANTED_CURRENCIES[0])

appendExchange(symbols)

#print(finalSymbols)



#================================
# ====== Helper Function ======== 
# Group output from last Step
# to a list containing lists of n 
#================================

# Group size, in production n=400
n=GROUP_SIZE

def group_into_n(data_list, n):
    return [data_list[i:i+n] for i in range(0, len(data_list), n)]

#test = [1,2,3,4,5,6,7,8]
#print(group_into_n(test, n))

grouped_pairs = group_into_n(finalSymbols, n)

#print(grouped_pairs)


#================================================
# ======== Outputting ======
# write a function to output each of the group in last
# to a separate file
#================================================


#def output_to_text_file(nested_grouped_pairs):
#    for idx, group in enumerate(nested_grouped_pairs):
#        with open(f'{idx+1}CMC p.{idx+1} {generation_date}.txt ', 'w') as f:
#            for pair in group:
#                f.write("%s,\n" % pair)


# /Users/raysonkong/code/python/webscrapping/scripts_v2/cmc_api_to_tradingview/outputs
def output_to_text_file(nested_grouped_pairs):
    for idx, group in enumerate(nested_grouped_pairs):
            filename=f"{os.getcwd()}/{EXCHANGES[0]}_All_{generation_date}/-1.0 {idx+1}.{EXCHANGES[0]}_All_{generation_date}.txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                for pair in group:
                  f.write("%s,\n" % pair)

#output_to_text_file(grouped_pairs)


def run_srapper():
    os.system('clear')
    output_to_text_file(grouped_pairs)


    print("== Kucoin Scrapping Completed ==")
    print('\n')
    #print("======================================================")
if __name__ =='__main__':
    run_srapper()

