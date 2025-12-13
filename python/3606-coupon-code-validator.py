import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        codes = sorted(zip(code, businessLine, isActive), key=lambda x: (x[1], x[0], x[2]))
        return [
            c for (c, b, a) in codes 
            if a
            and len(code) > 0 
            and re.fullmatch("[_a-zA-Z0-9]+", c)
            and b in {"electronics", "grocery", "pharmacy", "restaurant"}
        ]

