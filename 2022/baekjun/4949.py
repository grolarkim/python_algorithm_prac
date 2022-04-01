from collections import deque

    
def yes_no(strings):
    stack = deque()
    for i in range(len(strings)):
        if strings[i] == "(":
            stack.append("(")
        elif strings[i] == "[":
            stack.append("[")
        elif strings[i] == "]":
            if stack:
                if stack.pop() != "[":
                    return print("no")
            else:
                return print("no")
        elif strings[i] == ")":
            if stack:
                if stack.pop() != "(":
                    return print("no")
            else:
                return print("no")
    if not stack:
        return print("yes")
    else:
        return print("no")

while True:    
    strings = input()
    if strings == ".":
        break
    yes_no(strings)