class Printer():

	def __init__(self, rows, cols, lane):
		self.rows = rows
		self.cols = cols
		self.lane = lane	

	def print_board(self, cars, points):
		print "==> Printing the Board <=="
		for row in range(0, self.rows):
			out = ""
			for col in range(0, self.cols):
				if (points.__contains__((col, row))):
					out += str(points[(col, row)])
				else:
					out += "."
				if (col == self.lane + 1):
					out += "|"
				else:
					out += " "
				out += "        "
				if (col == self.lane - 1):
					out += "|"
				else:
					out += " "
			print out
			line = ("          " * self.lane) + "  |            |"
			print line
			print line
		print "==> End of the Board <=="
