class Market(object):

	
	def __init__(self, commision=0.0015, max_opens=10):
		self.commision = commision
		self.buys_sells = 0
		self.max_opens = max_opens
		self.coins_list_btc = ['SYS','BCN','DGB','LBC','NOTE','PASC','NAUT','SC','NEOS','ETH','ZEC','MAID','XRP',
			'BTS','XEM','SBD','STRAT','LTC','AMP','BCY','ETC','ARDR','POT','NXT','BELA','XBC',
			'BTCD','XMR','NXC','XCP','DCR','BLK','RIC','STEEM','NMC','PINK','OMNI','SJCX','NAV']
		self.coins_list_btc.append('BTC')
		
		self.status = dict()
		self.init_status()

	def init_status(self):
		for coin_btc in self.coins_list_btc:
    		self.status[coin_btc] = 0

    def manual_add_to_status(self, coin_name, amount):
    	self.status[coin_name] = amount

	def buy_bcn(self, coin_name, amount, price_btc, verbose=False):
		if self.buys_sells == self.max_opens:
			if verbose:
				print('buys_sells == '+str(self.max_opens)+':', self.buys_sells == self.max_opens)
			return False

		if amount*price_btc*(1+self.commision) > self.status['BTC']:
			if verbose:
				print('Don\'t have enough BTC')
				print('\tHave:', self.status['BTC'])
				print('\tNeed:', amount*price_btc)
			return False

		self.status[coin_name] += amount - amount*self.commision
		self.status['BTC'] -= amount*price_btc

		self.buys_sells += 1

		if verbose:
			print('# Buy '+coin_name+': amount =', amount, 
				'### price_btc =', price_btc)
			self.print_have()

		return True


	def sell_bcn(self, coin_name, amount, price_btc, verbose=False):
		if self.buys_sells == -self.max_opens:
			if verbose:
				print('buys_sells == -'+str(self.max_opens)+':', self.buys_sells == -self.max_opens)
			return False

		if self.status[coin_name] < amount*(1+self.commision):
			if verbose:
				print('Don\'t have enough BNC')
			return False

		self.status[coin_name] -= amount 
		self.status['BTC'] += amount*price_btc - amount*self.commision*price_btc

		self.buys_sells -= 1
		
		if verbose:
			print('# Sell '+coin_name+': amount =', amount, 
				'### price_btc =', price_btc)
			self.print_have()

		return True


	def print_have(self):
		print('status[coin_name] =', self.status[coin_name])
		print('status[\'BTC\'] =', self.status['BTC'], 
			'[aprox. ', self.status['BTC']*4000, '$ pseudo]')
		#print('[Total have aprox.:', self.status[coin_name]*0.0000004*4000 + self.status['BTC']*4000, '$ pseudo]')