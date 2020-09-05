

class Money():
	def __init__(self, sum: str, currency: str):
		self.sum = str(sum)
		self.currency = currency
		a = self.sum.replace(',', '.').split('.')
		self.int_part = int(a[0])
		self.change_part = int(a[1])		
		
	def choose_currency(self):
		curr_dct = {
		'hrivna': 
			{'int_': ('гривна', 'гривны', 'гривен'),
			'change_': ('копейка', 'копейки', 'копеек')},
		'dollar':
			 {'int_': ('доллар', 'доллара', 'долларов'),
			 'change_': ('цент', 'цента', 'центов')},
		 'pound':
			{'int_': ('фунт', 'фунта', 'фунтов'),
			'change_': ('пенс', 'пенса', 'пенсов')},
		 }
		if self.currency in curr_dct.keys():
			return curr_dct[self.currency]
			
	def choose_plural(self, value, noun):		
		if value == 1:
			res = f'{str(value)} {noun[0]}'
		elif 2 <= value <=4:
			res = f'{str(value)} {noun[1]}'
		elif 5 <= value <=19:
			res = f'{str(value)} {noun[2]}'
		elif value >= 20:
			huge_value = str(value)
			if huge_value[-1] is "1":
				res = f'{str(huge_value)} {noun[0]}'
			elif (huge_value[-1] is "2") or (huge_value[-1] is "3") or (huge_value[-1] is "4"):
				res = f'{str(huge_value)} {noun[1]}'
			else:
				res = f'{str(huge_value)} {noun[2]}'
		return res
			
	def formatting(self):
		money = self.choose_currency()
		if money:
			f0 = self.choose_plural(self.int_part, money['int_'])
			f1 = self.choose_plural(self.change_part, money['change_'])
			return (f0, f1)
		else:
			return f"Unable to display data"
			
	def view_results(self):
		res = self.formatting()
		if isinstance(res, tuple):
			print(' '.join(self.formatting()))
		else:
			print(f'Carrency {self.currency} does not found')
			print(self.formatting())
	
	@property
	def curr(self):
		return self.currency	
	@curr.setter
	def set_carrency(self, value):
		self.currency = value	
	
	@property
	def ints(self):
		return self.int_part
	@ints.setter
	def set_int_part(self, value):
		self.int_part = value
	
	@property
	def changes(self):
		return self.change_part
	@changes.setter
	def set_change_part(self, value):
		self.change_part = value

		
if __name__ == '__main__':
	mon = Money(4.97, 'pound')
	mon.view_results()
	mon.set_carrency = 'hrivna'
	mon.set_int_part = 13
	mon.set_change_part = 71
	mon.view_results()
