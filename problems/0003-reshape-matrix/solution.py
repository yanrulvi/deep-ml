import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
		return []
		
	reshaped_matrix = [[0] * new_shape[1] for _ in range(new_shape[0])]
	for i in range(len(a)):
		for j in range(len(a[0])):
			idx = i * len(a[0]) + j
			new_i = idx // new_shape[1]
			new_j = idx % new_shape[1]
			reshaped_matrix[new_i][new_j] = a[i][j]
	return reshaped_matrix