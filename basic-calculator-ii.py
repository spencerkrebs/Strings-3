# time: O(n)
# space: O(1)
class Solution:
    def calculate(self, s: str) -> int:

        # "3+2*2"
        #.     c
        res = 0 # 5
        curr = 0 # 2
        tail = 0 # 2

        op = "+" # start with any operator *

        for i, char in enumerate(s):

            # form the multi-digit current number
            if char.isdigit():
                curr = curr * 10 + int(char)

            if char in "+-*/" or i == len(s)-1:
                if op == "+":
                    res += curr
                    tail = curr 
                elif op == '-':
                    res -= curr
                    tail = -curr
                elif op == "*":
                    # undo the previous tail addition, multiply tail with curr, add back
                    res = res - tail + (tail * curr) # 3+(2*2)=7
                    tail = tail * curr 
                elif op == '/':
                    res = res - tail + int(tail/curr)
                    tail = int(tail/curr)

                op = char
                curr = 0

        return res

# time: O(n)
# space: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        # 3+2*2
        #     c
        op = "+" # start with any operator *
        curr = 0 # 0
        stack=[] # [3,4]
        for i, char in enumerate(s):

            # form the multi-digit current number
            if char.isdigit():
                curr = curr * 10 + int(char)

            if char in "+-*/" or i == len(s)-1:
                if op == "+":
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == "*":
                    # pop last element, multiply, push back
                    stack.append(stack.pop()*curr)
                elif op == '/':
                    stack.append(int(stack.pop()/curr))

                op = char
                curr = 0

        return sum(stack)


