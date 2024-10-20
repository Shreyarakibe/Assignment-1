def largest(arr):
    a=arr[0]
    for i in arr:
        if i>a:
            a=i
    return a


arr=[11,45,98,45,67,32,67,85,35,76,35]
largest=largest(arr)
print("The Largest Element is:",largest)