arr=[0,1,2,3,5,6,7,8,9]

def missing(arr):
    a=len(arr)
    
    total=a*(a+1)//2
    atcual=sum(arr)

    missing_num=total-atcual

    return missing_num

A=missing(arr)
print("The missing number in the Given Array is:",A,arr)