'''
Question:

Two Sum - You are given an array of Integers and another integer targetValue.
Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.
Try:

Try to optimise your solution and arrive at a Time Complexity of O(n)
'''


def two_sum(array, target):

    hash_map = {}

    for idx, num in enumerate(array):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], idx]
        hash_map[num] = idx

    return []

# test
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2,7, 11, 5], 11))

'''
complexities:
Time Complexity:    O(N)
Space Complexity:   O(N)
'''
