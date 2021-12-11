#
# Linked List
#
'''class LList(object):
	def __init__(self, name,  previous = 0, pointing = 0):
		self.name = name
		self.previous = previous
		self.pointing = pointing

	def prev(self, prev):
		self.previous = prev.name

	def pointing(self, point):
		self.pointing = point.name


	def __str__(self):
		return str("preceded by: --->" + str(self.previous) +"\t"+ str(self.name)  + "pointing to --->" + str(self.pointing))
n = LList(1)
print(n)
b = LList(2)
#print(b)
b.prev(n)
n.pointing(b)'''

#arr = [4,3,1,2]

c=0

'''for i in range(len(arr)-1):
	for j in range(len(arr)-1):
		if arr[j]  > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)'''

	



'''temp = [0] * len(arr)
print(temp)
for index, value in enumerate(arr):
	
	temp[value-1] = index
print(arr)
print(temp)'''

'''for i in range(len(arr)):
	if arr[i] != i+1:
		t = temp[i]
		print("ovo je t: ", t, "ovo je i:", i)
		print(arr[i], arr[t], i ,temp, temp[i])
		arr[i], arr[t] = i+1, arr[i]
		temp[i], temp[arr[t]-1] = i, t
		c+=1
print(c)'''
'''s=0
for i in range(len(arr)):
	c=0
	while arr[i] != i+1:

		print(arr)
		print(arr[i], i)
		temp = arr[i]-1
		print(temp)
		arr[i], arr[temp] = arr[temp], arr[i]

		print(arr)
		s+=1
		c+=1
	print("C:", c)
print(s)
print(arr)

'''
'''queries =  [ [1,5,3], [4,7,5] ]

arr = [0] * 10
print(arr)
for i in queries:
	print(i)
	for n in range(int(i[0]), int(i[1])+1):
		#print(n, i[2])
		arr[n-1] += i[2]
	print(arr)


print(arr)
'''
#arr = [1,2,3,4,5]
'''arr = [2,3,5,1,4]
p1 = 1
p2=2
p3=3
tBr=0

for x in range(len(arr)):
	#print(arr[x])
	if (arr[x] == p1):
		#print("Inside")
		p1=p2
		p2=p3
		p3+=1

	elif (arr[x] == p2):
		#print("Ins2")
		tBr+=1
		p2=p3
		p3+=1

	elif (arr[x] == p3):
		tBr+=2
		p3+=1

	else:
		#print("Too chaotic")
		pass

if tBr < 3:
	print(tBr)
else:
	print(tBr)
	print("Too CHaotic")

    
def funk(q):
    # Write your code here
    p1=1
    p2=2
    p3=3
    tBribes=0
    
    for i in range(len(q)):
       
        if (q[i] == p1):
            p1=p2
            p2=p3
            p3+=1
            #tBribes+=1
        
        elif (q[i] == p2):
            p2=p3
            p3+=1
            tBribes+=1
        elif (q[i] == p3):
            p3+=1
            tBribes+=2
        else:
            pass
            
    if tBribes >= 3:
        print(tBribes)
        print("Too chaotic")    
        #print(tBribes)
        #pass
    else:
        print(tBribes)

funk(arr)'''


'''s1='deified'

s2=len(s1)//2
p=True
for x in range(1,len(s1)):
	print(x, x-1)
	if s1[x-1] == s1[-x]:
		print("Ok")
		print(s1[x-1], s1[-x], x)
	else:
		print("out")
		p=False
		break
print("Word " + str(s1) + " is:" + str(p) + " palindrome")'''

'''v_v=0
for elm in x:
	for elm2 in x:
		if len(elm) == 1 and len(elm2) == 1:
			if ord(elm) == ord(elm2):
				print("Isti su", elm, elm2)
				v_v+=1
				continue

		elif (len(elm) > 1 and len(elm2) > 1) and (len(elm) == len(elm2)):
			print("Iste duzine, idem dalje")
			v1=0
			v2=0
			for chr in elm:
				v1+=ord(chr)
			for chr in elm2:
				v2+=ord(chr)

			print(v1, v2)
			if v1==v2:
				v_v+=1
				print("Jos jedan isti")

		else:
			print("Ne ide")
			pass

print(v_v)
'''
'''from collections import Counter
s1='ifailuhkqq'
x = ["".join(sorted(s1[i:j+1])) for i in range(len(s1)) for j in range(i, len(s1))]
print(x)



l1=[]


for i in range(len(s1)):
	for j in range(i, len(s1)):
		print(i, j)
		print(s1[i:j+1])
		l1.append(s1[i:j+1])

print(l1)
print(sorted(l1))

dikt = {}

for n in x:
	dikt[n] = 0

#print(dikt)

for n in x:
	dikt[n] += 1'''
#print(dikt)
v=0
'''for n in dikt:
	if dikt[n] > 1:
		print(dikt[n], n)
		if dikt[n] % 2 == 0:
			v+= dikt[n] // 2
		else:
			v+= dikt[n]'''
