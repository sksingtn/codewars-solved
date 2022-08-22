def find_even_index(arr):
    for i in range(len(arr)):
        left = sum(arr[0:i]) if arr[0:i] != [] else 0
        right = sum(arr[i+1:]) if arr[i+1:] != [] else 0
        if left == right:return i
    else:
        return -1


find_even_index([1,2,3,4,3,2,1])
