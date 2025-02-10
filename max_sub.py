A = [2,3,-4,-2,3,1,-2,-1,3,-2,3,1,-4,1,-3,2,2,-3]
"""
def MaxSubsequence(A):
    for i in range(1, len(A)):
        longest = 0
        c = i + 1
        for a in A[i, c]:
            new_count = longest + a
            if new_count > longest:
                longest = new_count
                return longest
"""
def MaxSubsequence(A):
    bests = 0
    beste = 0
    bestsum = A[0]
    for s in range(0,len(A)):
        for e in range(s, len(A)):
            current_sum = 0
            for i in range(s, e + 1):
                current_sum += A[i]
            if current_sum > bestsum:
                bests = s
                beste = e
                bestsum = current_sum
    print(bests)
    print(beste)
    print(bestsum)
    return bests, beste
MaxSubsequence(A)
