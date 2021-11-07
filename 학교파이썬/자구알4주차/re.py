import re
def index_slicing(val):
    val = val.lower(); val = re.sub('[^a-z0-9]','',val)
    return val == val[::-1]

print(index_slicing(input()))