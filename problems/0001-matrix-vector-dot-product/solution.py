def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	def dot(a: list[int|float], b: list[int|float]):
		res_dot = 0
		for i in range(len(a)):
			res_dot += a[i] * b[i]
		return res_dot

	res = [0] * len(a)
	for i in range(len(a)):
		if len(a[i]) != len(b):
			return -1
		res[i] = dot(a[i], b)

	return res