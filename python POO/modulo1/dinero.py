class Currency(object):
	def __init__(self, name, symbol, factor):
		self.name = name
		self.symbol = symbol
		self.factor = factor
	
	def convert_amount_to_base_currency(self, amount):
		return self.factor * amount

	def convert_amount_from_base_currency(self, amount):
		return amount / self.factor
	def __repr__(self):
		return self.name 

class Dinero(object):

	def __init__(self, cantidad, currency):
		self.cantidad = cantidad
		self.currency = currency

	def base_currency_amount(self):
		return self.currency.convert_amount_to_base_currency(self.cantidad)

	def __add__(self,anAmountOfMoney):
		cantidad = self.base_currency_amount() + anAmountOfMoney.base_currency_amount()
		cantidad = self.currency.convert_amount_from_base_currency(cantidad)
		return Dinero(cantidad, self.currency)

	def __sub__(self, anAmountOfMoney):
		cantidad = self.base_currency_amount() - anAmountOfMoney.base_currency_amount()
		cantidad = self.currency.convert_amount_from_base_currency(cantidad)
		return Dinero(cantidad, self.currency)

	def __mul__(self, anAmount):
		
		return Dinero(self.cantidad * anAmount , self.currency)
	
	def __truediv__(self,anAmount):
	
		return Dinero(self.cantidad / anAmount , self.currency)
	
	def __repr__(self):
		return '{} ({})'.format(self.currency.symbol,self.cantidad)


dolar = Currency('Dolar', 'USD$', 140)
pesos = Currency('Pesos', 'ARG$',1)

cuenta_pesos = Dinero(1, pesos)
cuenta_Dolares = Dinero(1, dolar)

print('cuenta_pesos', cuenta_pesos )



