s1={4,1,6,7}
s2={'a','b','c','d'}
s3=list(zip(s1,s2))
print(s3)

a1=[1,4,3,2,5,8,6,7,9]
a2=[10,40,30,20,50,80,60,70,90]
for x,y in zip(a1[::-1],a2[::-1]):
    print(x,y)

d1=['reliance', 'infosys', 'tata']
d2=[100,200,300]

newd={d1:d2 for d1,d2 in zip(d1,d2)}
print("\n",newd)

a=('a','b','c','d')
b=('apple', 'banana', 'cherry', 'durian')
x=zip(a,b)
print(list(x))