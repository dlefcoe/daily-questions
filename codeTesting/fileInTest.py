'''


some code will go here...



'''


import re

def solve(text, delims):
    # create regex to match words within boundaries
    reg, repl = re.compile(r"\b(\w+)\b"), "#nonword"

    # extract all words to a list, revese the list
    words = reversed(reg.findall(text))

    # substitute all words with placeholder, keeping delimeters intact
    text = reg.sub(repl, text)

    # substitude each placeholder with previously extracted words
    for x in words:
        text = re.sub(repl, x, text, count=1)

    return text

for i in ("hello/WORld:here", "hello/world:here/", "hello//world:here"):
    answer = solve(i, delims = {"/", ":"})
    print(i, " --> ", answer)
