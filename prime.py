# a Program which has function to find out a number is prime or not
def prime(n):
    pri = 0
    for i in range(2, n):
        if n % i == 0:
            pri = pri + 1
    return pri


n = int(input("Enter a number = "))
if prime(n) == 0:
    print("It is aPrime number.")
else:
    print("It is a Not prime number.")