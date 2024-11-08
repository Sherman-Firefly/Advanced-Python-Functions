#Hands on map

num1=[1,3,5]
num2=[2,4,6]
ans=map(lambda x, y:x+y, num1,num2)
print("Adding 2 lists")
print(list(ans))

num3=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num3))
print("Squares")
print(square)