import math
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boats = 0

        l = 0
        r = len(people) - 1
        while l < r:
            weight = people[l] + people[r]
            if weight > limit:
                boats += 1
                r -= 1
                continue
            boats += 1
            l += 1
            r -= 1

        return boats + 1 if r == l else boats