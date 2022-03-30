class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letter_table = {'2': 'abc',
                        '3': 'def',
                        '4': 'ghi',
                        '5': 'jkl',
                        '6': 'mno',
                        '7': 'pqrs',
                        '8': 'tuv',
                        '9': 'wxyz'}
        # reduce fucntion
        return reduce(lambda acc, digit: [x + y for x in acc for y in letter_table[digit]], digits, [''])