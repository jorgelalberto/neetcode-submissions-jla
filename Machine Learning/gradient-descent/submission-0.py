class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        cnt = 0
        x = init

        while cnt < iterations:
            dx = 2*x # deriv of x**2
            x -= learning_rate * dx
            cnt+=1

        return round(x, 5)