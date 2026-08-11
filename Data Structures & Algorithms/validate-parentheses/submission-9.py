class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        stacky = []

        for char in s:
            if char not in close_to_open:
                stacky.append(char)
            elif not stacky or stacky.pop() != close_to_open[char]:
                return False

        return not stacky