def count_words(sen,l):
    if l<0:
        return 0
    else:
        if sen[l]==" ":
            return (count+count_words(sen,l-1))
        else:
            return count_words(sen,l-1)
        
sen=input("Enter the sentence: ")
l=len(sen)
count=1
print("The number of words in the sentence is:",count_words(sen,l-1)+1)