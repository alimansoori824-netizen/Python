# Not working
n = int(input("Enter number: "))
x, y = n, n
count = 0
sum = 0

while n > 0:
    count += 1
    n = n // 10

while x > 0:
    digit = x % 10
    sum = sum + digit ** count
    x = x // 10

if y == sum:
    print("It's an Armstrong number")
else:
    print("Not an Armstrong number")