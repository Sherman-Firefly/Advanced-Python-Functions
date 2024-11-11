num=int(input("Input a number: "))

odds_under_in=[ i for i in range (1, num) if i%2 !=0]
odds_exam=[i for i in range (1, 31) if i%2 !=0]

print("Odd numbers under input", odds_under_in)
print("Odd numbers", odds_exam)

fruits=["apple", "banana", "cherry", "durian"]
cap=[fruit.capitalize() for fruit in fruits]

print(cap)