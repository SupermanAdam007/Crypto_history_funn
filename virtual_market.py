

class Market(object):

	
	def __init__(self, btc_init, bcn_init, commision=0.0015, max_opens=10):
		self.have_btc = btc_init
		self.have_bcn = bcn_init
		self.commision = commision
		self.buys_sells = 0
		self.max_opens = max_opens


	def buy_bcn(self, amount, price_btc, verbose=False):
		if self.buys_sells == self.max_opens:
			if verbose:
				print('buys_sells == '+str(self.max_opens)+':', self.buys_sells == self.max_opens)
			return ''

		if amount*price_btc*(1+self.commision) > self.have_btc:
			if verbose:
				print('Don\'t have enough BTC')
				print('\tHave:', self.have_btc)
				print('\tNeed:', amount*price_btc)
			return ''

		self.have_bcn += amount - amount*self.commision
		self.have_btc -= amount*price_btc

		self.buys_sells += 1

		if verbose:
			print('# Buy BCN: amount =', amount, 
				'### price_btc =', price_btc)
			self.print_have()

		return 'a'


	def sell_bcn(self, amount, price_btc, verbose=False):
		if self.buys_sells == -self.max_opens:
			if verbose:
				print('buys_sells == -'+str(self.max_opens)+':', self.buys_sells == -self.max_opens)
			return ''

		if self.have_bcn < amount*(1+self.commision):
			if verbose:
				print('Don\'t have enough BNC')
			return ''

		self.have_bcn -= amount 
		self.have_btc += amount*price_btc - amount*self.commision*price_btc

		self.buys_sells -= 1
		
		if verbose:
			print('# Sell BCN: amount =', amount, 
				'### price_btc =', price_btc)
			self.print_have()

		return 'a'


	def print_have(self):
		print('have_bcn =', self.have_bcn)
		print('have_btc =', self.have_btc, 
			'[aprox. ', self.have_btc*4000, '$ pseudo]')
		print('Total have aprox.:', self.have_bcn*0.0000004*4000 + self.have_btc*4000, '$ pseudo')