from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        ''' hash使うのが一番効率が良い
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        '''
        sc = deque([])
        for c in s:
            if c in ['(', '{' , '[']:
                sc.append(c)
            elif c in [')', '}' , ']'] and len(sc) != 0:
                ch = sc.pop()
                if ch == '(' and c == ')' or ch == '{' and c == '}' or ch == '[' and c == ']':
                    continue
                else:
                    return False
            else:
                return False
        if len(sc) == 0:
            return True
        else:
            return False