import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            match v:
                case "+":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first + second)
                case "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
                case "*":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first * second)
                case "/":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(math.trunc(first / second))
                case n:
                    stack.append(int(n))
            print(stack)

        return stack[-1]