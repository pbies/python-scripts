#!/usr/bin/env python3

import ccxt

binance = ccxt.binance({
	'apiKey': 'YOUR_API_KEY',
	'secret': 'YOUR_SECRET',
	'enableRateLimit': True,
})

btc_usdt_ticker = binance.fetch_ticker('BTC/USDT')
btc_usdt_price = btc_usdt_ticker['last']
print('Current BTC/USDT price:', btc_usdt_price)

if btc_usdt_price < 50000:
	order = binance.create_market_buy_order('BTC/USDT', 0.01)
	print('Bought 0.01 BTC at market price')

positions = binance.fetch_open_orders('BTC/USDT')
for position in positions:
	if position['side'] == 'buy' and position['price'] > 55000:
		binance.create_market_sell_order('BTC/USDT', position['amount'])
		print('Sold', position['amount'], 'BTC at market price')
