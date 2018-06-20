def find_product(arr):
    #left = list(range(0,len(arr)-1))
    left = [None] * len(arr)
    right = [None] * len(arr)
    product = [None] * len(arr)
    left[0] = 1
    right[len(arr)-1] = 1
    #construct the left array
    for x in range(1,len(arr)):
        left[x] = left[x-1] * arr[x-1]

    #construct the right array
    for y in range(len(arr)-2,-1,-1):
        right[y] = right[y+1]*arr[y+1]

    for x in range(0,len(arr)):
        product[x] = left[x]*right[x]

    return product




arr = [1,2,3,4,5]
print find_product(arr)
