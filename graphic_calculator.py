from graphics import *
class Stack:
    def __init__(self):
        self.A= []
    def pop(self):
        return self.A.pop()
    def top(self):
        return self.A[-1]
    def push(self, v):
        self.A.append(v)
    def isempty(self):
        return len(self.A)==0
def f(x):
    y = x*x/(x-1)
    return y
def PrintInstructions():
    print('This is how it works...')
def InfixToPostfix(infix):
    s = Stack()
    Postfix = ''
    for c in infix:
        if c in '0123456789x':
            Postfix += c
        elif c in '*/':
            if not s.isempty() and s.top() in '*/':
                Postfix += s.pop()
            s.push(c)
        elif c in '+-':
            while not s.isempty() and s.top() in '+-':
                Postfix += s.pop()
            s.push(c)
        elif c =='(':
            s.push(c)
        elif c == ')':
            while s.top() != '(':
                Postfix += s.pop()
            s.pop()
        else:
            print(f"\x1b[31munrecognized char: {c}\x1b[0m")
    while not s.isempty():
        Postfix += s.pop()
    return Postfix
def EvaluatePostfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c.isdigit():
            s.push(float(c))
        elif c == 'x':
            s.push(float(x))
        elif c == '+':
            rhs = s.pop()
            lhs = s.pop()
            v = lhs + rhs
            s.push(v)
        elif c == '-':
            rhs =  s.pop()
            lhs = s.pop()
            v = lhs - rhs
            s.push(v)
        elif c == '*':
            rhs = s.pop()
            lhs = s.pop()
            v = lhs * rhs
            s.push(v)
        elif c =='/':
            rhs = s.pop()
            lhs = s.pop()
            v = lhs / rhs
            s.push(v)
    v = s.pop()
    return v
def main():
    win = GraphWin("My Circle", 500,500)
    PrintInstructions()
    infix = input('Enter your expression. For example, x*(x+1)/(x-2) : ')
    postfix = InfixToPostfix(infix)
    print('postfix is', postfix)

    xlow = -10
    ylow= -10
    xhigh = 10
    yhigh = 10
    step = .1
    win.setCoords(xlow, ylow, xhigh, yhigh)
    x = xlow
    while x < xhigh:
        y = EvaluatePostfix(postfix, x)
        p1 = Point(x,y)
        x2 = (x + step)
        y2 = EvaluatePostfix(postfix, x2)
        p2 = Point(x2, y2)
        l = Line(p1, p2)
        l.draw(win)
        x += step
    win.getMouse()
    win.close()
main()