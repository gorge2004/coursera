
def customer_with_name(letter):
	selected_customers = []
	for customer in customers:
		if customer.name.startswith(letter):
			selected_customers.append(customer)
	return selected_customers

def overdraw_accounts():
	selected_accounts = []
	for account in accounts:
		if account.is_overdraw():
			selected_accounts.append(account)
	return selected_accounts


def select(object, condition):
	""" filtra los objectos segun la condicion
	 y los regresa en una lista 
	"""
	selected = []
	for an_object in objects:
		if codition(an_object):
			
			selected.append(an_object)
	return selected

select(customers, lambda customer: customer.name.startswith(letter) )
select(customers, lambda account: account.is_overdraw()) )