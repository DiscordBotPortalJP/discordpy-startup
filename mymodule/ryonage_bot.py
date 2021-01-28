class RyonageBot:
	max_hp = 150
	def __init__(self):
		self.hp = 150
		
	def get_hp(self):
		return self.hp
	
	def damage(self, n):
		self.hp -= n
		return self.hp
	
	def heal(self, n):
		self.hp += n
		if max_hp < self.hp:
			self.hp = 150
		return self.hp
