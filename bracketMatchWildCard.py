"""
This problem was asked by Google.
You're given a string consisting solely of (, ), and *. * can
represent either a (, ), or an empty string. Determine whether
the parentheses are balanced.
For example, (()* and () are balanced. )( is not balanced.


completed by: D Ross.
"""

def is_balanced(string, stack=0):

    # base cases
    if stack < 0:  # Too many ")" in front of "("
        return False
    elif string == "" and stack != 0:  # end of string, unbalanced
        return False
    elif string == "" and stack == 0:  # end of string, balanced
        return True

    else:  # recursive part
        first, rest = string[0], string[1:]

        if first is "(":
            return is_balanced(rest, stack + 1)

        elif first is ")":
            return is_balanced(rest, stack - 1)

        elif first is "*":
            # try for star is nothing, ( or )
            return is_balanced(rest, stack) or \
                is_balanced("(" + rest, stack) or \
                is_balanced(")" + rest, stack)
        else:
            raise ValueError  # Invalid char in string

strings = "(()) )( (() ()) ()() (()) (*)) ((*) (* ** * *) *( **) *)** (**"

for s in strings.split():
    print(s, is_balanced(s))

