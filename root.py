

class NewtonRaphson:

    def NewtonRaphson(eqx):
        equation = 'pow(x, 7) - 1000'
        derivative = 'pow(7*x, 6)'

        xn = 2
        ant = 0
        while ant != xn:
            ant = xn
            x1 = eval(equation.replace('x', str(xn)))
            x2 = eval(derivative.replace('x', str(xn)))
            xn = xn - (x1 / x2)

            xn = round(xn, 10)

        return xn

