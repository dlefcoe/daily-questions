#!/usr/bin/env python3

from hashlib import sha256

message1 = "This is the input message blah blah"
message2 = "This is the input message blah blaG"


def hash_it_up(message, fist_char):
    hashed = sha256(message.encode()).hexdigest()
    print(hashed)

    x = 0

    while True:
        x += 1
        attempt = sha256(str(x).encode()).hexdigest()
        if attempt[:fist_char] == hashed[:fist_char]:
            print(attempt)
            print(f'Cracked after {x} attempts')
            return attempt


# hash_it_up(message1)
# hash_it_up(message2)

# now same message
x = hash_it_up(message1, 2)
y = hash_it_up(message1, 3)

print(x)
print(y)



