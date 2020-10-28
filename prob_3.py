"""
3. Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the
  postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks,
  one for operators and one for operands, to perform the evaluation.
10.Implement a radix sorting machine. A radix sort
  for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit
  bins. Each bin acts like a queue and maintains its values in the order that they arrive. The algorithm begins by
  placing each number in the main bin. Then it considers each value digit by digit. The first value is removed and
  placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being
  considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. Once all the values are placed in the
  corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin. The process
  continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the
  values in order.
27.The linked list implementation given above is called a singly linked list because each node has a single reference
  to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation,
  each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (
  commonly called back). The head reference also contains two references, one to the first node in the linked list and
  one to the last. Code this implementation in Python.
"""


class Stack:  # a stack of blocks
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # place a new block on the stack O(1)
        self.items.append(item)

    def pop(self):  # look at and remove the top block O(1), bottom block O(n)
        return self.items.pop()

    def peek(self):  # just look at the top block O(1), bottom block O(n)
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def infix_to_postfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfix_eval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = do_math(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def infix_eval(orig):
    prob = infix_to_postfix(orig)
    sol = postfix_eval(prob)
    return sol

