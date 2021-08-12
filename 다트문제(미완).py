#점수 10점일 떄 어떻게 할꺼냐.. + 코드 너무 김
dartResult = "1D2S0T"
answer = 0
step_score = [0, 0, 0]
step_count = 0
i = 0
while (step_count < 2):
    step_count += 1
        #숫자 영어 특수문자 (3가지 구성요소가 다 있다면)
    if dartResult[i].isdigit() and dartResult[i+1].isupper and not dartResult[i+2].isdigit():
        print(i,"세개전부!")
        step_score[step_count-1] += int(dartResult[i])
            #대문자의 종류 검사
        if dartResult[i+1] == "S":
            step_score[step_count-1] **= 1

        elif dartResult[i+1] == "D":
            step_score[step_count-1] **= 2
        else:
            step_score[step_count-1] **= 3

            #특수문자 처리

        if dartResult[i+2] == "*":
                #2,3단계라면
            if step_count > 1:
                step_score[step_count-1] *= 2
                    #전 단계의 값에도 두배를 해준다
                step_score[step_count-2] *= 2
            #1단계라면
            else:
                step_score[step_count-1] *= 2

            # #이 나왔을 때
        else:
            step_score[step_count-1] *= (-1)

        #다음 스테이지를 계산해주기 위한 인덱스 i 업데이트
        i += 3

        #숫자 영어만 있다면(특수문자가 없다면)
    else:
        step_score[step_count-1] += int(dartResult[i])

        if dartResult[i+1] == "S":
            step_score[step_count-1] **= 1

        elif dartResult[i+1] == "D":
            step_score[step_count-1] **= 2
        else:
            step_score[step_count-1] **= 3

        i += 2

    #머리의 한계로, 인덱스 에러를 해결하지 못해 3단계는 따로 또 계산
    #3단계의 요소가 2개라면(숫자랑 알파벳만)

   
step_count += 1  # 3
if (len(dartResult)-i) == 2:
        step_score[step_count-1] += int(dartResult[i])

        if dartResult[i+1] == "S":
            step_score[step_count-1] **= 1

        elif dartResult[i+1] == "D":
            step_score[step_count-1] **= 2
        else:
            step_score[step_count-1] **= 3

    #3단계의 요소가 3개라면(*,#가 있을때)
else:
    step_score[step_count-1] += int(dartResult[i])
           #대문자의 종류 검사
    if dartResult[i+1] == "S":
        step_score[step_count-1] **= 1

    elif dartResult[i+1] == "D":
        step_score[step_count-1] **= 2
    else:
        step_score[step_count-1] **= 3

            #특수문자 처리

    if dartResult[i+2] == "*":
                #2,3단계라면
        if step_count > 1:
            step_score[step_count-1] *= 2
                    #전 단계의 값에도 두배를 해준다
            step_score[step_count-2] *= 2
                #1단계라면
        else:
            step_score[step_count-1] *= 2

            # #이 나왔을 때
    else:
        step_score[step_count-1] *= (-1)

#이러면, step_score에 각 단계의 점수가 저장되어 있다. [-2,4,3]
print(step_score)
for i in step_score:
    answer += i

print(answer)
