import collections
from itertools import combinations

def solution(orders, course):
    final = []
    for c in course:
        for order in orders:
            Com = combinations(sorted(order), c)
            final += Com
        count = collections.Counter(final)      
    print(count)
    return

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])

