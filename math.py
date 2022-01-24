# add implementation
def add(x,y);
	return (x+y)

# subtract implementation
def sub(x,y):
	if(x>y):
		return x-y
	else:
	return y-x       

#multiply implementation
def mul(x,y):
    return x*y

# divide implementation
def div(x,y):
    if y==0:				#on master branch
	return DIVIDE_BY_0_ERROR  
    else:
	return x/y

