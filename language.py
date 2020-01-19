class Expression:
    def evaluate(self, scope):
        pass

class Pointer(Expression):
    def __init__(self, val):
        """val: any value to be pointed to"""
        self.val = val
    def evaluate(self, scope):
        return self.val 

class Dereferencer(Expression):
    """A Dereferencer is an Expression that returns the value of a Pointer within a Scope."""
    def __init__(self, varname: str):
        """varname: the name of the Variable to dereference"""
        self.varname = varname
    def evaluate(self, scope):
        return scope.vars[self.varname].val

class Math(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str):
        """operation: either +, -, *, /, or ^"""
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation
    def evaluate(self, scope):
        val1: float = self.expr1.evaluate(scope)
        val2: float = self.expr2.evaluate(scope)
        return {"+":val1.__add__, "-":val1.__sub__, "*":val1.__mul__, "/":val1.__truediv__, "^":val1.__pow__}[self.operation](val2)

class Comparison(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str):
        """operation: either ==, !=, <, >, <=, or >="""
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation
    def evaluate(self, scope) -> bool:
        val1 = self.expr1.evaluate(scope)
        val2 = self.expr2.evaluate(scope)
        return {"==":val1.__eq__, "!=":val1.__ne__, "<":val1.__lt__, ">":val1.__gt__, "<=":val1.__le__, ">=":val1.__ge__}[self.operation](val2)

class Statement(Expression):
    """A statement is an Expression that returns nothing when evaluated."""
    def __init__(self, func):
        self.func = func

    def evaluate(self, scope):
        """Returns nothing by definition."""
        if self.func:
            self.func(scope)

class Assignment(Statement):
    """An assignment is a Statement that assigns a Pointer to a value within a Scope."""
    def __init__(self, varname: str, varvalexpr: Expression):
        """varname: the name of the variable\n
        varvalexpr: the value to point to"""
        self.varname = varname
        self.varvalexpr = varvalexpr
    def evaluate(self, scope):
        """Assigns an evaluated expression to a name. Returns nothing."""
        val = self.varvalexpr.evaluate(scope)
        if self.varname in scope.vars:
            scope.vars[self.varname].val = val
        else:
            scope.vars[self.varname] = Pointer(val)

class Scope(Statement):
    """A scope. It stores variables, inheriting variables from outer scopes."""
    def __init__(self, statements = []):
        """statements: a list of Statements to execute in the given order"""
        self.vars = {}
        self.statements = statements
    def evaluate(self, scope=None):
        if scope:
            self.vars.update(scope.vars)
        for statement in self.statements:
            statement.evaluate(self)

class IfElse(Statement):
    """An if-elif-else block."""
    def __init__(self, ifthens: list, elsethen: Statement=None):
        """ifthens: a list of (Expression, Statement) tuples where the Expression is a condition for the Statement to execute\n
        elsethen: a Statement that executes if none of the conditions were true"""
        self.ifthens = ifthens
        self.elsethen = elsethen
    def evaluate(self, scope):
        for ifthen in self.ifthens:
            if ifthen[0].evaluate(scope):
                ifthen[1].evaluate(scope)
                return
        if self.elsethen:
            self.elsethen.evaluate(scope)

class Loop(Statement):
    """A while loop."""
    def __init__(self, condition: Expression, block: Statement):
        """condition: an Expression that evaluates to a boolean and determines whether to loop\n
        block: a Statement that executes as long as condition is true"""
        self.condition = condition
        self.block = block
    def evaluate(self, scope):
        while self.condition.evaluate(scope):
            Scope([self.block]).evaluate(scope)

class ForEach(Statement):
    """A for loop to iterate through a list."""
    def __init__(self, listexpr: Expression, itemname: str, block: Statement):
        """listexpr: an Expression that evaluates to a list\n
        itemname: a string used as the variable name that takes on the value of each element in the list\n
        block: a Statement that is executed for each item in the list"""
        self.listexpr = listexpr
        self.itemname = itemname
        self.block = block
    def evaluate(self, scope):
        for item in self.listexpr.evaluate(scope):
            Scope([
                Assignment(self.itemname, Pointer(item)),
                self.block
            ]).evaluate(scope)

        


# code in Language
Scope([
    Assignment("i", Pointer(0)),
    Loop(Comparison(Dereferencer("i"), Pointer(5), "<"), Scope([
        Assignment("i", Math(Dereferencer("i"), Pointer(1), "+")),
        Statement(lambda s: print("weeee " + str(Dereferencer("i").evaluate(s)))),
        IfElse([
            (Comparison(Dereferencer("i"), Pointer(3), "=="),
            Scope([
                Assignment("listt", Pointer(["I", "love", "you,", "Emily"])),
                ForEach(Dereferencer("listt"), "word", Statement(lambda s: print(Dereferencer("word").evaluate(s), end=' '))),
                Statement(lambda scope: print())
            ]))
        ])
    ]))
]).evaluate()

# analog in python:
# i = 0
# while i < 5:
#     i = i + 1
#     print("wweeee " + str(i))
#     if i == 3:
#         listt = ["I", "love", "you,", "Emily"]
#         for word in listt:
#             print(word, end=' ')
#         print()