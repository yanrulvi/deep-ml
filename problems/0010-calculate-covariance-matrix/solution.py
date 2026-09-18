def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n = len(vectors)
	m = len(vectors[0])

	means = []
	for i in range(n):
		sum_ = 0
		for j in range(m):
			sum_ += vectors[i][j]
		means.append(sum_ / m)

	res = [[0] * n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			sum_ = 0
			for k in range(m):
				sum_ += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
			res[i][j] = sum_ / (m - 1)
	return res