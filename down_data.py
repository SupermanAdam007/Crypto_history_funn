import requests

class Downloader(object):


	def __init__(self):
		self.url = 'https://min-api.cryptocompare.com/data/'
		self.DEFAULT_MARKET = 'Poloniex'

	def get_pricemulti(self, fsyms, tsyms, e=''):
		"""
		fsyms: list of coins from
		tsyms: list of coins to
		e: markets
		response_type=''
		"""
		if e == '':
			e = self.DEFAULT_MARKET

		req = '&'.join([
			self.url + 'pricemulti?', 
			'fsyms=' + ','.join(fsyms), 
			'tsyms=' + ','.join(tsyms), 
			'e=' + e])

		print('get_pricemulti request: ' + req)
		res = requests.get(req)
		return res

	def get_histo(self, t_horiz='minute', fsym, tsym, limit=60, aggregate=1, e=''):
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
			self.url + 'histo'+type+'?', 
			'fsym=' + fsym, 
			'tsym=' + tsym, 
			'limit=' + str(limit), 
			'aggregate=' + str(aggregate), 
			'e=' + e])

		print('get_histominute request: ' + req)
		res = requests.get(req)
		return res


	def get_histominute(self, fsym, tsym, limit=60, aggregate=1, e=''):
		"""
		fsyms: coin from: ex. 'XMR'
		tsyms: coin to: ex. 'BTC'
		e: markets, ex. 'Poloniex' ... default
		aggregate: min = 1
		limit: min = 1, max = 2000
		"""
		if e == '':
			e = self.DEFAULT_MARKET

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

	def get_histohour(self, fsym, tsym, limit=60, aggregate=1, e=''):
		"""
		fsyms: coin from: ex. 'XMR'
		tsyms: coin to: ex. 'BTC'
		e: markets, ex. 'Poloniex' ... default
		aggregate: min = 1
		limit: min = 1, max = 2000
		"""
		if e == '':
			e = self.DEFAULT_MARKET

		req = '&'.join([
			self.url + 'histohour?', 
			'fsym=' + fsym, 
			'tsym=' + tsym, 
			'limit=' + str(limit), 
			'aggregate=' + str(aggregate), 
			'e=' + e])

		print('get_histohour request: ' + req)
		res = requests.get(req)
		return res

	def get_histoday(self, fsym, tsym, limit=60, aggregate=1, e=''):
		"""
		fsyms: coin from: ex. 'XMR'
		tsyms: coin to: ex. 'BTC'
		e: markets, ex. 'Poloniex' ... default
		aggregate: min = 1
		limit: min = 1, max = 2000
		"""
		if e == '':
			e = self.DEFAULT_MARKET

		req = '&'.join([
			self.url + 'histoday?', 
			'fsym=' + fsym, 
			'tsym=' + tsym, 
			'limit=' + str(limit), 
			'aggregate=' + str(aggregate), 
			'e=' + e])

		print('get_histohour request: ' + req)
		res = requests.get(req)
		return res


	def get_pricemulti_json(self, fsyms, tsyms, e=''):
		return self.get_pricemulti(fsyms, tsyms, e).json()

	def get_histominute_json(self, fsym, tsym, limit=60, aggregate=1, e=''):
		return self.get_histominute(fsym, tsym, limit, aggregate, e='').json()

	def get_histohour_json(self, fsym, tsym, limit=60, aggregate=1, e=''):
		return self.get_histohour(fsym, tsym, limit, aggregate, e='').json()

	def get_histoday_json(self, fsym, tsym, limit=60, aggregate=1, e=''):
		return self.get_histoday(fsym, tsym, limit, aggregate, e='').json()