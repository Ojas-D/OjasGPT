class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        """
        Performs gradient descent for minimizing f(x) = x^2.
        Takes in the learning rate, number of iterations, and initial value of x.
        Returns final value of x rounded to 5 places after gradient descent.

        """
        for i in range(iterations):
            init = init - (learning_rate * (2 * init))
        round_x = round(init, 5)
        return round_x 
        
