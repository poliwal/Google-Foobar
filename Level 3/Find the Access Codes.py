"""
	Level-3 :- Find the Access Codes 
	Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k. The length of l is between 2 and 2000 inclusive. The elements of l are between 1 and 999999 inclusive. The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

	For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

	Test cases
	Inputs: (int list) l = [1, 1, 1] 
	Output: (int) 1

	Inputs: (int list) l = [1, 2, 3, 4, 5, 6] 
	Output: (int) 3
"""
def solution(l):
    result = 0
    c = [0] * len(l)
    for i in range(0, len(l)):
        for j in range(0, i):
            if l[i]%l[j] == 0:
                c[i] += 1
                result += c[j]
    # print(c)
    return result

print(solution([1,2,3,4,5,6]))