def twoSum(data, target):
    var_key = {}
    for i, var in enumerate(data):
        var_key[var] = i
        print(var_key, var, i)
        if target - var in var_key:
            print(target, var)
            return [var_key[target - var], i]


print(twoSum([1, 8, 2, 4], 10))
