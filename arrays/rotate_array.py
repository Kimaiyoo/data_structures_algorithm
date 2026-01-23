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
print( "\n Test 1:")
print(rotate_array([1,2,3,4,5],8 ))

# when given no. of times to rotate
def rotate_array_2(array, k, times):
    n= len(array)

    k = (k * times) % n # get total steps

    reverse(array, 0, n - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, n - 1)
    return array

print( "\n Test 2:")
print(rotate_array_2([1,2,3,4],2, 4 ))
print(rotate_array_2([1,2,3,4,5],3, 3 ))

def rotate_list(nums, k, times):
    n = len(nums)
    k = (k * times) % n
    rotated = nums[-k:] + nums[:-k]
    return rotated
print( "\n Test 3:")
print(rotate_list([1,2,3,4],2, 4 ))
print(rotate_array_2([1,2,3,4,5],3, 3 ))