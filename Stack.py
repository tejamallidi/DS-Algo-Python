# We can have a custom class to mimic the functionality of a stack
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    '''
    Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
    reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
    '''

    def reverse_string(self, str_to_be_reversed):
        s = Stack()
        final_string = ''
        for letter in str_to_be_reversed:
            s.push(letter)
        while s.size() != 0:
            final_string += s.pop()
        return final_string

    '''
    Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".
    '''

    def is_balanced(self, str_to_be_evaluated):
        s = Stack()
        for letter in str_to_be_evaluated:
            # push the current letter if it is one of the brackets
            if letter == "{" or letter == "[" or letter == "(":
                s.push(letter)
            if letter == "}" or letter == "]" or letter == ")":
                # peek() check if the current bracket matches the peek() value to be a valid one
                if s.size() != 0:
                    last_letter = s.pop()
                    if last_letter == "{" and letter == "}":
                        return True
                    elif last_letter == "[" and letter == "]":
                        return True
                    elif last_letter == "(" and letter == ")":
                        return True
                    else:
                        return False
                else:
                    return False
        return s.size() == 0


if __name__ == '__main__':
    s = Stack()
    # s.push(5)
    # s.push(6)
    # s.push(7)
    # print(s.size())
    # print(s.is_empty())
    # print(s.peek())
    # print(s.pop())
    # print(s.pop()) # returns IndexError: pop from an empty deque as removed 5 already
    print(s.reverse_string('We will conquere COVID-19'))
    print(s.reverse_string('91-DIVOC ereuqnoc lliw eW'))
    print(s.is_balanced("(["))
    print(s.is_balanced("({a+b})"))  # --> True
    print(s.is_balanced("))((a+b}{"))  # --> False
    print(s.is_balanced("((a+b))"))  # --> True
    print(s.is_balanced("))"))  # --> False
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # --> True
