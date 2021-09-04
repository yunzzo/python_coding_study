def solution(files):
    """
    머리부분부터 사전순으로 검사하고, 숫자 부분을 오름차순으로 검사하면, 숫자 부분에서 너무 복잡해짐. 
    숫자 부분부터 오름차순으로 검사하고, 그 다음 머리부분부터 검사하면 무조건 정답
    """
    answer = []
    #숫자부분부터 오름차순으로 검사하기
    number=""
    files_numbers=[]
    for file in files:
        for i in range(len(file)):
            #숫자부분만 꺼내기 위해서는, 그 다음요소가 숫자인지 검사
            if file[i].isdigit():
                if i+1<len(file) and file[i+1].isdigit():
                    number+=file[i]
                else:
                    number+=file[i]
                    break
        files_numbers.append((file,int(number)))
        number=""
    #number부분 오름차순으로 정렬하기
    files_numbers.sort(key=lambda x:x[1])

    # 리스트 안 튜플에서, 정렬된 원본 문자열만 취해주기 
    sorted_files=list(list(zip(*files_numbers))[0])

    #head 부분, 사전순으로 검사하기
    files_heads=[]
    head=""
    for file in sorted_files:
        for h in file:
            #문자만 모아주려면, 처음은 무조건 문자이므로 계속 넣어주다 숫자를 만나면 종료
            if h.isdigit():
                break
            head+=h.lower()
        
        files_heads.append((file,head))
        head=""
    #head를 정렬, 두번쨰 요소를 기준으로 사전순으로 정렬
    files_heads.sort(key=lambda x:x[1])

    #리스트 안 튜플에서, 정렬된 원본 문자열만 취해주기
    answer=list(list(zip(*files_heads))[0])
    return answer


print("결과",solution(["F-20 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))