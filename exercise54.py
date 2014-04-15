# This is where Exercise 5.4 goes
# Name: Tyler

def is_triangle(a,b,c):
	if a > b+c:
		return "No"
	elif b > a + c:
		return "No"
	elif c > a + b:
		return "No"
	else:
		return "Yes"
	
raw_a = (raw_input('Enter your first stick length -->'))
raw_b = (raw_input('Enter your second stick length -->'))
raw_c = (raw_input('Enter your third stick length -->'))

print is_triangle(int(raw_a),int(raw_b),int(raw_c))
