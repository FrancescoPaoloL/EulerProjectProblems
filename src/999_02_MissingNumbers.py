'''
Same problem but now we have two missing numbers.

---
arrSum => Sum of all elements in the array

Sum of 2 missing numbers = n*(n + 1) / 2 - arrSum

Because of wwo numbers can never be equal since all
the given numbers are distinct:
    - one of the numbers will be less than or equal to avg while
    - the other one will be strictly greater than avg.

Average of 2 missing numbers = sum / 2;
    - we can find the first missing number as a sum of natural numbers from 1 to avg:
          avg*(avg+1)/2 minus the sum of array elements smaller than avg;
    - We can find the second missing number by subtracting the first missing number 
      from the sum of missing numbers

Ex.
	Input : 1 2 3 4 5 6 --> 1 3 5 6
		n = 6
		- Sum of missing integers = n*(n + 1) / 2 - arrSum  --> 6*(6 + 1) / 2 - (1 + 3 + 5 + 6) = 6.
		- Average of missing integers => 6 / 2 = 3.
		- Sum of array elements less than or equal to average => 1 + 3 = 4
		- Sum of natural numbers from 1 to avg => avg*(avg + 1)/2 = 3*(3 + 1) / 2 = 6

		- First missing number = 6 - 4 = 2
		- Second missing number = Sum of missing integers-First missing number -> 6 - 2 = 4

'''
import random


def missingNrs(n, lstNumbers):
	partialSum = 0
	sumLessEqual = 0
	completeSum = n*(n + 1) // 2 
	for item in lstNumbers:
		partialSum += item
	sumMissing = completeSum - partialSum
	avgMissing = sumMissing // 2
	lst = []
	for item in lstNumbers:
		if item <= avgMissing:
			lst.append(item)
	for item in lst:
		sumLessEqual += item
	sumToAvg = int(avgMissing * (avgMissing + 1) // 2)
	n1 = sumToAvg - sumLessEqual
	n2 = int(sumMissing - n1)
	return n1, n2

def verify(n, nums):
	print(nums)
	print(f'Missing value is: {missingNrs(n, nums)}')


n = 6 # (2, 4)
nums =  [1, 2, 3, 4, 5, 6]
nums =  [1, 3, 5, 6]
verify(n, nums)

n = 7 # (4, 6)
nums =  [1, 2, 3, 4, 5, 6, 7]
nums =  [1, 2, 3, 5, 7]
verify(n, nums)

n = 17 # (2, 15)
nums =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
nums =  [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]
verify(n, nums)

n = random.randint(3, 100)
nums = list(range(1,n+1))
nums.pop(random.randint(1,n-1))
nums.pop(random.randint(1,n-1))
verify(n, nums)