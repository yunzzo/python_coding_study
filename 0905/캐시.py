def solution(cacheSize, cities):
    answer = 0
    caches=[]
    # 캐시사이즈가 0이면 그냥 5x도시 길이가 정답
    if cacheSize==0:
        return 5 * len(cities)
    # 캐시사이즈가 0 보다 크다면
    for city in cities:
        #소문자화
        city=city.lower()
        #있으면, 기존에 있던 도시 제거 후 넣어주기
        if city in caches:
            #cache hit 이므로 +1
            answer+=1
            caches.pop(caches.index(city))
            caches.append(city)
        #없다면 넣어주는데, 길이를 검사해주어야 함    
        else:
            #cache miss이므로 +5
            answer+=5
            if len(caches)<cacheSize:
                caches.append(city)
            else:
                caches.pop(0)
                caches.append(city)
    
    return answer

print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))