'''for n in dikt:
	v+=(dikt[n] * (dikt[n] -1) // 2)
print(v)

cntr = 0
c = Counter(x)
for key in c:
	#print(key)
	#print((c[key] * (c[key] -1) // 2))
	cntr+=(c[key] * (c[key] -1) // 2)
print(cntr)

arr = [1, 3, 9, 27, 81]
c=3
m=0
l1=[]
for i in range(0,len(arr)-2):

	#print(i,arr[i])

	

	if arr[i] * arr[i+1] == arr[i+2]:
		print(arr[i], arr[i+1], arr[i+2])
		m+=1
'''

'''r=2

arr = [1,2,2,4]

numbers = {}
pairs = {}
counter = 0

for i in arr[::-1]:

	if r*i in pairs:
		counter += pairs[r*i]
	if r*i in numbers:
		pairs[i] = pairs.get(i, 0) + numbers[r*i]

	numbers[i] = numbers.get(i,0)+1
	print(numbers.get(i,0), numbers[i])

print(numbers)
print(pairs)
print(counter)'''

'''from collections import Counter
def freqQuery(queries):
	strukt = []
	ret1 = []
	print("Here")
	print()
	for dat in queries:
		print(dat[0])
		if dat[0] == 1:
			strukt.append(dat[1])
		if dat[0] == 2:
			if dat[1] in strukt:
				strukt.remove(dat[1])
			else:
				pass
		if dat[0] == 3:
			n = Counter(strukt)
			if 
				if strukt.count(dat[1]) == dat[1]:
					ret1.append(1)
				else:
					ret1.append(0)
			else:
				pass
	print(strukt)     
	return ret1
'''
'''
queries = [ (1,1), (1,1), (1,1), (3,3) ]

print(freqQuery(queries))
'''
'''strukt = {1: 3, 2: 4}

for element in strukt:
	print(strukt[element])

q = [(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)]

q1 = [ (1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2) ]
q3 = [ (3,4), (2, 1003), (1, 16), (3,1) ]
q4 = [ (1,5), (1, 6), (3,2), (1,10), (1,10), (1,6), (2,5), (3,2) ]
q5 = [ (1,3), (2,3), (3,2), (1,4), (1,5), (1,5), (1,4), (3,2), (2,4), (3,2) ]
def freq(queries):
	strukt = {}
	ret1 = []
	for x in queries:
		print(x)
		if x[0] == 1:
			if x[1] not in strukt:
				strukt[x[1]] = 1
			elif x[1] in strukt:
				strukt[x[1]] += 1
		if x[0] == 2:
			if x[1] in strukt:
				strukt[x[1]] -= 1
			if x[1] not in strukt:
				pass
		if x[0] == 3:
			if x[1] in strukt.values():
				ret1.append(1)
			else:
				ret1.append(0)

	return ret1, strukt

queries = [ (1,1), (1,1), (1,1), (3,3) ]

print(freq(q5))

a = [6, 4, 1]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[i] > a[j+1]:
            a[i], a[j+1] = a[j+1], a[i]
print(a)
'''
'''k = 7
maks = []
cnt = 0
prices = [1,2,3,4]  
counter = 0
for i in prices:
	print(cnt)
	cnt += i
	print(cnt, cnt+1)
	if cnt <= k:
		counter += 1
print(counter)'''
'''for x in range(len(prices)-1,0,-1):
    counter=0
    temp=x
    cnt = 0
    print(temp)
    while cnt <= k and temp>=0:
    	print("PRva iteracija:", temp, cnt, counter)
    	cnt += prices[temp]
    	counter += 1
    	temp-=1
    	#print("PRva iteracija:", temp, cnt, counter)
    maks.append(counter)'''
'''from collections import deque
d=3
m=[x*10 for x in range(1,6)]
n=5
#print(x)
notifs = 0

def med():
	'''

'''for x in range(d, n-1):
	print("Trenutna iteracija: ", x)
	if len(m[:d]) % 2 == 1:
		#median = m[ len(m[:d]) // 2 ]
		median = m[len(m[:d]) // 2]
		print(median, m[d],)
		if m[x]*2 >= 2*median:
			notifs+=1

	if len(m[:d]) % 2 == 0:
		median = len(m) // 2
		m_median = (m[median] + m[median-1]) / 2.0
		if m[x] >= m_median:
			notifs+=1
	del m[0]
print(notifs)'''


l1 = [4,6,149,653,9,12]


def merge_sort(A):
	if len(A) > 1:

		left=A[:len(A)//2]
		right=A[len(A)//2:]
		print(left,right)

		merge_sort(left)
		merge_sort(right)
		i=j=k=0

		while i < len(left) and j < len(right):

			if left[i] <= right[j]:
				A[k] = left[i]
				i+=1
			else:
				A[k] = right[j]
				j+=1
			k+=1
		while i < len(left):
			A[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			A[k]=right[j]
			j += 1
			k += 1
merge_sort(l1)
print(l1)


