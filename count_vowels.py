def count_vowels(s,l):
    if l<0:
        return 0
    else:
        if s[l] in "AEIOUaeiou":
            return (count+count_vowels(s,l-1))
        else:
            return count_vowels(s,l-1)
s=input("Enter a string: ")
l=len(s)
count=1
print("Count of vowels in the string:",count_vowels(s,l-1))