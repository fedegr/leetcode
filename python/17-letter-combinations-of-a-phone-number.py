from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        all_combinations = ('',) if len(digits) > 0 else []
        for d in digits:
            print(all_combinations, d, chars[d])
            all_combinations = tuple( 
                f'{comb}{c}'
                for comb in all_combinations
                for c in chars[d]
            )
        
        return all_combinations