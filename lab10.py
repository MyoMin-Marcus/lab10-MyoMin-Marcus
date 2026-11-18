# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first): stack to keep track of the numbers, and for each operator, pop the top two numbers from the stack,
    #  apply the operator, and push the result back onto the stack.
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))
    return stack[0]


def decode_string(s):
    # Outline: stack to keep track of the current string and the number of times to repeat it. When we encounter a closing bracket, 
    # pop from the stack and build the decoded string.
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_num = 0
    current_str = ""
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == "]":
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += char
    return current_str


def daily_temperatures(temps):
    # Outline: stack to keep track of the indices of the temperatures, and for each temperature, pop from the stack until we find a warmer
    # temperature or the stack is empty. The difference in indices gives the number of days to wait.
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    stack = []
    result = [0] * len(temps)

    for i in range(len(temps) - 1, -1, -1):
        while stack and temps[stack[-1]] <= temps[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
    print(eval_rpn(["2", "1", "+", "3", "*"]))    # returns 9    ((2 + 1) * 3)
    print(eval_rpn(["4", "13", "5", "/", "+"]))   # returns 6    (4 + 13 // 5)
    print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))                   # returns [1, 1, 1, 0]
