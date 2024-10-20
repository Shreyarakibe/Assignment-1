def second_largest(arr):
    a=arr[0]
    for i in arr:
        for j in arr:
            if j<i:
                if j>a:
                    a=j
    return a

arr=[11,45,98,45,67,32,67,85,35,76,35]
Second_largest=second_largest(arr)
print("The Second Largest Element is:",Second_largest)   