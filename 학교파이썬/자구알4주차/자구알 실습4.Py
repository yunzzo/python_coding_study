from dataclasses import dataclass
from typing import *

@dataclass
class Subject:
    name:str = None
    week:str = None
    credit:str = None

algorithm = Subject()
algorithm.credit = 3
print(f'algorithm credit = {algorithm.credit}')
