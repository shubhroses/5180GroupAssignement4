# Python 3.0
import numpy as np
# import other modules as needed


class pagerank:
	
	def pagerank(self, input_file, alpha = 0.15):
		# function to implement pagerank algorithm
		# input_file - input file that follows the format provided in the assignment description
		transition_mat = self.get_transition_mat_with_tp(input_file, alpha)
		initial_vector = self.get_init_vector(len(transition_mat))

		# change_sum = 1
		# while changeSum > 0.001:
		iterations = 14
		# calc xP^k power vectors each iteration, until threshold
		for _ in range(iterations):
			old_vector = initial_vector
			print(old_vector)
			initial_vector = self.power_iteration(initial_vector, transition_mat)
			# change_sum = np.sum(abs(oldVector - initialVector))

		page_rank = initial_vector.tolist()[0]
		page_rank_to_id = [(value, i) for i, value in enumerate(page_rank)]
		page_rank_to_id = sorted(page_rank_to_id, reverse = True)

		for value, id in page_rank_to_id:
			print(f"Page id: {id}, Page rank: {value}")

	def get_adj_mat(self, input_file):
		# Read input file
		with open(input_file) as f:
			lines = f.readlines()
		lines = [line.strip() for line in lines]
		pages = int(lines[0])

		# init the adjacency mat
		mat = [[0] * pages for _ in range(pages)]

		# insert edges into mat, skip line 1,2
		for line in lines[2:]:
			edge = [int(l) for l in line.split()]
			x, y = edge
			mat[x][y] = 1

		return mat

	def get_transition_mat_with_tp(self, input_file, alpha):
		mat = self.get_adj_mat(input_file)
		n = len(mat)

		# modify the adj mat to have prob to tp
		for row in range(len(mat)):
			edges = sum(mat[row])

			# dead-ends prob to tp as 1/n
			if edges == 0:
				for col in range(len(mat[0])):
					mat[row][col] = 1 / n

			# non-dead-ends prob to tp in proportion to 1/edges
			else:
				for col in range(len(mat[0])):
					if mat[row][col] == 1:
						mat[row][col] = 1/edges

		# lastly, mult the mat by tp rate alpha & add alpha/N to every entry
		mat = np.matrix(mat)
		mat = mat * (1-alpha)
		mat = mat + (alpha / n)

		return mat
	
	def get_init_vector(self, n):
		v = np.array([1/n for _ in range(n)])
		return v

	def power_iteration(self, x, p):
		return x.dot(p)


if __name__ == "__main__":
	pr = pagerank()
	# print(f"For file test1.txt")
	# pr.pagerank('groupassignment4/pagerank/test1.txt')
	# print(f"For file test2.txt")
	# pr.pagerank('groupassignment4/pagerank/test2.txt')
	print(f"For file test3.txt")
	pr.pagerank('test3.txt', alpha=0.14)