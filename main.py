from random import randint, shuffle


class MontyHall:
	def __init__(self, iterations: int = 1000):
		self.variants = ['Goat', 'Goat', 'Car']
		self.wins = 0
		self.iterations = iterations
		self.rechoose = False

	def __repr__(self):
		loses = self.iterations - self.wins
		return f"""
			Iterations: {self.iterations} 
			Wins: {self.wins}
			Losses: {loses}"""

	def __reset(self):
		self.variants = ['Goat', 'Goat', 'Car']
		shuffle(self.variants)

	def reset(self):
		self.wins = 0
		self.__reset()

	def switch_mode(self):
		self.rechoose = not self.rechoose


	def start(self):
		for _ in range(self.iterations):
			random_index = randint(0, 2)
			choice = self.variants.pop(random_index)

			random_remaining_index = randint(0, 1)
			if self.variants[random_remaining_index] == 'Car':
				stay = self.variants.pop(random_remaining_index)
				door_with_goat = self.variants[0]
			else:
				door_with_goat = self.variants.pop(random_remaining_index)
				stay = self.variants[0]

			if door_with_goat != 'Goat':
				raise Exception('Goat not chosen')

			if self.rechoose:
				choice = stay

			if choice == 'Car':
				self.wins += 1

			self.__reset()


if __name__ == '__main__':
	monty_hall = MontyHall()

	monty_hall.start()
	print('if not rechoose')
	print(monty_hall)

	monty_hall.reset()
	monty_hall.switch_mode()

	monty_hall.start()
	print('if rechoose')
	print(monty_hall)