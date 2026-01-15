def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

def rotate_array(array, k):
    n= len(array)
    k= k % n
    reverse(array, 0, n - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, n - 1)
    return array

# test
print(rotate_array([1,2,3,4,5   ],8 ))