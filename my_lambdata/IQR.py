


import numpy as np




def removeOutliers(x):
	   a = np.array(x)
	   upper_quartile = np.percentile(a, 75)
	   lower_quartile = np.percentile(a, 25)
	   IQR = (upper_quartile - lower_quartile) * 1.5
	   quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
	   resultList = []
	   for y in a.tolist():
        	if y >= quartileSet[0] and y <= quartileSet[1]: 
        		resultList.append(y)
        	return resultList   
	      