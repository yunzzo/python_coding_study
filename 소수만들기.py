from itertools import combinations

def solution(nums):
    nums=list(set(nums))
    number_combinations_list=list(combinations(nums, 3))
    result=0
    sum_results=[]
    count=0
    
    #3개씩 조합된 수들의 합 구해서 저장
    for i in number_combinations_list:
        sum_results.append(sum(i))
        # 11의 경우 (1,3,7) (2,4,5) 도 되는 것처럼 하나의 소수가 나오는 여러 경우의 개수가 있을 수 있으니 중복을 제거하면 안된다.
        #sum_results=list(set(sum_results))
    
    #소수인지 판별
    for i in sum_results:
        for  j in range(2,i):
            if i % j == 0:
                count+=1
        #소수라면 count ==0
        if count == 0:
            print("소수발견! 소수:",i)
            result+=1
        count=0
    return result

print(solution([1,2,3,4]))
