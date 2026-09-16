def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	def mean(nums: list[float]):
		sum_ = 0
		for num in nums:
			sum_ += num
		return sum_ / len(nums)

	if len(matrix) == 0 or len(matrix[0]) == 0:
		raise ValueError(f"matrix must be non-empty, got shape {len(matrix)}x0")

	means = []
	if mode == 'row':
		for row in matrix:
			means.append(mean(row))
	elif mode == 'column':
		for col in zip(*matrix):
			means.append(mean(col))
	else:
		raise ValueError(f"mode must be 'row' or 'column', got {mode!r}")

	return means