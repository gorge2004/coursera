""" 
def call_cost_calculate(call):
	docstring
	cost = 0
	if call.is_local():
		cost = calculate_local_cost_of(call)
	else:
		cost = calculate_national_cost_of(call)
	return cost """


class CallCostCalculator(object):
	@classmethod
	def to_handle(klass, call):
		pass
	
	def calculate(self):
		raise NotImplementedError('subclass responsability')

class  LocalCallCostCalculator(CallCostCalculator):
	def calculate(self):
		pass

class NationalCallCostCalculator(CallCostCalculator):
	def calculate(self):
		pass
	
class InternationalCallCostCalculator(CallCostCalculator):
	def calculate(self):
		pass
		
cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()