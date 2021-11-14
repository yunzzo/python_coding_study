from itertools import tee
import numpy as np

def solution(rows, columns, queries):
    # 행렬생성
    temp = list(range(1,rows*columns+1))
    temp = [temp[i:i+rows] for i in range(0, len(temp), rows)]
    m = np.array(temp)
    

    print(m)
    return

solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])