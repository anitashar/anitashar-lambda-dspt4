


import numpy as np




def removeOutliers(x):
	"""
	remove outliers in a series

	param: x(numeric) 

	return outlier

	"""
	a = np.array(x)
	upper_quartile = np.percentile(a, 75)
	lower_quartile = np.percentile(a, 25)
	IQR = (upper_quartile - lower_quartile) * 1.5
	quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
	resultList = []
	
	for y in np.nditer(a):
		print(y)
		
		if y <= quartileSet[0] or y >= quartileSet[1]: 
			resultList.append(y)
	return resultList   
	      

if __name__ == "__main__":

	print(removeOutliers([-10,2,5,3,8,4,7,5,10,99,1000]))

