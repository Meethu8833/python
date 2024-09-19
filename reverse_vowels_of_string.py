vowel_list=[]

def rev_vowels():
    for i in s:
        if i in "AEIOUaeiou":
            vowel_list.append(i)
    a=vowel_list[::-1]
    
    j=0
    string=""
    for i in s:
        if i in "AEIOUaeiou":
            string=string+a[j]
            j+=1
        else:
            string=string+i
    
    print(string)

s=input("Enter a string: ")
rev_vowels()