def solution(absolutes, signs):
    results=[]
    for i in range(len(signs)):
        if not signs[i]:
            absolutes[i]=-1*absolutes[i]
        results.append(absolutes[i])
        
        
    return sum(results)