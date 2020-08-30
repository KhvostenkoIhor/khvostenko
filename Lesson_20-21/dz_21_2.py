

class Book():
	'''Simple model of the book'''
	book_count = 0
	
	def __init__(self, name):
		self.book_name = name.title()
		self.author = ''
		self.year = ''
		self.pages = 0
		self.genre = ''
		self.price = 0
		Book.book_count += 1
		
	def set_author(self, *author: str):
		if author:
			author = str(author)
			self.author = author[2:-3].title()
		else:
			self.author = input('Enter the name of author of the book: ').title()
		return self.author
	
	def set_year(self, *year):
		if year:
			year = str(year)
			self.year = year[1:-2]
		else:
			self.year = input('Enter the book release year: ')
		return self.year
		
	def set_pages(self, *pages):
		if pages:
			pages = str(pages)
			self.pages = pages[1:-2]
		else:
			self.pages = input('Indicate the number of pages in the book: ')
		return self.pages
		
	def set_genre(self, *genre):
		if genre:
			genre = str(genre)
			self.genre = genre[2:-3].title()
		else:
			self.genre = input('Indicate the genre of the book: ').title()
		return self.genre
		
	def set_price(self, *price):
		if price:
			self.price = price
		else:
			self.price = input('Enter the book price: ')
		return self.price
	
	def book_description(self):
		new_book = {
	'Book title': self.book_name,
	'Author': self.author,
	'Release year': self.year,
	'Pages': self.pages,
	'Genre': self.genre,
	'Price': self.price,	
		}
		for key, value in new_book.items():
			print(key, value, sep=': ')
		print()
		return new_book
		
if __name__ == '__main__':
	book1 = Book('черновик')
	book1.set_author()
	book1.set_year()
	book1.set_pages()
	book1.set_genre()
	book1.set_price()
	#book2 = Book()
	print(book1.price)
	book1.book_description()
	#book2.book_description()
			
