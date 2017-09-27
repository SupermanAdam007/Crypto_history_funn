import requests

class Downloader(object):


	def __init__(self):
		self.url = 'https://min-api.cryptocompare.com/data/'
		self.url_poloniex = 'https://poloniex.com/public?command='
		self.DEFAULT_MARKET = 'Poloniex'

	def get_pricemulti(self, fsyms, tsyms, e='', verbose=True):
		"""
		fsyms: list of coins from
		tsyms: list of coins to
		e: markets
		"""
		if e == '':
			e = self.DEFAULT_MARKET

		req = '&'.join([
			self.url + 'pricemulti?', 
			'fsyms=' + ','.join(fsyms), 
			'tsyms=' + ','.join(tsyms), 
			'e=' + e])

		if verbose:
			print('get_pricemulti request: ' + req)

		res = requests.get(req)
		return res

	def get_histo(self, fsym, tsym, limit=60, aggregate=1, e='', t_horiz='minute', verbose=True):
		"""
		t_horiz: minute, hour, day
		fsyms: coin from: ex. 'XMR'
		tsyms: coin to: ex. 'BTC'
		e: markets, ex. 'Poloniex' ... default
		aggregate: min = 1
		limit: min = 1, max = 2000
		"""
		types = ['minute', 'hour', 'day']
		if t_horiz not in types:
			raise Exception('Invalid t_horiz parameter... Choose from: ' + ','.join(types))

		if e == '':
			e = self.DEFAULT_MARKET

		req = '&'.join([
			self.url + 'histo'+t_horiz+'?', 
			'fsym=' + fsym, 
			'tsym=' + tsym, 
			'limit=' + str(limit), 
			'aggregate=' + str(aggregate), 
			'e=' + e])

		if verbose:
			print('get_histo' + t_horiz + ' request: ' + req)

		res = requests.get(req)
		return res

	def get_returnTradeHistory(self, currencyPair, t_from, t_to, verbose=True):
		"""
		currencyPair: list of coins from
		t_from: list of coins to
		t_to: markets
		"""

		req = '&'.join([
			self.url_poloniex + 'returnTradeHistory', 
			'currencyPair=' + '_'.join(currencyPair), 
			'start=' + str(t_from), 
			'end=' + str(t_to)])

		if verbose:
			print('get_returnTradeHistory request: ' + req)

		res = requests.get(req)
		return res


	def get_pricemulti_json(self, fsyms, tsyms, e='', verbose=True):
		return self.get_pricemulti(fsyms, tsyms, e, verbose).json()

	def get_histo_json(self, fsym, tsym, limit=60, aggregate=1, e='', t_horiz='minute', verbose=True):
		return self.get_histo(fsym, tsym, limit, aggregate, e, t_horiz, verbose).json()

	def get_returnTradeHistory_json(self, currencyPair, t_from, t_to, verbose=True):
		return self.get_returnTradeHistory(currencyPair, t_from, t_to, verbose).json()