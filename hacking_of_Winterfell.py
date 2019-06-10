class Solution:

	def run(self, first_strike_army_name, no_of_dragons, no_of_white_lords):
		# first_strike_army_name = "Seven Kingdom Army"
		# no_of_dragons = 3
		# no_of_white_lords = 5

		ska = SKArmy(no_of_dragons)
		wwa = WWArmy(no_of_white_lords)

		count = 0
		while ska.units()>0 and wwa.units()>0:

			if first_strike_army_name == "Seven Kingdom Army":
				ska.attack_to(wwa)
				wwa.attack_to(ska)
			else:
				wwa.attack_to(ska)
				ska.attack_to(wwa)
			count += 1

		result = '{}|{}'.format("Seven Kingdom Army" if ska.units()>0 else "White Walker Army", count)
		return result

#-----------------------------------------------------------------------------

class Units:

	def __init__(self, n, attack, defense):
		self.n = n
		self.attack = attack
		self.defense = defense

	def total_damage(self):
		return self.n*self.attack

	def total_defense(self):
		return self.n*self.defense

	def get_damage(self, damage):
		spare = self.total_defense()-damage
		print("before n {}, at {}, def {}, dam {}, spare {}, tdef {}".format(self.n, self.attack, self.defense, damage, spare, self.total_defense()))
		if spare<=0:
			self.n = 0
			spare *= -1
		else:
			# self.n = 0
			self.n = int(math.ceil(float(spare)/self.defense))
			spare = 0

		print("after n {}, at {}, def {}, spare {}".format(self.n, self.attack, self.defense, spare))

		return spare


class Army:

	def __init__(self, name, large_units, small_units):
		self.large = large_units
		self.small = small_units
		self.name = name

	def attack_power(self):
		return self.large.total_damage()+self.small.total_damage()

	def receive_damage(self, damage):
		print(self.name, "received", damage)
		damage = self.large.get_damage(damage)
		damage = self.small.get_damage(damage)


	def units(self):
		return self.large.n + self.small.n

	def attack_to(self, army):
		damage = self.attack_power()
		army.receive_damage(damage)

class SKArmy(Army):

	def __init__(self, n_dragons):
		super().__init__("Seven Kingdom Army", Dragons(n_dragons), Infantry())

class WWArmy(Army):

	def __init__(self, n_lords):
		super().__init__("White Walker Army", White_Lords(n_lords), WWInfantry())


class Dragon(Units):

    def __init__(self):
        super().__init__(n, 600, 600)

class Infantry(Units):

    def __init__(self):
        super().__init__(5000, 2, 2)

class Ww(Units):

    def __init__(self):
        super().__init__(n, 50, 100)

class ww_inf(Units):

    def __init__(self):
        super().__init__(10000, 1, 3)


#
# class Army:
#
#     def __init__(self, l, s):
#         self.l = l
#         self.s = s
#
#     def units(self):
#         return self.l.n + self.s.n
#
# class SKArmy(Army):
#
#     def __init__(self, numOfDrag):
#         self.numOfDrag = numOfDrag
