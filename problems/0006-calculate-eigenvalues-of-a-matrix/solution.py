import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	disc = trace ** 2 - 4 * det
	eigenvalue_1 = (trace + math.sqrt(disc)) / 2
	eigenvalue_2 = (trace - math.sqrt(disc)) / 2
	return [eigenvalue_1, eigenvalue_2]