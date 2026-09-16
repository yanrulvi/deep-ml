def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	def mean(nums: list[float]):
		sum_ = 0
		for num in nums:
			sum_ += num
		return sum_ / len(nums)
		
	means = []
	if mode == 'row':
		for row in matrix:
			means.append(mean(row))
	elif mode == 'column':
		for j in range(len(matrix[0])):
			column = [matrix[i][j] for i in range(len(matrix))]
			means.append(mean(column))
	
	return means