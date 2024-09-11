n=int(input("Enter the size: "))
arr=[]
unique_arr=[]
val=0
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    arr.append(a)
print(arr)
for i in range(n-1):
    print(arr[i])
    if(arr[i]==0):
        i=i+1
        print("arr[i+1]",arr[i])
        for j in range(i+1,n):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            print("temp",temp,"arr[i]",arr[i],"arr[j]",arr[j])
        arr[i]=0
        
print(arr)
