'''

This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

The solution code was written by my friend and modded my me:
d ross

'''



openers = "{[("
closers = "}])"

inputstrings = ['([])[]({})',
                '(([{}])){}',
                '[(([{}])){}]',
                '([)]',
                '((()',
                '(()())',
                '())'
                ]

# An opener is allowed anywhere but a closer must match the last opener

def parse(inputstring):
    # Work from left to right, appending and removing from stack
    # when encountering openers and closers respectively
    stack = []
    print(f"Input is {inputstring}")

    for pos, char in enumerate(inputstring):
        if char in openers:
            stack.append(char)

        elif char in closers:
            # closer found, check last item in stack is corresponding opener
            # and if so remove it from our stack
            if not stack:
                # stack is empty so no corresponding opener exists
                print(f"Closer '{char}' found without preceeding opener at pos {pos}")
                return False

            expected_closer = closers[openers.index(stack[-1])]
            if char == expected_closer:
                stack.pop()  # all good
            else:
                # print('Expected opener or "{}" at pos {}, got "{}"'.format(expected_closer, pos, char))
                print(f'Expected opener or "{expected_closer}" at pos {pos}, got "{char}"')
                return False
    # End of string reached so stack should be empty
    if stack:
        print(f"Expected opener or '{expected_closer}', got END OF STRING")
        return False
    return True

for i in inputstrings:
    print(parse(i))



