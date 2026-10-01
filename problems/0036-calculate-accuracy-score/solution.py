import numpy as np

def accuracy_score(y_true, y_pred):
	numerator = np.where(y_true == y_pred, 1, 0).sum()
	return numerator / len(y_true)