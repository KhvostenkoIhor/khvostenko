from abc import ABC, abstractmethod

class Chess(ABC):
	
	def kill(self):
		print(f'Fgiure kills some other figure...')

	@abstractmethod
	def move(self, *args):
		print(f'Figure moves to {args}')
		
class Pawn(Chess):
	def move(self, coordinates):
		coordinates = coordinates.split()
		self.position = {'x': coordinates[0], 'y': coordinates[1]}
		print(f'Figure moves to {coordinates}')
		return self.position
	
class Queen(Chess):
	def move(self, coordinates):
		position = {}
		coordinates = coordinates.split()
		position['x'] = coordinates[0]
		position['y'] = coordinates[1]
		print(f'Figure moves to {coordinates}')
		return position
		
p = Pawn()
q = Queen()
p.move('e2, e4')
p.kill()
q.move('d1, h5')
q.kill()

