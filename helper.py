# input 
# [ {'symbol': 'ETHBTC', 'price': '0.07002700'}, .... ] 


binance_info = [ {'symbol': 'BNBBTC', 'price': '0.07002700'},
			     {'symbol': 'BTCUSDT', 'price': '23000'},
			     {'symbol': 'FTXBUSD', 'price': '0.0'}
			 ] 


result = []
currencies = ['USDT', 'BTC', 'BUSD']

def generate_tickers(binance_info, currencies):
	for info in binance_info:
		for currency in currencies:
			currency_length = len(currency)
			if info['symbol'][-currency_length:] == currency:
				result.append(info['symbol'][0:-currency_length])

generate_tickers(binance_info, currencies)



#print(result)
# ticker = "BTCUSDT"

# print(ticker[-4:])




# output
# [ 'BTC', "ETH", ...] 
# 