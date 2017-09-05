import requests

class Downloader(object):


	def __init__(self):
		self.url = 'https://min-api.cryptocompare.com/data/'
		self.market = 'Poloniex'

	def get_pricemulti(self, fsyms, tsyms, e=''):
		"""
		fsyms: list of coins from
		tsyms: list of coins to
		e: markets
		response_type=''
		"""
		if e == '':
			e = self.market

		req = '&'.join([
			self.url + 'pricemulti?', 
			'fsyms=' + ','.join(fsyms), 
			'tsyms=' + ','.join(tsyms), 
			'e=' + e])

		print('get_pricemulti request: ' + req)
		res = requests.get(req)
		return res

	def get_pricemulti_json(self, fsyms, tsyms, e=''):
		return self.get_pricemulti(fsyms, tsyms, e).json()

	def get_pricemulti_json(self, fsyms, tsyms, e=''):
		return self.get_pricemulti(fsyms, tsyms, e).json()

	def get_histominute(self, fsym, tsym, limit=60, aggregate=1, e=''):
		"""
		fsyms: coin from: ex. 'XMR'
		tsyms: coin to: ex. 'BTC'
		e: markets, ex. 'Poloniex' ... default
		aggregate: min = 1
		limit: min = 1, max = 2000
		"""
		if e == '':
			e = self.market

		req = '&'.join([
			self.url + 'histominute?', 
			'fsym=' + fsym, 
			'tsym=' + tsym, 
			'limit=' + str(limit), 
			'aggregate=' + str(aggregate), 
			'e=' + e])

		print('get_histominute request: ' + req)
		res = requests.get(req)
		return res

	def get_histominute_json(self, fsym, tsym, limit=60, aggregate=1, e=''):
		return self.get_histominute(fsym, tsym, limit, aggregate, e='').json()

