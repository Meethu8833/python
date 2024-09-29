class Odd_even:
    def check(self,a):
        if a%2==0:
            print(a,"is even")
        else:
            print(a,"is odd")

class Main:  
        a=int(input("Enter the number: "))
        c=Odd_even()
        c.check(a)



