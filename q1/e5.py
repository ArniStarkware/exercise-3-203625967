class LazyExpression:
    def __init__(self, *args) -> None:
        # this method should be private.
        self.expressionList = args
    def __repr__(self) -> str:
        if len(self.expressionList) == 1:
            return self.expressionList[0].__repr__()
        else:
            s = '('
            for expression in self.expressionList:
                s += expression if isinstance(expression, str) else expression.__repr__() 
            s += ')'
            return s

    def __add__(self, other):
        new_expression = LazyExpression(self, ' + ', other)
        return new_expression
    def __radd__(self,other):
        new_expression = LazyExpression(other, ' + ', self)
        return new_expression
    def __sub__(self, other):
        new_expression = LazyExpression(self, ' - ', other)
        return new_expression
    def __rsub__(self,other):
        new_expression = LazyExpression(other, ' - ', self)
        return new_expression
    
    def __mul__(self, other):
        # can even go with something like,
        # new_expression = LazyExpression(other, '*', self) if isinstance(other, int) else LazyExpression(self, '*', other)
        new_expression = LazyExpression(self, ' * ', other)
        return new_expression
    def __rmul__(self,other):
        new_expression = LazyExpression(other, ' * ', self)
        return new_expression
    def __truediv__(self, other):
        new_expression = LazyExpression(self, ' / ', other)
        return new_expression
    def __rtruediv__(self,other):
        new_expression = LazyExpression(other, ' / ', self)
        return new_expression
    def __pos__(self):
        new_expression = LazyExpression('+', self)
        return new_expression
    def __neg__(self):
        new_expression = LazyExpression('-', self)
        return new_expression
    
    def evaluate(self, **kwargs):
        if isinstance(self,LazyVariable):
            try:
                return kwargs[self.name]
            except KeyError as err:
                raise ValueError
        if len(self.expressionList) == 1:
            expression = self.expressionList[0]
            return expression
        subevaluates = []
        for subexpression in self.expressionList:
            if isinstance(subexpression, LazyExpression):
                subevaluates.append(subexpression.evaluate(**kwargs))
            else:
                subevaluates.append(subexpression)

        if len(subevaluates) == 2:
            if subevaluates[0] == '+':
                return + subevaluates[1]
            elif subevaluates[0] == '-':
                return - subevaluates[1]
            else:
                raise ValueError
        elif len(subevaluates) == 3:
            if subevaluates[1] == ' + ':
                return subevaluates[0] + subevaluates[2]
            elif subevaluates[1] == ' - ':
                return subevaluates[0] - subevaluates[2]
            elif subevaluates[1] == ' * ':
                return subevaluates[0] * subevaluates[2]
            elif subevaluates[1] == ' / ':
                return subevaluates[0] / subevaluates[2]
            else:
                raise ValueError
        else:
            raise ValueError
        pass
            

class LazyVariable(LazyExpression):
    # TODO
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def __repr__(self) -> str:
        return self.name


x = LazyVariable('x')
y = LazyVariable('y')

z = x + y
print(z.evaluate(x = 1, y = 2))