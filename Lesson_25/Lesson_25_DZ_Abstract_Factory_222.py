
class HeroFact():
	@classmethod
	def create_hero(Class, name):
		return Class.Hero(name)
		
	@classmethod
	def create_weapon(Class):
		return Class.Weapon()
		
	@classmethod
	def create_spell(Class):
		return Class.Spell()
		
class WarriorFact(HeroFact):
	class Hero:
		def __init__(self, name):
			self.name = name
			self.spell = None
			self.weapon = None
			
		def hit(self):
			print(f'Warrior {self.name} hits with {self.weapon.hit()}')
			self.weapon.hit()
			
		def cast(self):
			print(f'Warrior {self.name} casts {self.spell.cast()}')
			self.spell.cast()
			
		def add_weapon(self, weapon):
			self.weapon = weapon
			
		def add_spell(self, spell):
			self.spell = spell		
		
	class Weapon():
		def hit(self):
			return 'Claymore'
	
	class Spell():
		def cast(self):
			return 'Power'

def create_hero(factory):
	hero = factory.create_hero('Nagibator')
	
	weapon = factory.create_weapon()
	spell = factory.create_spell()
	
	hero.add_weapon(weapon)
	hero.add_spell(spell)

	return hero

player = create_hero(WarriorFact())
player.cast()
player.hit()



















