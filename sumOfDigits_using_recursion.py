def sum_of_digits(n):
    if n==0:
        return 0
    else:
        rem=n%10
        n=int(n/10)
        return (rem+sum_of_digits(n))

n=int(input("Enter the number: "))
print("The sum of digits is:",sum_of_digits(n))
