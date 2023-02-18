# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    position = 0
    validPair = True
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            validPair = are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], next)
            opening_brackets_stack.pop()
        position += 1
        if validPair == False: return position
    return False

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()