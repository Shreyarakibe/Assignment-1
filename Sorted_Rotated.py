arr=[1,5,2,4,3]
def sort(arr):
    a=len(arr)
    for i in range(a):
        for j in range(0,a-i-1):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return(arr)


def rotate(n,arr):
    n=n%len(arr)
    return arr[-n:]+arr[:-n]

n=2
a=sort(arr)
b=rotate(n,arr)
print("Sorted Array:",a)
print("Rotated Array",b)