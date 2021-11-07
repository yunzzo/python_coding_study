from typing import *
import time

def twoSum(data: List[int], target: int)->List[int]:
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == target:
                return [data[i],data[j]]

start_time = time.time()
data = [2,7,11,15]
target = 9
result = twoSum(data,target)
end_time = time.time()
print(f'result:{result}, runtime : {end_time - start_time}')

def twoSum(data,target):
    var_key={}
    for i, var in enumerate(data):
        var_key[var] = i
        if target - var in var_key:
            return [var_key[target-var],i]
            