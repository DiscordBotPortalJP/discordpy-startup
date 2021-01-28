import random
class RyonageBot:
	max_hp = 150
	dying_hp = 70
	def __init__(self):
		self.hp = self.max_hp
		
	def get_hp(self):
		return self.hp
	
	def damage(self, n):
		#85%～115%までの乱数
		self.hp -= n *(85 + random.randint(0,30))/100 
		return self.hp
	
	def heal(self, n):
		self.hp += n
		if self.max_hp < self.hp:
			self.hp = self.max_hp
		return self.hp
