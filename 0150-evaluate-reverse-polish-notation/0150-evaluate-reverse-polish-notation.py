class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = set(['+','-','/','*'])
        for token in tokens:
            if token in operators:
                q2 = operands.pop()
                print(q2)
                q1 = operands.pop()
                print(q1)
                if token == '+':
                    operands.append(q1+q2)
                if token == '-':
                    operands.append(q1-q2)
                if token == '/':
                    quot = q1/q2
                    quot = math.floor(quot) if quot > 0 else math.ceil(quot)
                    operands.append(quot)
                if token == '*':
                    operands.append(q1*q2)
            else:
                operands.append(int(token))
        return operands[0]