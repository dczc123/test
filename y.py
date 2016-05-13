def append_if_even(x,lst=[]):
	if x%2==0:
		lst.append(x)
	return lst

z=123
result=append_if_even(z)
print(result)    
