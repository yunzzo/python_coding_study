def solution(sizes): 
    answer = 0 
    sizes = [sorted(size) for size in sizes]
    small = [size[0] for size in sizes]
    large = [size[1] for size in sizes] 
    small, large = max(small), max(large)
    answer = small * large 
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))