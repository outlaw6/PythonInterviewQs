# Python INterview Qs
# Input : "aaaabbbcc"
# Output : (("a", 4), ("b", 3), ("c", 2))
# Write a function

def f1(s1):
	# Expects a string

	l1 = list(set(s1))
	dik = {}
	for char in l1:
		dik[char] = 0
	for char in l1:
		c=0
		while c < len(s1):
			if char == s1[c]:
				dik[char] += 1
				c+=1
			else:
				c+=1
	return dik
print(f1('aaaabbbcc'))