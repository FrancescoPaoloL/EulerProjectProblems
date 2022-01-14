'''
Given an array 'nums' containing 'n' distinct
numbers in the range [0, n], return the only
number in the range that is missing from the
array

Example

	Input: nums = [3, 0, 1]
	Output: 2
	Explanation:
		n = 3 since there are 3 numbers, 
		so all numbers are in the range [0,3].
		'2' is the missing number in the range
		since it does not appear in nums.

Sum of natural numbers 1..N = N(N+1)2
'''
import random

def seriesSumGauss(n):
	return int(n*(n + 1) / 2)

# def missingNr(maxNr, numbers):
# 	complete = sum(range(0, maxNr + 1))
# 	partial = sum(numbers)
# 	return complete - partial

# def verify(n, nums):
# 	print(nums)
# 	print(f'Missing value is: {missingNr(n, nums)}')

def missingNr(maxNr, lstNumbers):
	partial = 0
	complete = seriesSumGauss(maxNr)
	for item in lstNumbers:
		partial += item
	return complete - partial

def verify(n, nums):
	print(nums)
	print(f'Missing value is: {missingNr(n, nums)}')


n = 3
nums =  [0, 3, 1]
verify(n, nums)

n = 9
nums =  [9,6,4,2,3,5,7,0,1]
verify(n, nums)

n = random.randint(3, 100)
nums = list(range(1,n+1))
nums.pop(random.randint(1,n-1))

verify(n, nums)