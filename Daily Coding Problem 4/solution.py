def get_all_positive_numbers(arr):
    i=1
    j=0
    temp=0
    for x in range(0,len(arr)-1):
        if arr[i] < arr[j] and arr[i] < 0:
            temp = arr[j]
            arr[j]=arr[i]
            arr[i] = temp
            j = j + 1
        i = i+1
    print arr
    return j

def get_missing_positive(arr,start_index):
    positive_arr = arr[start_index:]
    size = len(positive_arr)
    for x in range(0,size):
        current = positive_arr[x]
        if current-1 < size:
           if positive_arr[abs(current) - 1] > 0:
                positive_arr[abs(current)-1] = -positive_arr[abs(current)-1]

    for x in range(0,size):
        if positive_arr[x] > 0:
            return x+1

    return size


#The idea is after filtering the negative numbers
#we check that every element is existing by marking it index value negative
#arr[0]=2 then we mark the element at arr[2-1] negative
#if all the elements are negative then we return the last index+1 or simply the size


arr = [3, 4, -1, 1]
positive_index = get_all_positive_numbers(arr)
missing = get_missing_positive(arr,positive_index)
print missing
