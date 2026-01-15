def sorted_squares(array):
    n = len(array)
    left = 0
    right = n - 1
    result = [0] * n

    for i in range(n - 1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] ** 2
            left += 1
        else:
            result[i] = array[right] ** 2
            right -= 1

    return result

# test
nums = [-7,-3,2,3,11]
print(sorted_squares(nums))