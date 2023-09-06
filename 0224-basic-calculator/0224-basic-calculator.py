class Solution:
    def evaluate_subexpression(self, stack, isParen):
        result = 0 
        operand = 0 
        stage = 0
        curr = stack.pop()
        nxt = "" if not stack else stack[len(stack) - 1]
        while (isParen and nxt != "") or (not isParen and stack): 
            if type(curr) == int:  
                operand = curr
            elif curr == "-":
                result -= operand
            elif curr == "+":
                result += operand
            curr = stack.pop()
            nxt = "" if not stack else stack[len(stack) - 1]
            if isParen and nxt == "(":
                break
        if curr == "-": # if you end on a negative sign, iit's a unary operator; subtract last operand
            result -= operand 
        else: # otherwise, ends on another operator
            result += curr
        if isParen:
            stack.pop() 
        return result

    def calculate(self, s: str) -> int:
        expression_stack = []
        i = 0
        while i < len(s):  
            operand = ""
            if s[i] != " ":
                if s[i].isdigit():
                    operand = s[i]
                    while i+1 < len(s) and s[i+1].isdigit():
                        i += 1 
                        operand = operand + s[i]
                if operand != "":
                    expression_stack.append(int(operand))
                    i+=1
                    continue
                elif s[i] == ")":
                    expression_stack.append(s[i])
                    expression_stack.append(self.evaluate_subexpression(expression_stack, True))
                else:
                    expression_stack.append(s[i])
            i += 1
        return self.evaluate_subexpression(expression_stack, False)