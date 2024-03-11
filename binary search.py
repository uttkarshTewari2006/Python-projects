#binary search

def binarySearch(list , item):

  lenList = len(list)

  if lenList<=3:
    return item in list
  halfWayPoint = int(lenList/2)

  if list[halfWayPoint]>item:
    return binarySearch(list[:halfWayPoint], item)

  if list[halfWayPoint]<item:
    return binarySearch(list[halfWayPoint+1::], item)

  if list[halfWayPoint] == item:
    return True


#test
binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],17)
sorted_array_1 = list(range(1, 10001))  # Array from 1 to 10000
sorted_array_2 = list(range(0, 100000, 2))  # Even numbers from 0 to 99998
sorted_array_3 = list(range(-5000, 5001))  # Array from -5000 to 5000

assert binarySearch(sorted_array_1,2345)==True
assert binarySearch(sorted_array_2,2345)==False
assert binarySearch(sorted_array_3 , -2345) == True

binarySearch(sorted_array_3,2345)
# Arrays with duplicate elements
duplicates_array_1 = [1] * 10000 + [2] * 10000  # Alternating 1s and 2s
duplicates_array_2 = [3] * 5000 + [6] * 5000  # Alternating 3s and 6s
assert binarySearch(duplicates_array_1,2345) == False
assert binarySearch(duplicates_array_1, 2) == True
assert binarySearch(duplicates_array_2,2345) == False
assert binarySearch(duplicates_array_2,6) == True

# Randomized arrays
import random
random_array_1 = random.sample(range(1, 10001), 10000)  # Random permutation of 1 to 10000
random_array_2 = random.sample(range(-5000, 5001), 10000)  # Random permutation of -5000 to 5000

assert binarySearch(sorted(random_array_1),2345) == (2345 in random_array_1)

assert binarySearch(sorted(random_array_2),2345) == (2345 in random_array_2)

# Edge cases
empty_array = []  # Empty array
single_element_array = [42]  # Array with a single element