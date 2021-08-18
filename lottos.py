#프로그래머스 레벨1 로또의 초고 순위와 최저 순위
def solution(lottos, win_nums):
    #lottos=[41,1,0,0,31,25]
    #win_numbers=[31,10,45,1,6,19]
    answer = []
    
    """
    두 배열에서, 같은 요소가 몇 개 있는 지 이중 반복문으로 조사, 같은 것이 나올 때 마다 count ++
    => 결국 count가 될 수 있는 최소 순위
    
    최고순위: count의 갯수에다가, 0의 갯수를 더하면, 그게 최고순위!
    
    출력부분
    조건문 6개 작성해주는건 너무 비효율 적이다.
    => 규칙 찾아냄. 순위 + 일치 번호 = 7 을 이용하면 될 것 같다.
    일치 번호가 2이상일 때만, 순위를 계산하고 그 외에는 모두 6위로
    하나하나 다 작성해야하는 상황에서, 멈추고 더 효율적인 방법을 고민하는 태도

    그리고, 파이썬이니까 솔직히 말해서 리스트간의 중복요소를 찾는 함수가 존재할 것이라
    생각했다.(실제로 존재한다)
    set intersection, 즉 set 자료형을 적절하게 잘 활용한다면 나처럼 
    일일히 반복문으로 요소 하나하나를 꺼내 확인해주는 과정을 작성할 필요가 없다.
    =>어짜피 중복이 없으니까, set자료형으로 변환
    이후 lottos와 win_numbers의 교집합을 구한 후, 그 길이를 세주면 그 길이가 일치하는 번호 개수
    len(lottos & win_numbers) 혹은 len(lottos.intersection(win_numbers))
    """
    
    #일치하는 번호가 있는지 확인해주는 과정
    count=0
    #0의 갯수 세주기
    len_zero=lottos.count(0)
    for i in win_nums:
        for j in lottos:
            if i==j:
                count+=1
                
    #최저순위 계산
    if count >= 2:
        bad_case=7-count
    else:
        bad_case=6
    
    #최고순위 계산
    if (count+len_zero) >= 2:
        good_case=7-(count+len_zero)    
    
    else:
        good_case=6
    
    answer.append(good_case)
    answer.append(bad_case)
    
    return answer