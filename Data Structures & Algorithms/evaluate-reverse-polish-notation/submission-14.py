import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0

        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for s in tokens:
            if s in operator_map:
                proc = operator_map[s]
                first = stack.pop()
                second = stack.pop()

                val = int(proc(second, first))
                stack.append(val)
            else:
                stack.append(int(s))
        
        return stack[0]

            
